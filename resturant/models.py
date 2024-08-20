from django.db import models
from django.contrib.auth.models import User
import os
import logging

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="blog_posts"
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"
class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"


class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email =models.CharField(max_length=200, default="")
    booking_date = models.DateField()
    booking_time = models.TimeField()
    number_of_people = models.IntegerField(default=0)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

def news_image_path(instance, filename):
    # Generate a unique filename based on the post's title
    ext = filename.split('.')[-1]  # Get the file extension
    filename = f"{instance.title.replace(' ', '_')}_image.{ext}"
    return os.path.join('resturant/static/images/news_images', filename)

    logger = logging.getLogger(__name__)
    logger.info(f"Instance title: {instance.title}")
    logger.info(f"Generated filename: {filename}")

    return os.path.join('resturant/static/images/news_images', filename)

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

