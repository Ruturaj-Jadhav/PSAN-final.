from re import T
from tkinter import CASCADE
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

# Create
#  your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=255, default='coding')
    snippet = models.CharField(max_length=255,)
    body = RichTextField(blank= True, null= True)
    post_date = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name=("blog_posts"))

    def total_likes(self):
        return self.likes.count()

    def __str__(self):

        return self.title + '/' + str(self.author)
    def get_absolute_url(self):
    
        return reverse("article-detail", args=(str(self.id)))

class Contactus(models.Model):
    name =models.CharField(max_length=122)
    email =models.CharField(max_length=122)
    domain =models.CharField(max_length=122)
    messege =models.TextField()
    date =models.DateField()

    def __str__(self):
        return self.name


class Contactuss(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    message = models.TextField()

    def __str__(self):
        return self.name
    
 
        
        
        
        
class Category(models.Model):

    name = models.CharField(max_length=255, default='coding')

    def __str__(self):

        return self.name

    def get_absolute_url(self):
        return reverse("blogs")


class Profile(models.Model):
    user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio=models.TextField()
    profile_pic=models.ImageField(blank= True, null= True,upload_to="static/profile/")
    linkedin_url = models.CharField(max_length=255,blank= True, null= True)
    twitter_url = models.CharField(max_length=255,blank= True, null= True)
    instagram_url = models.CharField(max_length=255,blank= True, null= True)


    def __str__(self):
        return str(self.user)
