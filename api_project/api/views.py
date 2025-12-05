from django.shortcuts import render

# Create your views here.

from .models import Book
from rest_framework import generics, viewsets, permissions
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated] #To ensure that a user must be authenticated before they can access this view.

