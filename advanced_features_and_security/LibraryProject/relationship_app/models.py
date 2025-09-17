from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.base_user import BaseUserManager
# Create your models here.
'''
ROLE_CHOICES  =[
    ('Admin','Admin'),
    ('Librarian','Librarian'),
    ('Member','Member')
    ]
'''




class Author(models.Model):    
    name=models.CharField(max_length=100)
    #return self.name

class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.ForeignKey(Author, on_delete=models.CASCADE,related_name='books')

    class Meta:
        permissions=[
            ("can_add",  "can_add_book"),
            ("can_change","can_change_book"),
            ("can_delete","can_delete_book"),
            ]

class Library(models.Model):
    name=models.CharField(max_length=100)
    books=models.ManyToManyField(Book, related_name='library')

class Librarian(models.Model):
    name=models.CharField(max_length=100)
    library=models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarian')


class UserProfile(models.Model):
    ROLE_CHOICES  =[
    ('Admin','Admin'),
    ('Librarian','Librarian'),
    ('Member','Member')
    ]

    user=models.OneToOneField(User, on_delete=models.CASCADE)
    role=models.CharField(max_length=100,
                          choices=ROLE_CHOICES,
                          default='Member')


@receiver (post_save, sender=User)
def create_UserProfile(sender, instance,created, **kwargs):
    if created:
       UserProfile.objects.create(user=instance)




class CustomUser(AbstractUser):
    date_of_birth=models.DateField()
    profile_photo=models.ImageField()

    objects=CustomUserManager()


class CustomUserManager(BaseUserManager):
    def create_user(self,date_of_birth,profile_photo):        
         user=self.model(date_of_birth=date_of_birth,
                    profile_photo=profile_photo)
         user.set_password('rama')
         user.save(using=self._db)
         return user

    def create_superuser(self,date_of_birth,profile_photo):
         return self.create_user(date_of_birth,profile_photo)

   # objects=CustomUserManager()
       
   # def __str__(self):
    #    return self.role

    
# Admin
# Member
