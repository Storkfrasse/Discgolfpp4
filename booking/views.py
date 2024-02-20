from django.shortcuts import render, redirect
from .models import TimeSlot, Booking
from .forms import BookingForm

def main(request):
    return render(request, 'booking/main.html')

def show_time_slots(request):
    time_slots = TimeSlot.objects.all()
    return render(request, 'booking/make_booking.html', {'form': BookingForm(), 'time_slots': time_slots})

def make_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_success')
    else:
        form = BookingForm()
    return render(request, 'booking/make_booking.html', {'form': form, 'time_slots': TimeSlot.objects.all()})

def booking_success(request):
    return render(request, 'booking/booking_success.html')