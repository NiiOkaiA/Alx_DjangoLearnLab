from django.db.models.signals import post_save
from django.dispatch import reciever
from django.contrib.auth import get_user_model
from .models import UserProfile


User=get_user_model()

@reciever (post_save, sender=User)
def create_UserProfile(sender, instance,created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
