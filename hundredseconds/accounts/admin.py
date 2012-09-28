from django.contrib import admin
from django.contrib.auth.models import User as AuthUser
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.utils.translation import ugettext, ugettext_lazy as _
from hundredseconds.accounts.models import User


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username",)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'phone', 'email', 'first_name', 'last_name', 'last_login', 'date_joined', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'phone')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm


admin.site.unregister(AuthUser)
admin.site.register(User, CustomUserAdmin)
