from django.urls import path
from .views import register,home,post,profileup,createblog,updateblog,showblog,listblogs,deleteblog
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns=[
    path('',home,name="home"),
    path("posts/",post.as_view(),name="posts"),
    path("register/",register,name="register"),
    path("login/",LoginView.as_view(template_name='blog/login.html'),name="login"),
    path("profile/",profileup,name="profileupdate"),
    path("post/",listblogs.as_view(),name='listblog'),
    path('post/<int:pk>/',showblog.as_view(),name='showblog'),
    path('post/new/',createblog.as_view(),name='createblog'),
    path('post/<int:pk>/update/',updateblog.as_view(),name='updateblog'),
    path('post/<int:pk>/delete/',deleteblog.as_view(),name='deleteblog')
]
