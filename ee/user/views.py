from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import User
from .serializers import UserSerializer
from .permissions import IsSelf, IsAdmin

class GetUserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_permissions(self):
        if self.action in ['create', 'update']:
            permission_classes = [AllowAny]
        elif self.action == 'destroy':
            permission_classes = [IsSelf | IsAdmin]
        else:
            permission_classes = [IsAdmin]

        return [permission() for permission in permission_classes()]
