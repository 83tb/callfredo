import re

from django import forms
from django.forms import ValidationError

from accounts.models import User


class UserPhoneForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('phone',)

    def __init__(self, *args, **kwargs):
        super(UserPhoneForm, self).__init__(*args, **kwargs)
        self.fields['phone'].widget.attrs['class'] = 'text'

    def clean_phone(self):
        if not re.match(r'[0-9]+', self.cleaned_data['phone']):
            raise ValidationError('Phone number should contain only numbers.')
        return self.cleaned_data['phone']


class ConfirmForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('code',)

    def __init__(self, *args, **kwargs):
        super(ConfirmForm, self).__init__(*args, **kwargs)
        self.fields['code'].widget.attrs['class'] = 'text'

