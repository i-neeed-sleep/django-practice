from rest_framework import serializers
from .models import Question, QuestionInstance

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'type', 'question', 'choices', 'answer']

    def validate(self, data):
        question_type = data.get('type')
        choices = data.get('choices')
        answer = data.get('answer')
        if question_type == 'm' and not choices:
            raise serializers.ValidationError("Choices are required for multiple choice questions.")
        elif question_type == 's' and choices:
            raise serializers.ValidationError("Choices should not be provided for short answer questions.")
        if question_type == 'm':
            if len(answer)!=1:
                raise serializers.ValidationError("MCQs should have letter or number answer")
            answer = answer.upper()
        return data

class QuestionInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionInstance
        fields = ['question','quiz_instance', 'response']

    def validate(self, data):
        question = data.get('question')
        response = data.get('response')
        if question and response:
            if question.type == 'm':
                if len(response) >1:
                    raise serializers.ValidationError({"Multiple choice response must be a single letter"})
            response = response.upper()
        return data