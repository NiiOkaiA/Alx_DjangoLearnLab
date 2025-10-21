from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    bio=models.CharField(max_length=100)
    profile_picture=models.ImageField()
    followers=models.ManyToManyField('self',symmetrical=False,blank=True)



#from django.contrib.auth.views import LoginView,LogoutView

'''
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post

class CustomUser(forms.ModelForm):
    email=forms.EmailField(required=True)

    class Meta:
        model=Post
        fields=["title","content"]
'''
