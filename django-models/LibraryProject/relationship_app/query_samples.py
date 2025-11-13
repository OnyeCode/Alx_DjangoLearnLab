Book.objects.filter(author=author)
Library.objects.get(name=library_name).books.all()
Librarian.objects.get(Library = '').name
