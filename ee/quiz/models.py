from django.db import models

class Quiz(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey('user.User', on_delete=models.CASCADE)
    students = models.ManyToManyField('user.User', related_name='quizzes', blank=True)

class QuizInstance(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='quiz_instances')
    student = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='quiz_instances')
    submitted = models.BooleanField(default=False)
    score = models.IntegerField(blank=True, null=True)