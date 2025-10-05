from django.shortcuts import render
from .models import Book
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class ListView(generics.ListAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer


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
