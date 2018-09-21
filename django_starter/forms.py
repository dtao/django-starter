import re

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

from django_starter.models import User


class RegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')

    real_name = forms.CharField(
        label=_("Real name"), required=False, strip=True,
        help_text=_("First and last name (optional)."))

    def clean_real_name(self):
        parts = re.split(r'\s+', self.cleaned_data['real_name'])
        self.instance.first_name = parts[0]
        self.instance.last_name = ' '.join(parts[1:])
