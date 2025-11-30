from django.shortcuts import render

# Create your views here.

from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


"""
List all books.
Accessible to everyone (authenticated or not).
Uses DRF GenericAPIView + ListAPIView.
"""
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Read-only access


"""
Retrieve a single book by ID.
Accessible to everyone.
"""
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = "pk"


"""
Create a new book instance.
Restricted to authenticated users only.
Includes validation provided by the serializer.
"""
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Must be logged in

    # Optional: custom behavior example
    def perform_create(self, serializer):
        # You can add extra processing here (logging, assigning user, etc.)
        serializer.save()


"""
Update an existing book instance.
Restricted to authenticated users only.
"""
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "pk"

    # Customize update behavior
    def perform_update(self, serializer):
        serializer.save()


"""
Delete a book instance.
Restricted to authenticated users only.
"""
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "pk"

