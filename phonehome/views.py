from twilio.rest import TwilioRestClient

from django.views.decorators.csrf import csrf_exempt
from django.views.generic.simple import direct_to_template
from django.conf import settings
from django.http import HttpResponse

from phonehome.models import Recording


@csrf_exempt
def phone(request):
    return direct_to_template(request, template='phonehome/default.xml')

    
def call(request, number):
    client = TwilioRestClient(settings.ACCOUNT_SID, settings.AUTH_TOKEN)
    call = client.calls.create(to=number, from_=settings.OUTGOING_NUMBER,
                               url='http://desolate-escarpment-8965.herokuapp.com/phone/')
    
    return HttpResponse(call.sid)


@csrf_exempt
def recording(request):
    # Called by Twilio when recording is finished
    if request.method == 'POST':
        Recording.objects.create(call_sid=request.POST.get('CallSid'),
                                 caller=request.POST.get('From'),
                                 recipient=request.POST.get('To'),
                                 duration=int(request.POST.get('RecordingDuration')),
                                 url=request.POST.get('RecordingUrl'))
    
    return HttpResponse('OK')
