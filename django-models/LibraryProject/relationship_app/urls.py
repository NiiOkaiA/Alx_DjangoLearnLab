from django.urls import path, include
from .views import list_books,LibraryDetailView
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns= [ path(' ', list_books, name='book_list'),
               path(' ',LibraryDetailView.as_view(), name='LibraryDetailView'),
               path('accounts/', include('django.contrib.auth.urls')),
               path('login/',LoginView.as_view(template_name='login.html')),
               path('logout/',LogoutView.as_view(template_name='logout.html')),
              #      ,name= 'logout'),
               path('admin_view/',admin_view, name='ad_view')
              ]


# views.register
