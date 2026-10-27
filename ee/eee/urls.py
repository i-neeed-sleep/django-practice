from django.urls import include, path
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api/login/', obtain_auth_token, name='api_token_auth'),
    path('', include("question.urls")),
    path('', include("quiz.urls")),
    path('', include("user.urls")),
    path('admin/', admin.site.urls)
]
