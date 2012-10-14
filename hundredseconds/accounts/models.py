from django.db import models
from django.contrib.auth.models import User as AuthUser, UserManager

class User(AuthUser):
    phone = models.CharField(max_length=40, blank=True)
    calling_hour = models.IntegerField()
    calling_minute = models.IntegerField()
    objects = UserManager()

