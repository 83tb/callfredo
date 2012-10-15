import datetime
from django.db import models
from django.contrib.auth.models import User as AuthUser, UserManager
from accounts import backends

class User(AuthUser):
    phone = models.CharField(max_length=40, blank=True)
    calling_hour = models.IntegerField(default=0)
    calling_minute = models.IntegerField(default=0)
    last_call_date = models.DateField(default=lambda: datetime.date.today() - datetime.timedelta(days=1))
    objects = UserManager()

    @property
    def access_token(self):
        return self.social_auth.get(provider='facebook').extra_data.get('access_token')

    def create_call(self):
        now = datetime.datetime.now()
        bdays = backends.get_friends_birthdays(self)
        events = backends.get_events(self)
        inbox = backends.get_inbox(self)

        data = {
            'name' : self.get_full_name(),
            'unread' : backends.get_unread_count(inbox),
            'events' : backends.get_only_today_events(events),
            'bdays' : backends.get_today_bdays(bdays),
        }

        from phonehome.models import Call
        Call.objects.create(user=self, fetched_date=now, data=data)

        return str(data)
