from django.db import models

# Create your models here.


class Topic(models.Model):
    topic_name = models.CharField(max_length=50)


class Card(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    question = models.CharField(max_length=250)
    answer = models.CharField(max_length=250)


class PractiseSession(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    session_start = models.DateTimeField()


class SessionCard(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    practise_session = models.ForeignKey(PractiseSession, on_delete=models.CASCADE)
    correct = models.BooleanField(null=True)
