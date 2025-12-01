book = Book.objects.get(title = '1984')
book.title = 'Nineteen Eighty-Four'
book.save()
book.title 'Nineteen Eighty-Four'
Book.objects.get(id = 1) #<Book: Nineteen Eighty-Four>
