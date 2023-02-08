import json

from api.models import Card, PractiseSession, SessionCard, Topic

from django.test import TestCase

from rest_framework import status

# Create your tests here.


class TopicTestCase(TestCase):
    def setUp(self) -> None:
        Topic.objects.create(topic_name='TestTopic1')
        Topic.objects.create(topic_name='TestTopic2')

    def test_get_topics(self):
        response = self.client.get('/api/topics/')
        self.assertEqual(response.status_code, 200)
        topics = json.loads(response.content)['data']
        self.assertEqual(len(topics), 2)
        self.assertEqual(topics[0]['id'], 1)
        self.assertEqual(topics[0]['topicName'], 'TestTopic1')
        self.assertEqual(topics[1]['id'], 2)
        self.assertEqual(topics[1]['topicName'], 'TestTopic2')

    def test_get_topic(self):
        response = self.client.get('/api/topic/1')
        self.assertEqual(response.status_code, 200)
        topics = json.loads(response.content)['data']
        self.assertEqual(topics['id'], 1)
        self.assertEqual(topics['topicName'], 'TestTopic1')

        response = self.client.get('/api/topic/99')
        self.assertEqual(response.status_code, 404)

    def test_create_topic(self):
        response = self.client.post('/api/topics/', {'topicName': 'Topic 3'})
        self.assertEqual(response.status_code, 201)
        topic = json.loads(response.content)
        self.assertEqual(topic['id'], 3)
        self.assertEqual(topic['topicName'], 'Topic 3')

        response = self.client.post('/api/topics/', {})
        self.assertEqual(response.status_code, 400)

        response = self.client.post('/api/topics/', {'topicName': 'Topic 3'})
        self.assertEqual(response.status_code, 400)

    def test_update_topic(self):
        response = self.client.put('/api/topic/1', {'topicName': 'Updated Topic 1'},
                                   'application/json')
        self.assertEqual(response.status_code, 200)
        topic = json.loads(response.content)
        self.assertEqual(topic['id'], 1)
        self.assertEqual(topic['topicName'], 'Updated Topic 1')

        response = self.client.put('/api/topic/1', {}, 'application/json')
        self.assertEqual(response.status_code, 400)

        response = self.client.post('/api/topics/', {'topicName': 'Updated Topic 2'})
        self.assertEqual(response.status_code, 201)

        response = self.client.put('/api/topic/1', {'topicName': 'Updated Topic 2'},
                                   'application/json')
        self.assertEqual(response.status_code, 400)

        response = self.client.put('/api/topic/99', {'topicName': 'Topic 3'},
                                   'application/json')
        self.assertEqual(response.status_code, 404)

    def test_delete_topic(self):
        response = self.client.delete('/api/topic/1')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Topic.objects.count(), 1)
        self.assertEqual(Topic.objects.get().topic_name, 'TestTopic2')


class CardTestCase(TestCase):
    def setUp(self):
        self.topic = Topic.objects.create(topic_name='Math')
        self.valid_payload = {
            'topicId': self.topic.id,
            'question': '1+1',
            'answer': '2'
        }
        self.invalid_payload = {
            'topicId': self.topic.id,
            'question': '',
            'answer': ''
        }

    def test_create_valid_card(self):
        response = self.client.post(
            '/api/cards/',
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Card.objects.count(), 1)
        self.assertEqual(Card.objects.get().question, '1+1')

    def test_create_invalid_card(self):
        response = self.client.post(
            '/api/cards/',
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)

    def test_update_valid_card(self):
        card = Card.objects.create(topic=self.topic, question='1+1', answer='2')
        response = self.client.put(
            '/api/card/%s' % card.id,
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Card.objects.count(), 1)
        self.assertEqual(Card.objects.get().question, '1+1')

    def test_update_invalid_card(self):
        card = Card.objects.create(topic=self.topic, question='1+1', answer='2')
        response = self.client.put(
            '/api/card/%s' % card.id,
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)

    def test_delete_card(self):
        card = Card.objects.create(topic=self.topic, question='1+1', answer='2')
        response = self.client.delete('/api/card/%s' % card.id)
        self.assertEqual(response.status_code, 204)


class PractiseSessionTests(TestCase):

    def setUp(self):
        self.topic = Topic.objects.create(topic_name="test topic")
        self.valid_payload = {
            'topicId': self.topic.id,
        }
        self.invalid_payload = {
            'topic': 0,
        }

    def test_create_valid_practise_session(self):
        response = self.client.post(
            '/api/practisesessions/',
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_practise_session(self):
        response = self.client.post(
            '/api/practisesessions/',
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_practise_sessions(self):
        PractiseSession.objects.create(topic=self.topic)
        response = self.client.get(
            '/api/practisesessions/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_practise_session(self):
        practise_session = PractiseSession.objects.create(topic=self.topic)
        response = self.client.delete(
            '/api/practisesession/%s' % practise_session.id
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class SessionCardTests(TestCase):
    def setUp(self):
        topic = Topic.objects.create(topic_name='Test Topic')
        topic.save()
        self.cards = [
            {'q': 'q1', 'a': 'a1'},
            {'q': 'q2', 'a': 'a3'},
            {'q': '2*2', 'a': '4'},
            {'q': 'high', 'a': 'hoch'},
            {'q': 'low', 'a': 'niedrig'},
            {'q': 'q3', 'a': 'a3'},
        ]
        for card in self.cards:
            Card.objects.create(topic=topic, question=card['q'], answer=card['a']).save()
        self.practise_session = PractiseSession.objects.create(topic=topic)
        self.practise_session.save()

    def test_get_session_cards(self):
        response = self.client.get('/api/sessioncards/%s' % self.practise_session.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        session_cards = json.loads(response.content)['data']
        self.assertEqual(len(session_cards), len(self.cards))

    def test_update_session_card(self):
        data = {
            'userAnswer': 'Updated User Answer',
            'correct': True
        }
        response = self.client.put('/api/sessioncard/1', data,
                                   'application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        session_card = SessionCard.objects.get(pk=1)
        self.assertEqual(session_card.user_answer, 'Updated User Answer')
        self.assertEqual(session_card.correct, True)
