from rest_framework import serializers

from .models import Card, PractiseSession, SessionCard, Topic


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'topic_name']


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['id', 'topic', 'question', 'answer']


class PractiseSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PractiseSession
        fields = ['id', 'topic', 'session_start']


class SessionCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = SessionCard
        fields = ['id', 'card', 'practise_session', 'correct']
