

Book.objects.get(title="1984")
<QuerySet [<Book: Book object (1)>]>


#successful creation. Apparently, I had to use self. title to ensure that text is created.