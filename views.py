from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, render
from django.views.generic import TemplateView, UpdateView
from accounts.forms import UserPhoneForm


class IndexView(TemplateView):
    template_name = 'index.html'


class GiveNumberView(UpdateView):
    form_class = UserPhoneForm
    template_name = 'givenumber.html'

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        super(GiveNumberView, self).form_valid(form)
        url = reverse('tryit')
        return HttpResponseRedirect(url)

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

    return render_to_response('player.html', {'url':recording.url })


def birthdays(request):
    data = request.user.create_call()
    return HttpResponse(data)
