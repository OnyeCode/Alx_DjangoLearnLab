from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('subjects', SubjectViewSet)
router.register('modules', ModuleViewSet)
router.register('lessons', LessonViewSet)
router.register('questions', PracticeQuestionViewSet)
router.register('submissions', PracticeSubmissionViewSet)
router.register('progress', ProgressViewSet)

urlpatterns = router.urls

