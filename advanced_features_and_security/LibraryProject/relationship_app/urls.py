from django.urls import path, include
from .views import list_books,LibraryDetailView,admin_view,Register,can_add_book,can_delete_book,can_change_book
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns= [ path(' ', list_books, name='book_list'),
               path(' ',LibraryDetailView.as_view(), name='LibraryDetailView'),
              # path("admin_view/",admin_view, name='ad_view'),

               path('accounts/', include('django.contrib.auth.urls')),
               path('login/',LoginView.as_view(template_name='relationship_app/login.html')),
               path('logout/',LogoutView.as_view(template_name='logout.html')),
               path('register/',Register.as_view(template_name='register.html'),name='register'), 
              #      ,name= 'logout'),
               path("admin_view/",admin_view, name='ad_view'),
               path("add_book/",can_add_book, name='add'),
               path ("delete_book/",can_delete_book,name='del'),
               path ("edit_book/",can_change_book,name='change'),              ]


# views.register
