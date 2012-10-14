from phonehome.utils import JSONField
from django.db import models
from hundredseconds.accounts.models import User


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


