from django.urls import path
from .views import RegisterView, StudentProfileView, StudentProfileListView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('profile/', StudentProfileView.as_view(), name='student-profile'),
    path('profiles/', StudentProfileListView.as_view(), name='student-profiles'),
]


from django.urls import path
from .views import (
    login_page,
    register_page,
    profile_page,
)

urlpatterns = [
    path("login/", login_page, name="login"),
    path("register/", register_page, name="register"),
    path("profile/", profile_page, name="profile"),
]

