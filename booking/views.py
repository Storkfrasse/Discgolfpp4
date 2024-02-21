from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import BookingForm
from .models import TimeSlot, Booking
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login

def main(request):
    return render(request, 'booking/main.html')

def show_time_slots(request):
    time_slots = TimeSlot.objects.all()
    return render(request, 'booking/make_booking.html', {'form': BookingForm(), 'time_slots': time_slots})

def make_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('booking_success')
    else:
        form = BookingForm()
    return render(request, 'booking/make_booking.html', {'form': form, 'time_slots': TimeSlot.objects.all()})

def booking_success(request):
    return render(request, 'booking/booking_success.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('make_booking')
    else:
        form = RegistrationForm()
    return render(request, 'booking/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('make_booking')
            else:
                # Handle invalid credentials
                # You might want to display an error message
                pass
    else:
        form = AuthenticationForm()
    return render(request, 'booking/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('main')

def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('booking_success')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'booking/edit_booking.html', {'form': form, 'booking': booking})

def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    if request.method == 'POST':
        booking.delete()
        return redirect('booking_success')
    return render(request, 'booking/cancel_booking.html', {'booking': booking})