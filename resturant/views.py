from django.shortcuts import render, redirect
from django.views import generic
from .forms import CustomerForm
from .models import Customer
from datetime import datetime
from .models import News
from django.contrib import messages

def index(request):
    return render(request, 'resturant/index.html')

def home(request):
    return render(request,"index.html")

def news(request):
    news_list = News.objects.all().order_by('-created_at')[:3]  
    return render(request, 'home.html', {'news_list': news_list})

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
                messages.success(request, 'Your booking has been successfully made!')
                
            else:
                messages.error(request, "This date and time is already booked.")
    else:
        form = CustomerForm()

    # För att fylla i tidväljare i formuläret, skicka time_slots om det behövs
    context = {
        'form': form,
        # 'time_slots': time_slots  # Om du vill använda denna lista i formuläret eller mallen
    }

    return render(request, "resturant/book.html", context)


    
