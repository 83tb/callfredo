from django import forms
from hundredseconds.accounts.models import User


class UserPhoneForm(forms.Form):

    class Meta:
        model = User
        fields = ('phone',)
