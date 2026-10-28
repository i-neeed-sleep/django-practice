from rest_framework import status, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .models import Question, QuestionInstance
from .serializers import QuestionSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    permission_classes = [IsAuthenticated]    

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        question = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)   

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.quiz.exists():
            return Response({"error": "Cannot delete question with associated question instances."}, status=status.HTTP_400_BAD_REQUEST)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


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
