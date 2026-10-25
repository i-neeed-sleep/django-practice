from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import QuizViewSet, QuizInstanceViewSet

router = DefaultRouter()
router.register(r'quizzes', QuizViewSet, basename='quiz')
router.register(r'quiz-instances', QuizInstanceViewSet, basename='quiz-instance')

urlpatterns = [
    path('', include(router.urls)),
]