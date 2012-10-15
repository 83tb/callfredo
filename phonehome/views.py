import datetime
from facebook import GraphAPI, GraphAPIError #@UnresolvedImport
from twilio.rest import TwilioRestClient

from django.views.decorators.csrf import csrf_exempt
from django.views.generic.simple import direct_to_template
from django.contrib.auth.decorators import login_required
from django.conf import settings

from phonehome.models import Call, Recording
from accounts.models import User


@csrf_exempt
def phone(request, number):
    user = User.objects.get(phone=number)
    calls = Call.objects.filter(user=user).order_by('-fetched_date')[:1]
    if calls:
        json_data = calls[0].data
        jubilat = calls[0].data['bdays'][0]['name']
    else:
        json_data = {}

    return direct_to_template(request, template='default.xml',
                              extra_context={'json_data': json_data,
                                             'jubilat' : jubilat,
                                             'user': user})

@login_required
def call(request, number):
    today = datetime.date.today()
    user = request.user
    if user.last_call_date == today:
        return direct_to_template(request, template='error.html', extra_context={})

    client = TwilioRestClient(settings.ACCOUNT_SID, settings.AUTH_TOKEN)
    call = client.calls.create(to=number, from_=settings.OUTGOING_NUMBER,
                               url='http://callfredo.com/phone/twiml/%s/' % number)
    user.last_call_date = today
    user.save()
    return direct_to_template(request, template='done.html', extra_context={})


@csrf_exempt
def recording(request):
    # Called by Twilio when recording is finished
    user = None
    if request.method == 'POST':
        recording = Recording(call_sid=request.POST.get('CallSid'),
                                 caller=request.POST.get('From'),
                                 recipient=request.POST.get('To'),
                                 duration=int(request.POST.get('RecordingDuration')),
                                 url=request.POST.get('RecordingUrl'))
        recording.save()

        number = request.POST.get('To')[2:] # Remove leading '+1'
        try:
            user = User.objects.get(phone=number)
            social_user = user.social_auth.get(provider='facebook')
            api = GraphAPI(social_user.extra_data.get('access_token'))

            call = Call.objects.filter(user=user).order_by('-id')[:1].get()

            api.put_wall_post("Happy birthday!",
                              profile_id=call.data['bdays'][0]['id'],
                              attachment={'name': 'Happy birthday!',
                                           'link': 'http://callfredo.com/wishes/' + str(recording.id) + '/', })
        except (User.DoesNotExist, GraphAPIError):
            user = None

    return direct_to_template(request, template='afterrecording.xml',
                              extra_context={'user': user})
