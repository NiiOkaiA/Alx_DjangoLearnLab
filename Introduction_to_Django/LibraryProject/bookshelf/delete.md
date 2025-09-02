book=Book.objects.get(id=1) 
book.delete() 

'''(1, {'bookshelf.Book': 1})
>>> Book.objects.all()
<QuerySet []>'''

#this shows there is no longer any output in books