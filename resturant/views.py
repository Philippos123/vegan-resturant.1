from django.shortcuts import render
from django.views import generic
from .models import News, Post

def index(request):
    return render(request, 'resturant/index.html')

