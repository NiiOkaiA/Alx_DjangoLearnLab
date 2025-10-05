from django.shortcuts import render
from .models import Book
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework
from rest_framework import filters
from rest_framework import status
from rest_framework import status, response.data
#response.data
#from rest_framework.permissions import IsAuthenticatedOrReadOnly
#from rest_framework.permissions import 


# Create your views here.

class ListView(generics.ListAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    filter_backends = [filters.OrderingFilter]
    filter_backends = [filters.SearchFilter]
    search_fields=['title','publication_year','author']


class DetailView(generics.RetrieveAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer

class CreateView(generics.CreateAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer


class UpdateView(generics.UpdateAPIView):
    queryset=Books.objects.all()
    serializer_class=BookSerializer

class DeleteView(generics.DestroyAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
