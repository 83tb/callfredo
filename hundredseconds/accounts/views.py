from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
from hundredseconds.accounts.forms import UserPhoneForm
from hundredseconds.accounts.backends import get_friends_birthdays, get_events, get_inbox
from django.http import HttpResponseRedirect, HttpResponse

TEMPLATES_DIR = 'accounts/'


class SocialErrorView(TemplateView):
    template_name = TEMPLATES_DIR + 'error.html'


class LoggedInView(TemplateView):
    template_name = 'loggedin.html'

    def get_context_data(self, **kwargs):
        data = super(LoggedInView, self).get_context_data(**kwargs)
        data['form'] = UserPhoneForm()
        if self.request.user.is_authenticated():
            data['form'] = UserPhoneForm(instance=self.request.user)
        return data


class PhoneUpdateView(UpdateView):
    form_class = UserPhoneForm

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        super(PhoneUpdateView, self).form_valid(form)
        referer = self.request.META.get('HTTP_REFERER', '/')
        return HttpResponseRedirect(referer)


from hundredseconds.views import getData



def birthdays(request):
    bdays = get_friends_birthdays(request.user)
    events = get_events(request.user)
    inbox = get_inbox(request.user)


    data = getData(events.text, bdays.text, inbox.text)



    return HttpResponse(data)





