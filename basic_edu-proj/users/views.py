from rest_framework import generics, permissions, views
from .serializers import RegisterSerializer, StudentProfileSerializer
from django.contrib.auth.models import User
from .models import StudentProfile


class RegisterView(views.APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        StudentProfile.objects.create(user=user)

        return Response({"message": "Registered successfully"})


class StudentProfileView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        profile, _ = StudentProfile.objects.get_or_create(user=request.user)
        serializer = StudentProfileSerializer(profile)
        return Response(serializer.data)

    def put(self, request):
        profile, _ = StudentProfile.objects.get_or_create(user=request.user)
        serializer = StudentProfileSerializer(
            profile, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class StudentProfileListView(generics.ListAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer
    permission_classes = [permissions.IsAdminUser]



from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def login_page(request):
    return render(request, "auth/login.html")


def register_page(request):
    return render(request, "auth/register.html")


@login_required
def profile_page(request):
    return render(request, "users/profile.html")


