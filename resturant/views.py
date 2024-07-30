from django.shortcuts import render
from django.http import HttpResponse

def my_resturant(request):
    return HttpResponse("Hello, resturant!")
