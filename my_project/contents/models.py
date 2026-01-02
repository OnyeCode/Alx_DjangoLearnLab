from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class Module(models.Model):
    subject = models.ForeignKey(Subject, related_name='modules', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Lesson(models.Model):
    module = models.ForeignKey(Module, related_name='lessons', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title

class PracticeQuestion(models.Model):
    lesson = models.ForeignKey(Lesson, related_name='questions', on_delete=models.CASCADE)
    question = models.TextField()
    correct_answer = models.TextField()

    def __str__(self):
        return self.question[:50]

class PracticeSubmission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(PracticeQuestion, on_delete=models.CASCADE)
    answer = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

class Progress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

