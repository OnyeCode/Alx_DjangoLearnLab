from django.db import models
from django.contrib.auth.models import User

#StudentProfile
class StudentProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="student_profile"
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(
        upload_to="profiles/",
        blank=True,
        null=True
    )
    date_of_birth = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

#Subject
class Subject(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="subjects"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

#Module
class Module(models.Model):
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name="modules"
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    order = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.subject.title} - {self.title}"

#Enrollment (Many-to-Many Resolver)
class Enrollment(models.Model):
    student = models.ForeignKey(
        StudentProfile,
        on_delete=models.CASCADE,
        related_name="enrollments"
    )
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name="enrollments"
    )
    enrolled_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ("active", "Active"),
            ("completed", "Completed"),
            ("dropped", "Dropped"),
        ],
        default="active"
    )

    class Meta:
        unique_together = ("student", "subject")

    def __str__(self):
        return f"{self.student} enrolled in {self.subject}"

#PracticeQuestion
class PracticeQuestion(models.Model):
    QUESTION_TYPES = [
        ("mcq", "Multiple Choice"),
        ("text", "Text"),
    ]

    module = models.ForeignKey(
        Module,
        on_delete=models.CASCADE,
        related_name="questions"
    )
    question_text = models.TextField()
    question_type = models.CharField(
        max_length=10,
        choices=QUESTION_TYPES
    )
    correct_answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Question in {self.module.title}"

#PracticeSubmission
class PracticeSubmission(models.Model):
    student = models.ForeignKey(
        StudentProfile,
        on_delete=models.CASCADE,
        related_name="submissions"
    )
    question = models.ForeignKey(
        PracticeQuestion,
        on_delete=models.CASCADE,
        related_name="submissions"
    )
    submitted_answer = models.TextField()
    is_correct = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Submission by {self.student}"

#Progress
class Progress(models.Model):
    student = models.ForeignKey(
        StudentProfile,
        on_delete=models.CASCADE,
        related_name="progress"
    )
    module = models.ForeignKey(
        Module,
        on_delete=models.CASCADE,
        related_name="progress"
    )
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        unique_together = ("student", "module")

    def __str__(self):
        return f"{self.student} - {self.module}"

