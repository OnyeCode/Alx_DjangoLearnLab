from bookshelf.models import Book
book = Book.objects.create(title = '1984', author = 'George Orwell', publication_year = 1949)
book.id #1

Book.objects.get(1d=1) #<QuerySet [<Book: 1984>]>

book = Book.objects.get(title = '1984')
book.title = 'Nineteen Eighty-Four'
book.save()
book.title 'Nineteen Eighty-Four'
Book.objects.get(id = 1) #<Book: Nineteen Eighty-Four>

book = Book.objects.get(title = 'Nineteen Eighty-Four')
book.delete() #(1, {'bookshelf.Book': 1})
Book.objects.filter(title = 'Nineteen Eighty-Four') #<QuerySet []>
Book.objects.get(title = 'Nineteen Eighty-Four') #bookshelf.models.Book.DoesNotExist: Book matching query does not exist.
