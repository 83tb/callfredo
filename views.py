from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, render
from django.views.generic import TemplateView, UpdateView
from accounts.models import User
from accounts.forms import UserPhoneForm
from phonehome.models import Recording


class IndexView(TemplateView):
    template_name = 'index.html'


class GiveNumberView(UpdateView):
    form_class = UserPhoneForm
    template_name = 'givenumber.html'
    success_url = reverse_lazy('tryit')

    def get_object(self):
        return self.request.user


"""
class ConfirmNumberView(TemplateView):
    template_name = 'confirmnumber.html'


class ScheduleView(TemplateView):
    template_name = 'schedule.html'


class SaveInContactsView(TemplateView):
    template_name = 'saveincontacts.html'
"""

def TryItView(request):
    return render(request, 'tryit.html', { 'phone': request.user.phone, })


def PlayerView(request, id=0):
    try:
        recording = Recording.objects.get(id=id)
    except:
        return HttpResponseRedirect(reverse('index'))

    caller = User.objects.get(phone=recording.recipient.replace("+1",""))

    return render_to_response('player.html', {'url':recording.url, 'caller':caller, })


def birthdays(request):
    data = request.user.create_call()
    return HttpResponse(data)
