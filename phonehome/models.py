from phonehome.utils import JSONField
from django.db import models
from accounts.models import User


class Call(models.Model):
    user = models.ForeignKey(User, null=False, blank=False)
    data = JSONField(json_type=dict, default='{}')
    fetched_date = models.DateTimeField(auto_now_add=True)

class Recording(models.Model):
    call_sid = models.CharField(max_length=240)
    caller = models.CharField(max_length=240)
    recipient = models.CharField(max_length=240)
    duration = models.IntegerField()
    url = models.CharField(max_length=240)
    fb_user_name = models.CharField(max_length=240, null=True, blank=True, default=None)

class Birthday(models.Model):
    call = models.ForeignKey(Call, null=False, blank=False)
    recording = models.ForeignKey(Recording, null=True, blank=True, default=None)
    recipient_fb_name = models.CharField(null=False, blank=False)
    recipient_fb_id = models.BigIntegerField(null=False, blank=False)
    status = models.IntegerField(null=False, blank=False, default=0, choices=((0,'Fetched'),(1,'Posted'),(2,'Skipped')))
