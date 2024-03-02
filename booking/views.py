from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import BookingForm, RegistrationForm
from .models import TimeSlot, Booking
from django.contrib.auth import authenticate
from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.http import Http404
from django.db.models import Q


class BookingUpdateView(UpdateView):
    model = Booking
    fields = ['time_slot', 'comments']
    template_name = 'booking/edit_booking.html'
    success_url = reverse_lazy('user_bookings')

    # Control that the booking is the users
    def dispatch(self, request, *args, **kwargs):
        booking = self.get_object()
        if booking.user != request.user:
            raise Http404("You are not allowed to edit this booking.")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        available_time_slots = TimeSlot.objects.filter(available=True).exclude(booking__user=self.request.user)
        context['available_time_slots'] = available_time_slots
        return context


def main(request):
    return render(request, 'booking/main.html')

def show_time_slots(request):
    time_slots = TimeSlot.objects.all()
    return render(request, 'booking/make_booking.html', {'form': BookingForm(), 'time_slots': time_slots})

@login_required
def make_booking(request):
    
    user_bookings = Booking.objects.filter(user=request.user).values_list('time_slot', flat=True)

    other_users_bookings = Booking.objects.exclude(user=request.user).values_list('time_slot', flat=True)

    booked_time_slots = list(user_bookings) + list(other_users_bookings)

    available_time_slots = TimeSlot.objects.filter(available=True).exclude(id__in=booked_time_slots)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('booking_success')
    else:
        form = BookingForm()

    return render(request, 'booking/make_booking.html', {'form': form, 'time_slots': available_time_slots})

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
            print(form.errors)
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

@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    if request.method == 'POST':
        booking.delete()
        return redirect('user_bookings')
    return render(request, 'booking/cancel_booking.html', {'booking': booking})

@login_required
def user_bookings(request):
    user_bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking/user_bookings.html', {'user_bookings': user_bookings})