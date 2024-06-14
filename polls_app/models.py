from django.db import models
from django.contrib.auth.models import User

class Poll(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    responded_users = models.ManyToManyField(User, related_name='answered_polls', blank=True, default=None)

    def __str__(self):
        return self.title

class Option(models.Model):
    text = models.CharField(max_length=200)
    poll = models.ForeignKey(Poll, related_name='option', on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.text

class Response(models.Model):
    answer = models.CharField(max_length=200)
    poll = models.ForeignKey(Poll, related_name='responses', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, related_name='responses', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.answer
