# In quiz_app/models.py

from django.db import models
from django.contrib.auth.models import User

class Quiz(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text

class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text

class QuizTaker(models.Model):
    user = models.ForeignKey(User, related_name='quiz_takers', on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, related_name='quiz_takers', on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return f"{self.user.username} - {self.quiz.title}"

class UserAnswer(models.Model):
    quiz_taker = models.ForeignKey(QuizTaker, related_name='user_answers', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name='+', on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, related_name='+', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.quiz_taker.user.username} - {self.question.text}"
