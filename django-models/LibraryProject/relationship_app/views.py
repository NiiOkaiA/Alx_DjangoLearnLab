from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Book
from .models import Library, UserProfile
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.decorators import user_passes_test,login_required
from django.db.models.signals import post_save


# Create your views here.

def list_books(request):
    books=Book.objects.all()
    context = {'book_list':books}
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    model= Library
    template_name= 'relationship_app/library_detail.html'

   # def get_context_data(self, **kwargs):
   # context= super.get_context_data(**kwargs)


class Signup(CreateView):
    form_class =UserCreationForm()
    success_url= reverse_lazy('login')
    template_name= 'relationship_app/register.html'

'''
@login_required
@user_passes_test(lambda u: u.role=='Admin')
def admin_view(request):
    report=UserProfile.objects.all()
    return render(request, 'admin_view.html')


#    report=UserProfile.objects.all()
#    return render(request, 'admin_view.html',{'reports':reports})
'''

def is_admin(user):
    return user.is_authenticated and hasattr(user,"userprofile") and user.userprofile.role=='Admin'

@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

#@login_required         
@user_passes_test(lambda u: u.role=='Librarian')
def librarian_view(request):
         pass
'''
@receiver (post_save, sender=User)
def create_UserProfile(sender, instance,created, **kwargs):
    if created:
       UserProfile.objects.create(user=instance)

'''
