from django.shortcuts import render

# Create your views here.

#function-based view that lists all books stored in the database.
#This view should render a simple text list of book titles and their authors.

from .models import Book, Library

def list_books(request):
	context = {'books' : Book}
	return render(request, 'relationship_app/list_books.html', context)


#class-based view that displays details for a specific library, listing all books available in that library.
#Utilize Django’s ListView or DetailView to structure this class-based view.

from django.views.generic import DetailView

class library_detail(DetailView):
	model = Library
	template_name = 'relationship_app/library_detail.html'
	context_object_name = 'library'
