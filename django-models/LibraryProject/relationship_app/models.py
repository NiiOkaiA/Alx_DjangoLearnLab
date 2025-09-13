from django.db import models
from django.contrib.auth.models import User


# Create your models here.

ROLE_CHOICES  =[
    ('Admin','Admin'),
    ('Librarian','Librarian'),
    ('Member','Member')
    ]






class Author(models.Model):    
    name=models.CharField(max_length=100)
    #return self.name

class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.ForeignKey(Author, on_delete=models.CASCADE,related_name='books')

class Library(models.Model):
    name=models.CharField(max_length=100)
    books=models.ManyToManyField(Book, related_name='library')

class Librarian(models.Model):
    name=models.CharField(max_length=100)
    library=models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarian')


class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    role=models.CharField(max_length=100,
                          choices=ROLE_CHOICES,
                          default='Member')

   # def __str__(self):
    #    return self.role

    
# Admin
# Member
