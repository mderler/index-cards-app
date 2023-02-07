import json

from api.models import Topic

from django.test import TestCase

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

    def test_update_topic(self):
        response = self.client.put('/api/topic/1', {'topicName': 'Updated Topic 1'},
                                   'application/json')
        self.assertEqual(response.status_code, 200)
        topic = json.loads(response.content)
        self.assertEqual(topic['id'], 1)
        self.assertEqual(topic['topicName'], 'Updated Topic 1')

    def test_delete_topic(self):
        response = self.client.delete('/api/topic/1')
        self.assertEqual(response.status_code, 204)
        response = self.client.get('/api/topics/')
        self.assertEqual(response.status_code, 200)
        topics = json.loads(response.content)['data']
        self.assertEqual(len(topics), 1)
        self.assertEqual(topics[0]['id'], 2)
        self.assertEqual(topics[0]['topicName'], 'TestTopic2')
