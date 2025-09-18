from django.shortcuts import render
from django.contrib.auth.models import Group,Permission
from django.contrib.contenttypes.models import ContentType
from .models import Book
from django.contrib.auth.decorators import permission_required
# Create your views here.

Editors,created=Group.objects.get_or_create(name='Editors')
Viewers,created=Group.objects.get_or_create(name='Viewers')
Admins,created=Group.objects.get_or_create(name='Admins')



Contenttype=ContentType.objects.get_for_model(Book)
edit_perm=Permission.objects.get(codename='can _edit', content_type=content_type)
view_perm=Permission.objects.get(codename='can _view', content_type=content_type)
create_perm=Permission.objects.get(codename='can _create', content_type=content_type)
delete_perm=Permission.objects.get(codename='can _delete', content_type=content_type)


Editors.permissions.add(edit_perm)
Viewers.permissions.add(view_perm)
Admin.permissions.add(create_perm,delete_perm)


@permission_required('bookshelf.can_edit',raise_exception=True)
def can_edit_book(request):
    return Book.objects.update()

@permission_required('bookshelf.can_view',raise_exception=True)
def can_view_book(request):
    return Book.book_list
