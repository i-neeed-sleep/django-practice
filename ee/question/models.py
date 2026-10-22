from django.db import models

class Question(models.Model):
    type = models.CharField(max_length=1, choices=[('m', 'multiple choice'), ('s', 'short answer')])
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200, blank=True)
    choices = models.JSONField(blank=True)

class QuestionInstance(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question_instances')
    quiz = models.ManyToManyField('quiz.Quiz', related_name='question_instances')
