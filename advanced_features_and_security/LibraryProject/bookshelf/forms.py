from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class ExampleForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields=('date_of_birth','profile_photo')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model=CustomUser
        fields=('date_of_birth','profile_photo')
'''    
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields=('date_of_birth','profile_photo')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model=CustomUser
        fields=('date_of_birth','profile_photo')
'''
