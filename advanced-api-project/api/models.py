from django.db import models


#The Author model with 'name' fields, which is a string field to store the author’s name
class Author(models.Model):
    name = models.CharField(max_length=200)


#The Book model with title field: a string field for the book’s title; publication_year field: an integer field for the year the book was published; author field: a foreign key linking to the Author model, establishing a one-to-many relationship from Author to Books
class Book(models. Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
