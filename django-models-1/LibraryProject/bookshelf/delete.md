from bookshelf.models import Book
book = Book.objects.get(title = 'Nineteen Eighty-Four')
book.delete() #(1, {'bookshelf.Book': 1})
Book.objects.filter(title = 'Nineteen Eighty-Four') #<QuerySet []>
Book.objects.get(title = 'Nineteen Eighty-Four') #bookshelf.models.Book.DoesNotExist: Book matching query does not exist.
