from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Book

from django.views.generic.detail import DetailView
from .models import Library

def list_books(request):
    books = Book.objects.all()
    output = ""

    for book in books:
        output += f"{book.title} by {book.author.name}\n"

    return HttpResponse(output, content_type="text/plain")


class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"
    context_object_name = "library"

