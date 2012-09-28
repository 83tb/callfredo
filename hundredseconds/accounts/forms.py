from django import forms
from hundredseconds.accounts.models import User


class UserPhoneForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('phone',)
