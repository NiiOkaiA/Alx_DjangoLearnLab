from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
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

@login_required    
def profileup(request):
    if request.method=='POST':
        if form.is_valid():
            form.save()
            return redirect('posts')
   # queryset=Post.objects.all()
