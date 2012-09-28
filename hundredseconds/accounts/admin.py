from django.contrib import admin
from hundredseconds.accounts.models import User
from django.contrib.auth.models import User as AuthUser
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'phone', 'email', 'first_name', 'last_name', 'last_login', 'date_joined', 'is_staff')


admin.site.unregister(AuthUser)
admin.site.register(User, CustomUserAdmin)
