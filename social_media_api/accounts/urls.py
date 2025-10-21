from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView






url_patterns=["login/",LoginView.as_view(template_name='accounts/login.html'),name="login"),
              path("register/",register,name="register"),

path

    


    ]
