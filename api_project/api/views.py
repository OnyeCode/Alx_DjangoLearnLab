from django.shortcuts import render

# Create your views here.

from .models import Book
from rest_framework import generics
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
