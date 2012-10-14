from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.views.generic import TemplateView, UpdateView
from hundredseconds.accounts.forms import UserPhoneForm


class IndexView(TemplateView):
    template_name = 'index.html'


class GiveNumberView(UpdateView):
    form_class = UserPhoneForm
    template_name = 'givenumber.html'

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        super(GiveNumberView, self).form_valid(form)
        url = reverse('schedule')
        return HttpResponseRedirect(url)


class ConfirmNumberView(TemplateView):
    template_name = 'confirmnumber.html'


class ScheduleView(TemplateView):
    template_name = 'schedule.html'


class SaveInContactsView(TemplateView):
    template_name = 'saveincontacts.html'


class TryItView(TemplateView):
    template_name = 'tryit.html'


def PlayerView(request):

    code = request.GET['code']
    return render_to_response('player.html', {'code':code })


def birthdays(request):
    data = request.user.create_call()
    return HttpResponse(data)
