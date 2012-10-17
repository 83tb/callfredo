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
        bdays = backends.get_today_bdays(backends.get_friends_birthdays(self))

        data = {
            'name' : self.get_full_name(),
            'bdays' : bdays,
        }

        from phonehome.models import Call, Birthday
        call = Call(user=self, fetched_date=now, data=data)
        call.save()

        for bday in bdays:
            Birthday.objects.create(call=call, recipient_fb_name=bday['name'], recipient_fb_id=bday['id'])

        return str(data)
