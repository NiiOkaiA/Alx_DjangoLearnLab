from django.urls import path
from .views import add_user,list_users,update_user,delete_user


urlpatterns=[
    path('users/new/',add_user.as_view(),name='newuser'),
    path('users/list/',list_users.as_view(),name='listusers'),
    path('users/update/',update_user.as_view(),name='updateuser'),
    path('users/delete/',delete_user.as_view(),name='deleteuser'),
    ]
