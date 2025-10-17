from django.shortcuts import render
from rest_framework import generics
from .models import CustomUser
from .serializers import UserSerializer,UserCreateSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class add_user(generics.CreateAPIView):
    model=CustomUser
    serializer_class=UserCreateSerializer
    queryset=CustomUser.objects.all

class list_users(generics.ListAPIView):
    model=CustomUser
    serializer_class=UserSerializer
    queryset=CustomUser.objects.all()
    permission_classes=[IsAuthenticated]

class update_user(generics.UpdateAPIView):
    model=CustomUser
    serializer_class=UserSerializer
    queryset=CustomUser.objects.all
    permission_classes=[IsAuthenticated]

class delete_user(generics.DestroyAPIView):
    model=CustomUser
    serializer_class=UserSerializer
    queryset=CustomUser.objects.all
    permission_classes=[IsAuthenticated]

