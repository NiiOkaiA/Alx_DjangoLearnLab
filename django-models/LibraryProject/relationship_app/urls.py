from django.urls import path
from .views import book_list,Libraryview

urlpatterns= [ path(' ', book_list, name='book_list'),
               path(' ',Libraryview.as_view(), name='Libraryview'),

              ]
