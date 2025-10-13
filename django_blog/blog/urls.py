from django.urls import path
from .views import register,home,post,profileup
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns=[
    path('',home,name="home"),
    path("posts/",post.as_view(),name="posts"),
    path("register/",register,name="register"),
    path("login/",LoginView.as_view(template_name='blog/login.html'),name="login"),
    path("profile/",profileup.as_view(),name="profileupdate")
    ]
