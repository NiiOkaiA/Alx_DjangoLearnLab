from django.shortcuts import render
from .forms import CustomUser
from rest_framework import generics
from .models import Post

# Create your views here.
def register(request):
    form=CustomUser()
    return render(request, 'blog/base.html',{"form":form})

def home(request):
    return render(request, 'blog/base.html')

class post(generics.CreateAPIView):
    queryset=Post.objects.all()
    
