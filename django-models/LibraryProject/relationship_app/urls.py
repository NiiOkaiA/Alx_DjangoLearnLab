from django.urls import path
from .views import list_books,LibraryDetailView

urlpatterns= [ path(' ', book_list, name='book_list'),
               path(' ',Libraryview.as_view(), name='LibraryDetailView'),

              ]
