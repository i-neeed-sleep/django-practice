from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import GetUserView

router = DefaultRouter()
router.register(r'users', GetUserView, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]