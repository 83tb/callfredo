from twilio.rest import TwilioRestClient

from django.views.decorators.csrf import csrf_exempt
from django.views.generic.simple import direct_to_template
from django.conf import settings


@csrf_exempt
def phone(request):
    return direct_to_template(request, template='phonehome/default.xml')

    
def call(request):
    client = TwilioRestClient(settings.ACCOUNT_SID, settings.AUTH_TOKEN)
    call = client.calls.create(to="+48728858525", from_=settings.OUTGOING_NUMBER,
                               url='http://desolate-escarpment-8965.herokuapp.com/phone/')
    return str(call.sid)
