from django.urls import path
from .models import ListView


url_patterns=[
    '/books/',ListView.as_view(),
    'books/create/',CreateView.as_view(),
    'books/delete/',DeleteView.as_view(),
    'books/update/',UpdateView.as_view(),
    'books/detail/',DetailView.as_view(),
    
               


    ]
