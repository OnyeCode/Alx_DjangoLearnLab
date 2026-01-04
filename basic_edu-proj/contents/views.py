from rest_framework import viewsets, generics, views
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



from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def subjects_page(request):
    return render(request, "contents/subjects.html")


class SubjectListView(views.APIView):
    def get(self, request):
        subjects = Subject.objects.all()
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data)

class PracticeListView(views.APIView):
    def get(self, request):
        module_id = request.query_params.get("module_id")
        questions = PracticeQuestion.objects.filter(module_id=module_id)
        serializer = PracticeQuestionSerializer(questions, many=True)
        return Response(serializer.data)

class SubmitPracticeView(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        PracticeSubmission.objects.create(
            student=request.user,
            data=request.data
        )
        return Response({"message": "Submitted"})


