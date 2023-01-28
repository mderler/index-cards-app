from rest_framework import serializers

from .models import Card, PractiseSession, SessionCard, Topic


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'topic_name']
    
    def to_representation(self, instance: Topic):
        return {
            'id': instance.pk,
            'topicName': instance.topic_name
        }
        

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['id', 'topic', 'question', 'answer']

    def to_representation(self, instance: Card):
        representation = super().to_representation(instance)
        del(representation['topic'])
        representation['topicId'] = instance.topic.pk
        return representation


class PractiseSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PractiseSession
        fields = ['id', 'topic', 'session_start']

    def to_representation(self, instance: PractiseSession):
        return {
            'id': instance.pk,
            'topicId': instance.topic.pk,
            'sessionStart': instance.session_start
        }


class SessionCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = SessionCard
        fields = ['id', 'card', 'practise_session', 'user_answer', 'correct']
    
    def to_representation(self, instance: SessionCard):
        return {
            'id': instance.pk,
            'cardId': instance.card.pk,
            'practiseSessionId': instance.practise_session.pk,
            'userAnswer': instance.user_answer,
            'correct': instance.correct
        }
