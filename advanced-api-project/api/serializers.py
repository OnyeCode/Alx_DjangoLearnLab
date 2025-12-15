from rest_framework import serializers
from .models import Author, Book
from datetime import date

#BookSerializer that serializes all fields of the Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

    #Custom validation to the BookSerializer to ensure the publication_year is not in the future
    def validate(self, data):
        if data['pubication_year'] > date.year():
            raise serializers.ValidationError("Publication year cannot be in the future")
        return data

#AuthorSerializer that serializers the 'name' field of the Author model, and also serializers the related books through nested serialization
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True) #nested BookSerializer to serialize the related books dynamically

    class Meta:
        model = Author
        fields = ['name', 'books']

