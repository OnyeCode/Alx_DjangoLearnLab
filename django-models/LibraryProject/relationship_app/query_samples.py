#Query all books by a specific author.
Book.objects.filter(author=Author_name)


#List all books in a library.
Library.objects.get(name=Library_name).books


#Retrieve the librarian for a library.
Librarian.objects.get(library=library_name).name
