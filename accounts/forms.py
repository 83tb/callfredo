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
        try:
            test = int(self.cleaned_data['phone'])
        except:
            raise ValidationError('Phone number should contain only numbers.')
        if len(str(self.cleaned_data['phone']))!=10:
            raise ValidationError('Please provide proper US phone number.')
        return self.cleaned_data['phone']


class ConfirmForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('code',)

    def __init__(self, *args, **kwargs):
        super(ConfirmForm, self).__init__(*args, **kwargs)
        self.fields['code'].widget.attrs['class'] = 'text'

    def clean_code(self):
        if self.fields['code'] != self.cleaned_data['code']:
            raise ValidationError('Code is incorrect.')
        return self.cleaned_data['code']

