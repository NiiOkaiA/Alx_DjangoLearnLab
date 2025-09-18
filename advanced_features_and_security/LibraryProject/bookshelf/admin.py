from django.contrib import admin
from .models import Book
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display=('title','author','publication_year')
    list_filter=['title','author']
    search_fields=('title','author')

admin.site.register(Book,BookAdmin)



class CustomUserAdmin(UserAdmin):
    add_form=CustomUserCreationFormm
    form=CustomUserChangeForm
    model=ExtUser

    list_display=('date_of_birth','profile_photo')
    list_filter=('date_of_birth','profile_photo')

admin.site.register(CustomUser, CustomUserAdmin)
