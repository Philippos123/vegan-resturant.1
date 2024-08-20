from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('news/', views.news_list, name='news_list'),
    path('accounts/', include('allauth.urls')),


]