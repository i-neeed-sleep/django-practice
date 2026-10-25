from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Quiz, QuizInstance
from .serializers import QuizSerializer, QuizInstanceSerializer
from question.models import Question, QuestionInstance
from user.models import User

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        quiz = serializer.save(teacher=request.user)
        return Response(QuizSerializer(quiz).data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        quiz = self.get_object()
        if new_questions := request.data.get("questions"):
            current_ids = set(quiz.questions.values_list("id", flat=True))
            new_ids = set(new_questions)
            to_add = new_ids - current_ids
            to_remove = current_ids - new_ids
            if to_add:
                quiz.questions.add(*to_add)
                quiz_instances = quiz.quiz_instances.all()

                new_question_instances = [
                    QuestionInstance(
                        quiz_instance=quiz_instance,
                        question_id=question_id,
                    )
                    for quiz_instance in quiz_instances
                    for question_id in to_add
                ]

                QuestionInstance.objects.bulk_create(new_question_instances)
            if to_remove:
                quiz.questions.remove(*to_remove)
                QuestionInstance.objects.filter(
                    quiz_instance__quiz=quiz,
                    question_id__in=to_remove,
                ).delete()
        
        serializer = self.get_serializer(quiz, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        quiz = serializer.save()
        return Response(QuizSerializer(quiz).data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        quiz = self.get_object()
        self.perform_destroy(quiz)
        return Response(status=status.HTTP_204_NO_CONTENT)

class QuizInstanceViewSet(viewsets.ModelViewSet):
    queryset = QuizInstance.objects.all()
    serializer_class = QuizInstanceSerializer

    def submit_quiz(self, request, pk=None):
        quiz_instance = self.get_object()
        if quiz_instance.submitted:
            return Response({"error": "Quiz has already been submitted."}, status=status.HTTP_400_BAD_REQUEST)
        quiz_instance.submitted = True
        quiz_instance.save()
        return Response({"message": "Quiz submitted successfully."}, status=status.HTTP_200_OK)