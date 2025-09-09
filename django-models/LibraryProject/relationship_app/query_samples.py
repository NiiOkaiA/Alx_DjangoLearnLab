author_query= Book.objects.filter(author='me')

library_books=Library.objects.get(name='katyk',books.all())

librarian=Librarian.objects.all()
