from django.db import models
from django.contrib.auth.models import User as AuthUser, UserManager

class User(AuthUser):

    objects = UserManager()

