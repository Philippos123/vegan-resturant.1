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
    path('my-bookings/', views.my_bookings, name="my_booking"),
    path('booking/<int:booking_id>/update/', views.update_booking, name='update_booking'),
    path('booking/<int:booking_id>/delete/', views.delete_booking, name='delete_booking'),

]