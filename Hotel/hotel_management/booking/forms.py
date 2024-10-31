from django import forms
from .models import Hotel, Room, Booking, CustomUser
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        max_length=150,
        required=True,
    )

    class Meta:
        model = CustomUser
        fields = ["username",
                  "email",
                  "first_name",
                  "last_name",
                  "password1",
                  "password2"]

    def clean_username(self):
        username = self.cleaned_data.get('username')

        return username

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        return password1

    def clean_password2(self):
        password2 = self.cleaned_data.get('password2')

        return password2


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['user', 'room', 'start_date', 'end_date', 'guest_name']


class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ['name', 'description', 'address', 'min_price_per_night', 'rating', 'image']


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['hotel', 'price_per_night', 'is_available', 'image']