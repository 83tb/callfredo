from django.views.generic.base import TemplateView
from hundredseconds.accounts.backends import get_friends_birthdays, get_events, get_inbox
from django.http import HttpResponse

TEMPLATES_DIR = 'accounts/'

class SocialErrorView(TemplateView):
    template_name = TEMPLATES_DIR + 'error.html'


from hundredseconds.views import getData


def birthdays(request):
    bdays = get_friends_birthdays(request.user)
    events = get_events(request.user)
    inbox = get_inbox(request.user)

    data = getData(events.text, bdays.text, inbox.text)

    return HttpResponse(data)





