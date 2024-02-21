from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Booking

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['time_slot', 'comments']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comments'].widget.attrs['class'] = 'readonly-field'