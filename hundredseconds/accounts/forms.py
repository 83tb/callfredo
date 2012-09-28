import re

from django import forms
from django.forms import ValidationError

from hundredseconds.accounts.models import User


class UserPhoneForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('phone',)

    def clean_phone(self):
        if not re.match(r'[0-9]+', self.cleaned_data['phone']):
            raise ValidationError('Phone number should contain only numbers.')
        return self.cleaned_data['phone']
