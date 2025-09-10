from django.urls import path
from .views import list_books,LibraryDetailView

urlpatterns= [ path(' ', list_books, name='book_list'),
               path(' ',LibraryDetailView.as_view(), name='LibraryDetailView'),
              ]
