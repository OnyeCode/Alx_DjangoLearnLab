from rest_framework import serializers
from django.contrib.auth.models import User

from .models import (
    StudentProfile,
    Subject,
    Module,
    Enrollment,
    PracticeQuestion,
    PracticeSubmission,
    Progress
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]

class StudentProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = StudentProfile
        fields = [
            "id",
            "user",
            "first_name",
            "last_name",
            "bio",
            "profile_picture",
            "date_of_birth",
            "created_at",
        ]

class SubjectSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Subject
        fields = [
            "id",
            "title",
            "description",
            "created_by",
            "created_at",
        ]

class ModuleSerializer(serializers.ModelSerializer):
    subject = serializers.StringRelatedField()

    class Meta:
        model = Module
        fields = [
            "id",
            "subject",
            "title",
            "description",
            "order",
            "created_at",
        ]

class EnrollmentSerializer(serializers.ModelSerializer):
    student = serializers.StringRelatedField()
    subject = serializers.StringRelatedField()

    class Meta:
        model = Enrollment
        fields = [
            "id",
            "student",
            "subject",
            "enrolled_at",
            "status",
        ]

class PracticeQuestionSerializer(serializers.ModelSerializer):
    module = serializers.StringRelatedField()

    class Meta:
        model = PracticeQuestion
        fields = [
            "id",
            "module",
            "question_text",
            "question_type",
            "created_at",
        ]

class PracticeSubmissionSerializer(serializers.ModelSerializer):
    student = serializers.StringRelatedField(read_only=True)
    question = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = PracticeSubmission
        fields = [
            "id",
            "student",
            "question",
            "submitted_answer",
            "is_correct",
            "submitted_at",
        ]
        read_only_fields = ["is_correct"]

class ProgressSerializer(serializers.ModelSerializer):
    student = serializers.StringRelatedField()
    module = serializers.StringRelatedField()

    class Meta:
        model = Progress
        fields = [
            "id",
            "student",
            "module",
            "completed",
            "completed_at",
        ]


