from django import forms
from django.forms.widgets import PasswordInput, TextInput
from .models import Traveler


class TravelerForm(forms.ModelForm):
    class Meta:
        model = Traveler
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'province', 'country', 'travel_date', 'return_date', 'country_destination']
        