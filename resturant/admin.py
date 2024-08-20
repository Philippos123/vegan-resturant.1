from django.contrib import admin
from .models import Customer, News
from django_summernote.admin import SummernoteModelAdmin


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ['title', 'content']
    list_filter = ('created_at',)

    def save_model(self, request, obj, form, change):
        # Custom logic can be added here if needed before saving the object
        super().save_model(request, obj, form, change)


admin.site.register(News)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'booking_date', 'booking_time', 'display_number_of_people')

    def display_number_of_people(self, obj):
        return obj.number_of_people

    display_number_of_people.short_description = 'Number of People'

admin.site.register(Customer, CustomerAdmin)

# Register your models here.

