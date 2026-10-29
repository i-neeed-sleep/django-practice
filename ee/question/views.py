from rest_framework import status, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .models import Question, QuestionInstance
from .serializers import QuestionSerializer
from user.permissions import IsAdmin, IsTeacher

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get_permissions(self):
        if self.action == 'destroy':
            permission_classes = [IsAdmin]
        elif self.action == 'update':
            permission_classes = [IsAdmin | IsTeacher]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]


class QuestionInstanceViewSet(viewsets.ModelViewSet):
    queryset = QuestionInstance.objects.all()
    serializer_class = QuestionSerializer

    permission_classes = [AllowAny]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.quiz_instance.submitted:
            return Response(
                "Cannot update question instance that has been submitted.",
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        return Response(QuestionInstanceSerializer(instance).data, status=status.HTTP_200_OK)
