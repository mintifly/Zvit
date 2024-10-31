from django.contrib import admin
from .models import Hotel, Room, Booking, CustomUser

admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(CustomUser)