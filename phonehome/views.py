from facebook import GraphAPI, GraphAPIError
from twilio.rest import TwilioRestClient

from django.views.decorators.csrf import csrf_exempt
from django.views.generic.simple import direct_to_template
from django.conf import settings
from django.http import HttpResponse

from phonehome.models import Call, Recording
from hundredseconds.accounts.models import User


@csrf_exempt
def phone(request, number):
    user = User.objects.get(phone=number)
    calls = Call.objects.filter(user=user).order_by('-fetched_date')[:1]
    if calls:
        json_data = calls[0].data
    else:
        json_data = {}

    return direct_to_template(request, template='phonehome/default.xml',
                              extra_context={'json_data': json_data,
                                             'user': user})

    
def call(request, number):
    client = TwilioRestClient(settings.ACCOUNT_SID, settings.AUTH_TOKEN)
    call = client.calls.create(to=number, from_=settings.OUTGOING_NUMBER,
                               url='http://desolate-escarpment-8965.herokuapp.com/phone/twiml/%s/' % number)
    
    return HttpResponse(call.sid)


@csrf_exempt
def recording(request):
    # Called by Twilio when recording is finished
    user = None
    if request.method == 'POST':
        Recording.objects.create(call_sid=request.POST.get('CallSid'),
                                 caller=request.POST.get('From'),
                                 recipient=request.POST.get('To'),
                                 duration=int(request.POST.get('RecordingDuration')),
                                 url=request.POST.get('RecordingUrl'))


        number = request.POST.get('To')[1:] # Remove leading '+'
        try:
            user = User.objects.get(phone=number)
            social_user = user.social_auth.get(provider='facebook')
            api = GraphAPI(social_user.extra_data.get('access_token'))
            api.put_wall_post("Wishing you a happy birthday!",
                              profile_id='1557648750', # TODO: Change from Ola to dynamic
                              attachment= {'name': 'Your Birthday Wishes!',
                                           'link': request.POST.get('RecordingUrl') + '.mp3', 
                                           'caption': '',
                                           'description': '',
                                           'picture': 'http://desolate-escarpment-8965.herokuapp.com/static/img/cakeisalie.jpeg'})
        except (User.DoesNotExist, GraphAPIError):
            user = None
    
    return direct_to_template(request, template='phonehome/afterrecording.xml',
                              extra_context={'user': user})
