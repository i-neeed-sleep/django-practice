from rest_framework import serializers
from models import Question

class McqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['question', 'choices', 'answer']