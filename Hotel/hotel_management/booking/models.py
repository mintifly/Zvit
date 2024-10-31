from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.username}'


class Hotel(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    min_price_per_night = models.DecimalField(max_digits=6, decimal_places=2, default=100.00)
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=1.0)
    image = models.ImageField(upload_to='hotel_images/', default='hotel_images/mrs-hotel.jpg')
    address = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name}'


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rooms')
    room_type = models.CharField(max_length=16, default='normal')
    image = models.ImageField(upload_to='room_images/', default='room_images/hilton-room.jpeg')
    price_per_night = models.DecimalField(max_digits=6, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.hotel.name}"


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='bookings')
    start_date = models.DateField()
    end_date = models.DateField()
    guest_name = models.CharField(max_length=30, default='Guest')

    def __str__(self):
        return f"Booking by {self.guest_name} ({self.user.username}) from {self.start_date} to {self.end_date}"
