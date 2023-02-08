from django.db import models

# Create your models here.


class Topic(models.Model):
    topic_name = models.CharField(max_length=50, unique=True)


class Card(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    question = models.CharField(max_length=250)
    answer = models.CharField(max_length=250)


class PractiseSession(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    session_start = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        is_new = self._state.adding
        super().save(*args, **kwargs)
        if is_new:
            cards = Card.objects.filter(topic=self.topic)
            for card in cards:
                SessionCard.objects.create(card=card, practise_session=self, user_answer='')


class SessionCard(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    practise_session = models.ForeignKey(PractiseSession, on_delete=models.CASCADE)
    user_answer = models.CharField(max_length=250)
    correct = models.BooleanField(null=True)
