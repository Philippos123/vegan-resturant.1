from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('home/', views.index, name="home"),
    path('news/', views.news, name='news'),
    path('accounts/', include('allauth.urls')),
    path('booking/', views.book, name="book"),


]