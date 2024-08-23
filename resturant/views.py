from django.shortcuts import render, redirect
from django.views import generic
from .forms import CustomerForm
from .models import Customer
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

            # Kontrollera om datum och tid redan är bokade
            existing_booking = Customer.objects.filter(booking_date=booking_date, booking_time=booking_time).exists()

            if not existing_booking:
                form.save()
                
                messages.success(request, "Your booking has been successfully made!")

            else:
                messages.error(request, "This date and time is already booked.")
    else:
        form = CustomerForm()

    context = {
        'form': form,
        # 'time_slots': time_slots
    }

    return render(request, "resturant/book.html", context)


    
