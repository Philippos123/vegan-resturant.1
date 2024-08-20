from django.shortcuts import render, redirect
from django.views import generic
from .forms import CustomerForm
from .models import Customer
from datetime import datetime
from .models import News

def index(request):
    return render(request, 'resturant/index.html')

def news_list(request):
    news_list = News.objects.all()
    return render(request, 'news_list.html', {'news_list': news_list})

def news(request):
    news_list = News.objects.all().order_by('-created_at')[:3]  
    return render(request, 'home.html', {'news_list': news_list})

def book(request):
    form = CustomerForm()

    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            
            booking_date = form.cleaned_data['booking_date']
            booking_time = form.cleaned_data['booking_time']

            
            existing_booking = Customer.objects.filter(booking_date=booking_date, booking_time=booking_time).exists()

            if not existing_booking:
                
                form.save()
                return redirect('home')
            else:
                
                form.add_error(None, "This date and time is already booked.")
               
    time_slots = [f"{i:02d}" for i in range(0, 61, 15)]

    context = {'form': form}
    return render(request, "resturant/book.html")


    
