from django.urls import include, path
from rest_framework.routers import DefaultRouter

from question.urls import router as question_router
from quiz.urls import router as quiz_router
from user.urls import router as user_router

router = DefaultRouter()

router.registry.extend(question_router.registry)
router.registry.extend(quiz_router.registry)
router.registry.extend(user_router.registry)

urlpatterns = [
    path('', include(router.urls))
]
