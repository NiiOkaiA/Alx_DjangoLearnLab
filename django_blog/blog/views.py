from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUser
from rest_framework import generics
from .models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
#from django.views.generic.update import UpdateView
#from django.views.generic.delete import DeleteView


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


class listblogs(ListView):
    model=Post
    template_name='blog/listblogs.html'
    context_object_name='listblog'

class showblog(DetailView):
    model=Post
    template_name='blog/showblog.html'
    context_object_name='showblog'
    '''
    def get_queryset(self)
      return Post.objects.get(title=self.kwargs['title'])'''

class createblog(CreateView):
    model=Post
    fields=['title','body']
    template_name='blog/createblog.html'
    success_url='/posts/'
    
    #queryset=Post.objects.all()

class updateblog(UpdateView):
    model=Post
    template_name='blog/updateblog.html'
    success_url='/posts/'
    
   #queryset=post.objects.all()

class deleteblog(DeleteView):
    model=Post
    template_name='blog/deleteblog.html'
    success_url=reverse_lazy('posts')
    
    #queryset=post.objects.all()
    
'''

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from .models import Post
from .forms import PostForm  # Optional

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_create.html'
    success_url = '/posts/'

    def form_valid(self, form):
        form.instance.author = self.request.user  # Attach logged-in user
        return super().form_valid(form)'''
