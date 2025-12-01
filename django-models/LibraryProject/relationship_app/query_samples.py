#Query all books by a specific author.
Book.objects.filter(author=author_name)


#List all books in a library.
Library.objects.get(name=library_name).books.all()


#Retrieve the librarian for a library.
Librarian.objects.get(library=library_name).name
