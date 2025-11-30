from rest_framework import serializers
from datetime import date
from .models import Author, Book


"""
BookSerializer:
- Serializes all fields from the Book model.
- Includes validation to ensure publication year is not in the future.
"""
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

    # Custom validation: publication_year must not be in the future
    def validate_publication_year(self, value):
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


"""
AuthorSerializer:
- Serializes the Author model.
- Nests BookSerializer to show related books.
- The 'books' field uses the reverse relation (related_name='books').
"""
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']

