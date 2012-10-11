from django.views.generic.base import TemplateView
from django.shortcuts import render_to_response
from accounts.models import User
from hundredseconds.accounts.forms import UserPhoneForm


class IndexView(TemplateView):
    template_name = 'index.html'

class GiveNumberView(TemplateView):
    template_name = 'givenumber.html'




def PlayerView(request):

    code = request.GET['code']
    return render_to_response('player.html', {'code':code })



from filter_fb_data import *
from phonehome.models import Call
from datetime import datetime


def getData(events, bdays, inbox):

    now = datetime.now()
    data = {
        'name' : "Kuba Kucharski",
        'unread' : get_unread_count(inbox),
        'events' : get_only_today_events(events),
        'bdays' : get_today_bdays(bdays),
        }


    Call.create(fetched_date=now, data=str(data), user=User.objects.filter(id=1))

    return data




"""

{ 'name' : "Kuba Kucharski",
'unread' : 0,
'events' : ['openreaktor','rails'],
'bdays' : 'name',
}




"""


