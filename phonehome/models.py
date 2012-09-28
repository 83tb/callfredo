from phonehome.utils import JSONField
from django.db import models
from hundredseconds.accounts.models import User


class Call(models.Model):
    user = models.ForeignKey(User, null=False, blank=False)
    data = JSONField(json_type=dict)
    fetched_date = models.DateTimeField(auto_now_add=True)
