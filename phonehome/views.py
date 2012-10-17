import datetime
from facebook import GraphAPI, GraphAPIError #@UnresolvedImport
from twilio.rest import TwilioRestClient
from twilio import twiml

from django.views.decorators.csrf import csrf_exempt
from django.views.generic.simple import direct_to_template
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import HttpResponse

from phonehome.models import Call, Recording, Birthday
from accounts.models import User


@csrf_exempt
def phone(request, number):
    user = User.objects.get(phone=number)
    call = Call.objects.filter(user=user).order_by('-fetched_date')[:1]
    resp = twiml.Response()
    resp.pause(length="3")

    if Birthday.objects.filter(call=call).count()==0:
        resp.say("No one of your friends has birthday today. Have a nice day!")
    else:
        bdays = Birthday.objects.filter(call=call)
        resp.say("Hi %s! %i of your friends have birthday today:" % (user.first_name, bdays.count()))
        for bday in bdays:
            resp.say(bday.recipient_fb_name)

        for bday in bdays:
            with resp.gather(timeout=2, action="http://callfredo.com/phone/press/"+str(bday.id)+"/", method="POST") as g:
                g.say("If you want record birthday wishes for %s, press 1. If you want to skip recording, then press 2." % bday.recipient_fb_name)


    return HttpResponse(str(resp), content_type='application/xml')

@csrf_exempt
def press(request, id):
    bday = Birthday.objects.get(id=id)
    resp = twiml.Response()
    resp.pause(length="3")

    if int(request.POST['Digits'])==1:
        bday.status = 1
        bday.save()

        resp.record(playBeep=True, maxLength="10", method="POST", action="http://callfredo.com/phone/recording/"+str(bday.id)+"/")
    else:
        bday.status = 2
        bday.save()

        if Birthday.objects.filter(call=bday.call, status=0).count()>0:
            bday = Birthday.objects.filter(call=bday.call, status=0)[:1].get()
            with resp.gather(timeout=3, action="http://callfredo.com/phone/press/"+str(bday.id)+"/", method="POST") as g:
                g.say("If you want record birthday wishes for %s, press 1. If you want to skip recording, then press 2." % bday.recipient_fb_name)

        else:
            resp.say("That is it! All wishes have been posted. Have a nice day!")
            resp.hangup()

    return HttpResponse(str(resp), content_type='application/xml')

@login_required
def call(request, number):
    today = datetime.date.today()
    user = request.user
    data = request.user.create_call()
    #if user.last_call_date == today:
    #    return direct_to_template(request, template='error.html', extra_context={})
    client = TwilioRestClient(settings.ACCOUNT_SID, settings.AUTH_TOKEN)

    call = client.calls.create(to=number, from_=settings.OUTGOING_NUMBER,
                               url='http://callfredo.com/phone/twiml/%s/' % number)
    user.last_call_date = today
    user.save()

    return direct_to_template(request, template='done.html', extra_context={})

import time

@csrf_exempt
def recording(request, id):
    # Called by Twilio when recording is finished
    user = None
    bday = Birthday.objects.get(id=id)

    if request.method == 'POST':
        call = bday.call
        user = call.user
        social_user = user.social_auth.get(provider='facebook')
        api = GraphAPI(social_user.extra_data.get('access_token'))
        number = user.phone

        recording = Recording(call_sid=request.POST.get('CallSid'),
                                 caller=request.POST.get('From'),
                                 recipient=request.POST.get('To'),
                                 duration=int(request.POST.get('RecordingDuration')),
                                 url=request.POST.get('RecordingUrl'),
                                 fb_user_name=bday.recipient_fb_name)
        recording.save()

        bday.recording = recording
        bday.save()
        url = str('http://callfredo.com/wishes/') + str(bday.recording.id) + str('/')
        try:
            api.put_wall_post("Happy birthday!",
                              profile_id=str(bday.recipient_fb_id),
                              attachment={'name': 'Happy birthday!', 'link': str(url), })
        except (User.DoesNotExist, GraphAPIError):
            user = None

    resp = twiml.Response()
    resp.pause(length="3")

    if Birthday.objects.filter(call=bday.call, status=0).count()>0:
        bday = Birthday.objects.filter(call=bday.call, status=0)[:1].get()
        with resp.gather(timeout=3, action="http://callfredo.com/phone/press/"+str(bday.id)+"/", method="POST") as g:
            g.say("If you want record birthday wishes for %s, press 1. If you want to skip recording, then press 2." % bday.recipient_fb_name)

    else:
        resp.say("That is it! All wishes have been posted. Have a nice day!")
        resp.hangup()

    return HttpResponse(str(resp), content_type='application/xml')
