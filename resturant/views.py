from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .forms import CustomerForm
from .models import Customer
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import News
from django.contrib import messages


def index(request):
    news_list = News.objects.all().order_by('-created_at')
    return render(request, 'resturant/index.html', {'news_list': news_list})


def home(request):
    return render(request, "index.html")


# News function views
def news(request):
    news_list = News.objects.all().order_by('-created_at')
    print(news_list)
    return render(request, 'index.html', {'news_list': news_list})


# Book a table views
def book(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            booking_date = form.cleaned_data['booking_date']
            booking_time = form.cleaned_data['booking_time']

            # Check if the date and time are already booked
            existing_booking = Customer.objects.filter(
                booking_date=booking_date, booking_time=booking_time
            ).exists()

            if not existing_booking:
                booking = form.save(commit=False)
                booking.user = request.user
                booking.save()
                messages.success(request,
                                 "Your booking has been successfully made!")
            else:
                messages.error(request,
                               "This date and time is already booked.")
    else:
        form = CustomerForm()

    return render(request, "resturant/book.html", {'form': form})


@login_required
def my_bookings(request):
    bookings = Customer.objects.filter(user=request.user)
    return render(
        request,
        'resturant/my_bookings.html',
        {'bookings': bookings}
    )


@login_required
def update_booking(request, booking_id):
    booking = get_object_or_404(Customer, id=booking_id, user=request.user)

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=booking)
        if form.is_valid():
            updated_booking = form.save(commit=False)
            # Check if the new date and time are already booked
            if not Customer.objects.filter(
                booking_date=updated_booking.booking_date,
                booking_time=updated_booking.booking_time
            ).exclude(id=booking_id).exists():
                updated_booking.save()
                messages.success(request,
                                 "Your booking has been successfully updated!")
            else:
                messages.error(request,
                               "This date and time is already booked.")
    else:
        form = CustomerForm(instance=booking)

    return render(request, 'resturant/update_booking.html', {'form': form})


@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(Customer, id=booking_id, user=request.user)

    if request.method == 'POST':
        booking.delete()
        messages.success(request,
                         "Your booking has been successfully deleted!")

    return render(
        request,
        'resturant/delete_booking.html',
        {'booking': booking}
    )




    
