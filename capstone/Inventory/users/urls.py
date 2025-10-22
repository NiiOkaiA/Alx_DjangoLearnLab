from django.urls import path
from .views import add_user,list_users,update_user,delete_user
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns=[
    path('users/new/',add_user.as_view(),name='newuser'),
    path('users/list/',list_users.as_view(),name='listusers'),
    path('users/<int:pk>/update/',update_user.as_view(),name='updateuser'),
    path('users/<int:pk>/delete/',delete_user.as_view(),name='deleteuser'),
    path('login/', obtain_auth_token, name='obtain_token'),
    
    ]
