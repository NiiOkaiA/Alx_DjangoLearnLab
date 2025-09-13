from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Book
from .models import Library, UserProfile
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.decorators import user_passes_test



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
@user_passes_test(lambda u: u.role=='Admin')
def admin_view(request):
    report=UserProfile.objects.all()
    return render(request, 'admin_view.html',{'reports':reports})
'''

def is_admin(user):
    return user.is_staff

@user_passes_test(is_admin)
def admin_view(request):
    report=UserProfile.objects.all()
    return render(request, 'admin_view.html',{'reports':reports})
         
         
@user_passes_test(lambda u: u.role=='Librarian')
def librarian_view(request):
         pass

