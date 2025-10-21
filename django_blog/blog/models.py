from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone




# Create your models here.
class  Post(models.Model):
    post_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200,unique=True)
    content=models.TextField()
    published_date=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
