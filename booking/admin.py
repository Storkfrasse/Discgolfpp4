from django.contrib import admin
from .models import UserProfile, TimeSlot, Booking

admin.site.register(UserProfile)
admin.site.register(TimeSlot)
admin.site.register(Booking)

