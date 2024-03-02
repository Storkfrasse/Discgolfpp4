from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Booking, TimeSlot

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    error_messages = {
        'password_mismatch': "The two password fields didn't match.",
        'password_too_similar_to_username': "Password is too similar to the username."
    }

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username__iexact=username).exists():
            raise ValidationError("Username already exists.", code='unique')
        return username

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password1 = cleaned_data.get('password1')

        if password1 and username and password1.lower().startswith(username.lower()):
            raise ValidationError(
                self.error_messages['password_too_similar_to_username'],
                code='password_too_similar_to_username',
            )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['time_slot', 'comments']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        available_time_slots = TimeSlot.objects.filter(booking__isnull=True)
        
        self.fields['time_slot'].queryset = available_time_slots