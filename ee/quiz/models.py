from django.db import models

class Quiz(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    teacher = models.ForeignKey('user.User', on_delete=models.CASCADE)

class QuizInstance(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='quiz_instances')
    student = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='quiz_instances')
    score = models.IntegerField()

