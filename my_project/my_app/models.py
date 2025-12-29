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


#Subject
class Subject(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

#Module
class Module(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="modules")
    title = models.CharField(max_length=255)
    description = models.TextField()
    order = models.PositiveIntegerField()


#Enrollment
class Enrollment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ])
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'subject')


#Lesson
class Lesson(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name="lessons")
    title = models.CharField(max_length=255)
    content = models.TextField()
    order = models.PositiveIntegerField()

#Practice
class Practice(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="practices")
    title = models.CharField(max_length=255)
    instructions = models.TextField()
    practice_type = models.CharField(max_length=20, choices=[
        ('quiz', 'Quiz'),
        ('code', 'Code'),
        ('text', 'Text')
    ])
    max_score = models.IntegerField()


"""
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()

'''
