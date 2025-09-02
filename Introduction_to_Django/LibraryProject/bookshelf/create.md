book=Book(title="1984", author="George Orwell", publication_year=1949)
book.save()
Book.objects.all()




#this is the document for retrieving the book instance 
 
 the result was <QuerySet [<Book: Book object (1)>]> . Apparently, I had to use self.title to ensure that i saw the text