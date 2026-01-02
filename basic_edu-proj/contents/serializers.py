from rest_framework import serializers
from .models import *

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class PracticeQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PracticeQuestion
        fields = ['id', 'lesson', 'question']

class PracticeSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PracticeSubmission
        fields = '__all__'
        read_only_fields = ['user']

class ProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progress
        fields = '__all__'
        read_only_fields = ['user']

