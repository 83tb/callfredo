from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
from hundredseconds.accounts.forms import UserPhoneForm
from hundredseconds.accounts.backends import get_firends_birthdays
from django.http import HttpResponseRedirect, HttpResponse

TEMPLATES_DIR = 'accounts/'


class SocialErrorView(TemplateView):
    template_name = TEMPLATES_DIR + 'error.html'


class PhoneUpdateView(UpdateView):
    form_class = UserPhoneForm

    def get_object(self):
        return self.request.user

    def get_success_url(self):
        referer = request.META.get('HTTP_REFERER', '/')
        return HttpResponseRedirect(referer)


def birthdays(request):
    data = get_firends_birthdays(request.user)
    return HttpResponse(data)
