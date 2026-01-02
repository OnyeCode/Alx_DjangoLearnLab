from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *

class SubjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class ModuleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer


class LessonViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class PracticeQuestionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PracticeQuestion.objects.all()
    serializer_class = PracticeQuestionSerializer


class PracticeSubmissionViewSet(viewsets.ModelViewSet):
    queryset = PracticeSubmission.objects.all()
    serializer_class = PracticeSubmissionSerializer

    def get_queryset(self):
        return PracticeSubmission.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ProgressViewSet(viewsets.ModelViewSet):
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer

    def get_queryset(self):
        return Progress.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

