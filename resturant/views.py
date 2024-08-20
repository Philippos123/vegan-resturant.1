from django.shortcuts import render
from django.views import generic
from .models import News, Post

def index(request):
    return render(request, 'resturant/index.html')

def news_list(request):
    news_list = News.objects.all()
    return render(request, 'news_list.html', {'news_list': news_list})

def home(request):
    news_list = News.objects.all().order_by('-created_at')[:3]  
    return render(request, 'home.html', {'news_list': news_list})