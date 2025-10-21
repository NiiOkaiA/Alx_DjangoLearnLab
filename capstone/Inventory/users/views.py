from django.shortcuts import render
from rest_framework import generics
from .models import CustomUser
from .serializers import UserSerializer,UserCreateSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from rest_framework.exceptions import NotFound


# Create your views here.


class add_user(generics.CreateAPIView):
    model=CustomUser
    serializer_class=UserCreateSerializer
    queryset=CustomUser.objects.all
    permission_classes=[AllowAny]
    authentication_classes=[]

class list_users(generics.ListAPIView):
    model=CustomUser
    serializer_class=UserSerializer
    queryset=CustomUser.objects.all()
    permission_classes=[IsAuthenticated]

class update_user(generics.UpdateAPIView):
    model=CustomUser
    serializer_class=UserSerializer
    queryset=CustomUser.objects.all()
    permission_classes=[IsAuthenticated]

    


class delete_user(generics.DestroyAPIView):
    model=CustomUser
    serializer_class=UserSerializer
    queryset=CustomUser.objects.all()
    permission_classes=[IsAuthenticated]

