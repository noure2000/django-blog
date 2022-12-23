from django.db import models

# Import User Model :
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User=get_user_model()

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    boi = models.TextField(max_length = 200,blank=True)
    location='Maroc'
    # location = models.CharField(max_length = 50,blank=True)
    birth_date = models.DateField(null=True,blank=True)


class Post(models.Model):
    author = models.ForeignKey(Profile,on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)