from django.contrib import admin
from django.contrib.auth.models import User as AuthUser
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.utils.translation import ugettext, ugettext_lazy as _
from hundredseconds.accounts.models import User
from django.core.urlresolvers import reverse


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username",)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'phone', 'call', 'email', 'first_name', 'last_name', 'last_login', 'date_joined', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'phone')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    def call(self, obj):
        return '<a href="%s">Call</a>' % reverse('call', kwargs={'number': obj.phone})
    call.allow_tags = True
    call.short_description = 'Call'


admin.site.unregister(AuthUser)
admin.site.register(User, CustomUserAdmin)
