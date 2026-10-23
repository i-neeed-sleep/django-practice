from rest_framework import serializers
from .models import Question

class McqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['type', 'question', 'choices', 'answer']

    def validate(self, data):
        question_type = data.get('type')
        choices = data.get('choices')
        if question_type == 'm' and not choices:
            raise serializers.ValidationError("Choices are required for multiple choice questions.")
        elif question_type == 's' and choices:
            raise serializers.ValidationError("Choices should not be provided for short answer questions.")
        return data