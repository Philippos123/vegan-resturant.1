from django.contrib import admin
from .models import Post
from .models import Comment
from .models import Customer
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'booking_date', 'booking_time', 'display_number_of_people')

    def display_number_of_people(self, obj):
        return obj.number_of_people

    display_number_of_people.short_description = 'Number of People'

admin.site.register(Customer, CustomerAdmin)

# Register your models here.

