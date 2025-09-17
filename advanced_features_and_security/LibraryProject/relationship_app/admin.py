from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import ExtUser
from .forms import CustomUserCreationForm, CustomUserChangeForm



class CustomUserAdmin(UserAdmin):
    add_form=CustomUserCreationFormm
    form=CustomUserChangeForm
    model=ExtUser

    list_display=('date_of_birth','profile_photo')
    list_filter=('date_of_birth','profile_photo')

admin.site.register(ExtUser,CustomUserAdmin)
# Register your models here.
