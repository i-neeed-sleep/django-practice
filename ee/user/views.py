from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer

class GetUserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({'user_id': user.id}, status=201)

    def list(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        self.perform_destroy(user)
        return Response(
            {"message": "Item deleted successfully"}, 
            status=status.HTTP_200_OK
        )