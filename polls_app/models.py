from django.db import models
from django.contrib.auth.models import User

class Poll(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Question(models.Model):
    text = models.CharField(max_length=200)
    poll = models.ForeignKey(Poll, related_name='questions', on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class Response(models.Model):
    answer = models.CharField(max_length=200)
    question = models.ForeignKey(Question, related_name='responses', on_delete=models.CASCADE)

    def __str__(self):
        return self.answer
