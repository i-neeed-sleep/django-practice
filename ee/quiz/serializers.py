from rest_framework import serializers
from .models import Quiz, QuizInstance
from question.serializers import QuestionSerializer

class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = ['name', 'teacher', 'questions', 'students']
        read_only_fields = ['teacher']

    def create(self, validated_data):
        teacher = self.context['request'].user
        return Quiz.objects.create(
            name=validated_data['name'],
            teacher=teacher,
            questions=validated_data.get('questions', []),
            students=validated_data.get('students', [])
        )

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        if 'students' in validated_data:
            instance.students.set(validated_data['students'])
        if 'questions' in validated_data:
            instance.questions.set(validated_data['questions'])
        instance.save()
        return instance

class QuizInstanceSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = QuizInstance
        fields = ['quiz', 'student', 'questions', 'submitted', 'score']
        read_only_fields = ['quiz', 'student']

    def delete(self, instance):
        instance.delete()