from django.db import models
from django.contrib.auth.models import User as AuthUser, UserManager

class User(AuthUser):
    phone = models.CharField(max_length=40, blank=True)

    objects = UserManager()

