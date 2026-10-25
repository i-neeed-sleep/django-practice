from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import QuestionViewSet, QuestionInstanceViewSet

router = DefaultRouter()
router.register(r'questions', QuestionViewSet, basename='question')
router.register(r'question-instances', QuestionInstanceViewSet, basename='question-instance')

urlpatterns = [
    path('', include(router.urls)),
]