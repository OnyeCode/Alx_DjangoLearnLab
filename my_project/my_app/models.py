from django.db import models
from django.contrib.auth.models import AbstractUser

#User (Django’s default)
class User(AbstractUser):
    email = models.EmailField(unique=True)

"""
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()

'''
