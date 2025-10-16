from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm



class CustomUserAdmin(UserAdmin):
    add_form=CustomUserCreationForm
    form=CustomUserChangeForm
    model=CustomUser

    list_display=('date_of_birth','profile_photo')
    list_filter=('date_of_birth','profile_photo')

admin.site.register(CustomUser,CustomUserAdmin)
# Register your models here.
