from datetime import datetime

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Card, PractiseSession, SessionCard, Topic


class TopicSerializer(serializers.ModelSerializer):
    topicName = serializers.CharField(source='topic_name', validators=[
        UniqueValidator(queryset=Topic.objects.all())
    ])

    class Meta:
        model = Topic
        fields = ['id', 'topicName']


class CardSerializer(serializers.ModelSerializer):
    topicId = serializers.PrimaryKeyRelatedField(source='topic', queryset=Topic.objects.all())
    question = serializers.CharField(default='')
    answer = serializers.CharField(default='', allow_blank=True)

    class Meta:
        model = Card
        fields = ['id', 'topicId', 'question', 'answer']


class CustomDateTimeField(serializers.Field):
    def to_representation(self, value):
        return value.strftime("%H:%M %d-%m-%Y")


class PractiseSessionSerializer(serializers.ModelSerializer):
    topicId = serializers.PrimaryKeyRelatedField(source='topic', queryset=Topic.objects.all())
    sessionStart = CustomDateTimeField(source='session_start', default=datetime.now)

    class Meta:
        model = PractiseSession
        fields = ['id', 'topicId', 'sessionStart']


class SessionCardSerializer(serializers.ModelSerializer):
    cardId = serializers.PrimaryKeyRelatedField(source='card.id', queryset=Card.objects.all())
    practiseSessionId = serializers.PrimaryKeyRelatedField(source='practise_session.id',
                                                           queryset=PractiseSession.objects.all())
    userAnswer = serializers.CharField(source='user_answer')

    class Meta:
        model = SessionCard
        fields = ['id', 'cardId', 'practiseSessionId', 'userAnswer', 'correct']
