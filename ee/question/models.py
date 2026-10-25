from django.db import models

class Question(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=1, choices=[('m', 'multiple choice'), ('s', 'short answer')])
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200, blank=True)
    choices = models.JSONField(blank=True, null=True)
    quiz = models.ManyToManyField('quiz.Quiz', related_name='question_instances', blank=True)

class QuestionInstance(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question_instances')
    quiz_instance = models.ForeignKey('quiz.QuizInstance', related_name='question_instances', on_delete=models.CASCADE)
    response = models.CharField(max_length=200, blank=True)