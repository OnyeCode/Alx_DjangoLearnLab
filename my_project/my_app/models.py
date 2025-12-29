from django.db import models
from django.contrib.auth.models import AbstractUser

#User (Django’s default)
class User(AbstractUser):
    email = models.EmailField(unique=True)

#StudentProfile
class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=20)
    country = models.CharField(max_length=50)
    education_level = models.CharField(max_length=50)



"""
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()

'''
