from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('eeee.urls')),
    path('admin/', admin.site.urls),
]
