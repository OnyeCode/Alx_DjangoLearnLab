from django.shortcuts import render

# Create your views here.

#function-based view that lists all books stored in the database.
#This view should render a simple text list of book titles and their authors.

from .models import Book

def list_books(request):
	context = {'books' : Book.objects.all()}
	return render(request, 'relationship_app/list_books.html', context)


#class-based view that displays details for a specific library, listing all books available in that library.
#Utilize Django’s ListView or DetailView to structure this class-based view.

from django.views.generic.detail import DetailView
from .models import Library

class LibraryDetailView(DetailView):
	model = Library
	template_name = 'relationship_app/library_detail.html'
	context_object_name = 'library'

from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class RegisterView(CreateView):
	form_class = UserCreationForm
	template_name = 'relationship_app/register.html'
	success_url = reverse_lazy('login')
