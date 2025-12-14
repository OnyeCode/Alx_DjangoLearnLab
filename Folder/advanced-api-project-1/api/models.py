from django.db import models

# Create your models here.

from datetime import date

"""
Author model:
- Represents a writer.
- One author can have many books.
"""
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


"""
Book model:
- Represents a single book.
- Linked to an Author through a ForeignKey (One-To-Many relationship).
"""
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"

