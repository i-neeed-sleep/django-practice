import os
from rest_framework import generics 
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer

class GetUserView:
    serializer_class = UserSerializer

    def get(self, request):
        try:
            user = User.objects.get(id=request.user.name)
            return Response(UserSerializer(user).data, status=200)
        except User.DoesNotExist:
            return Response({"error": "User not found."}, status=404)