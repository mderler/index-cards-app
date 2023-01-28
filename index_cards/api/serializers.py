from rest_framework import serializers

from .models import Card, PractiseSession, SessionCard, Topic


class TopicSerializer(serializers.ModelSerializer):
    topicName = serializers.CharField(source='topic_name')

    class Meta:
        model = Topic
        fields = ['id', 'topicName']
        

class CardSerializer(serializers.ModelSerializer):
    topicId = serializers.IntegerField(source='topic')

    class Meta:
        model = Card
        fields = ['id', 'topicId', 'question', 'answer']


class PractiseSessionSerializer(serializers.ModelSerializer):
    topicId = serializers.IntegerField(source='topic')
    sessionStart = serializers.DateTimeField(source='session_start')

    class Meta:
        model = PractiseSession
        fields = ['id', 'topicId', 'sessionStart']


class SessionCardSerializer(serializers.ModelSerializer):
    cardId = serializers.IntegerField(source='card')
    practiseSession = serializers.IntegerField(source='practise_session')
    userAnswer = serializers.CharField(source='user_answer')

    class Meta:
        model = SessionCard
        fields = ['id', 'cardId', 'practiseSession', 'userAnswer', 'correct']
