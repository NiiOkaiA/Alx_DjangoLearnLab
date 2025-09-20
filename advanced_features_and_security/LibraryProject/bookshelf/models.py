from django.db import models
from django.contrib.auth.models import User,AbstractUser
from django.contrib.auth.base_user import BaseUserManager

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=100)
    publication_year=models.IntegerField()

class Author(models.Model):
    name=models.CharField(max_length=100)

'''class CustomUser(AbstractUser):
    date_of_birth=models.DateField()
    profile_photo=models.ImageField()

    objects=CustomUserManager()
'''


class CustomUserManager(BaseUserManager):
    def create_user(self,date_of_birth,profile_photo):        
         user=self.model(date_of_birth=date_of_birth,
                    profile_photo=profile_photo)
         user.set_password('rama')
         user.save(using=self._db)
         return user

    def create_superuser(self,date_of_birth,profile_photo):
         return self.create_user(date_of_birth,profile_photo)



class CustomUser(AbstractUser):
    date_of_birth=models.DateField()
    profile_photo=models.ImageField()
    
    objects=CustomUserManager()


class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.ForeignKey(Author, on_delete=models.CASCADE,related_name='books')
    book_list=Book.objects.all()
    
    class Meta:
        permissions=[
            ("can_create",  "can_create"),
            ("can_view","can_view"),
            ("can_delete","can_delete"),
            ("can_edit", "can_edit")
            ]
