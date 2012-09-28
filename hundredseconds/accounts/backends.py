from django.conf import settings
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.db.models.loading import get_model
from django.core.exceptions import ImproperlyConfigured
import requests


FACEBOOK_GRAPH_URL = 'https://graph.facebook.com/'
FACEBOOK_ME = 'https://graph.facebook.com/me/'


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
    social_user = user.social_auth.get(provider='facebook')
    data = data or {}
    data.update({
        'access_token': social_user.extra_data.get('access_token'),
    })
    url = FACEBOOK_ME + path
    r = requests.get(url, data=data)
    return r.json

def get_firends_birthdays(user):
    return get_graph_data(user, 'friends', {'fields': 'birthday'})

def get_inbox(user):
    return get_graph_data(user, 'inbox ', {'fields': 'from,unread'})

def get_events(user):
    return get_graph_data(user, 'events ', {})

