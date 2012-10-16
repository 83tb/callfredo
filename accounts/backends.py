import datetime
import requests
from django.conf import settings
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.db.models.loading import get_model
from django.core.exceptions import ImproperlyConfigured
from facebook import GraphAPI, GraphAPIError #@UnresolvedImport
from django.core.serializers import json


class UserModelBackend(ModelBackend):

    def authenticate(self, username=None, password=None):
        try:
            user = self.user_class.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except self.user_class.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return self.user_class.objects.get(pk=user_id)
        except self.user_class.DoesNotExist:
            return None

    @property
    def user_class(self):
        if not hasattr(self, '_user_class'):
            self._user_class = get_model(*settings.CUSTOM_USER_MODEL.split('.', 2))
            if not self._user_class:
                raise ImproperlyConfigured('Could not get custom user model')
        return self._user_class

def get_graph_data(user, path, data=None):
    data = data or {}
    try:
        api = GraphAPI(user.access_token)
        r = api.get_connections('me', path, **data)
    except GraphAPIError:
        return GraphAPIError
    return r


def get_friends_birthdays(user):
    result = page = get_graph_data(user, 'friends', {'fields': 'birthday,name'})
    while 'paging' in page and 'next' in page['paging']:
        page = requests.get(result['paging']['next'])
        page = json.simplejson.loads(page.content)
        result['data'].extend(page['data'])
    return result


def get_inbox(user):
    return get_graph_data(user, 'inbox', {'fields': 'from,unread'})


def get_events(user):
    return get_graph_data(user, 'events', {})


def get_only_today_events(events):
    todays_events = []
    for ev in events['data']:
        if ev['start_time'] > str(datetime.datetime.now()) and ev['start_time'] < str(datetime.datetime.now() + datetime.timedelta(1)):
            todays_events.append(ev)

    return todays_events


def get_unread_count(inbox):
    unread = 0
    for m in inbox['data']:
        unread += m['unread']
    return unread

def get_today_bdays(bdays):

    today_birthdays = []
    for bday in bdays['data']:
        try:

            test = bday['birthday']

        except:
            bday['birthday'] = u'01/01'

        if len(bday['birthday']) <= 5:
            bday['birthday'] += u'/1970'


        if str(datetime.datetime.strptime(bday['birthday'], "%m/%d/%Y").strftime("%Y-%m-%d"))[5:] == str(datetime.date.today())[5:]:
            today_birthdays.append(bday)

        print today_birthdays



    #return today_birthdays
    #just a test
    return bdays['data']


