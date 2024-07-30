from django.contrib import admin
from django.urls import path
from resturant.views import my_resturant

urlpatterns = [
    path('admin/', admin.site.urls),
    path('resturant/', my_resturant, name='resturant'),

]
