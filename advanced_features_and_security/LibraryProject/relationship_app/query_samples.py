Book.objects.filter(author=author)
Author.objects.get(name=author_name)
Library.objects.get(name=library_name).books.all()
Librarian.objects.get(library=library).name
