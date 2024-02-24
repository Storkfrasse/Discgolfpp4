from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email_address = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.user.username

class TimeSlot(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    max_bookings = models.IntegerField(default=1)  # Max bookings for timeslot
    available = models.BooleanField(default=True)

    @classmethod
    def available_time_slots(cls, user):
        user_bookings = Booking.objects.filter(user=user).values_list('time_slot', flat=True)
        return cls.objects.filter(available=True).exclude(id__in=user_bookings)

    def available_slots(self):
        """
        Spots for timeslot
        """
        booked_slots = self.booking_set.count()
        available_slots = self.max_bookings - booked_slots
        return available_slots

    def __str__(self):
        return f"{self.start_time.strftime('%Y-%m-%d %H:%M')} to {self.end_time.strftime('%Y-%m-%d %H:%M')}"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_slot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)
    booking_time = models.DateTimeField(auto_now_add=True)
    comments = models.TextField(blank=True)