from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import os
import logging

from django.core.exceptions import ValidationError
from django.utils import timezone

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.


# For admin to book costumer
class Customer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, default="")
    booking_date = models.DateField()
    booking_time = models.TimeField()
    number_of_people = models.IntegerField(default=0)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


# news img path
def news_image_path(instance, filename):
    ext = filename.split('.')[-1]  # Get the file extension
    filename = f"{instance.title.replace(' ', '_')}_image.{ext}"

    logger = logging.getLogger(__name__)
    logger.info(f"Instance title: {instance.title}")
    logger.info(f"Generated filename: {filename}")

    return os.path.join('news_images', filename)


# For admin to post News
class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to=news_image_path)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "news"

    def __str__(self):
        return self.title