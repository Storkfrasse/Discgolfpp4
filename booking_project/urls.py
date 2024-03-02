"""
URL configuration for booking_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from booking import views

urlpatterns = [
    path('', views.main, name='main'),
    path('admin/', admin.site.urls),
    path('time-slots/', views.show_time_slots, name='show_time_slots'),
    path('make-booking/', views.make_booking, name='make_booking'),
    path('edit-booking/<int:pk>/', views.BookingUpdateView.as_view(), name= 'edit-booking'),
    path('booking-success/', views.booking_success, name='booking_success'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'), 
    path('logout/', views.user_logout, name='user_logout'),
    path('cancel-booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('user-bookings/', views.user_bookings, name='user_bookings'),
]
