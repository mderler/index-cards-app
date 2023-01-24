from django.http import JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Card, Topic, PractiseSession, SessionCard
from .serializers import CardSerializer, PractiseSessionSerializer, TopicSerializer, SessionCardSerializer

# Create your views here.


@api_view(['GET', 'POST'])
def topic_list(request):
    if request.method == 'GET':
        topics = Topic.objects.all()
        serializer = TopicSerializer(topics, many=True)
        return JsonResponse({"data": serializer.data})

    if request.method == 'POST':
        serializer = TopicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def topic_detail(request, pk):
    try:
        topic = Topic.objects.get(pk=pk)
    except Topic.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TopicSerializer(topic)
        return JsonResponse({"data": serializer.data})

    if request.method == 'PUT':
        serializer = TopicSerializer(topic, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        topic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def card_list(request):
    if request.method == 'GET':
        cards = Card.objects.all()
        serializer = CardSerializer(cards, many=True)
        return JsonResponse({"data": serializer.data})

    if request.method == 'POST':
        serializer = CardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def card_list_topic(request, topic):
    if request.method == 'GET':
        cards = Card.objects.filter(topic=topic)
        serializer = CardSerializer(cards, many=True)
        return JsonResponse({"data": serializer.data})


@api_view(['GET', 'PUT', 'DELETE'])
def card_detail(request, pk):
    try:
        card = PractiseSession.objects.get(pk=pk)
    except Card.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CardSerializer(card)
        return JsonResponse({"data": serializer.data})

    if request.method == 'PUT':
        serializer = CardSerializer(card, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        card.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def practise_session_list_topic(request, topic):
    practise_sessions = PractiseSession.objects.filter(topic=topic)
    serializer = PractiseSessionSerializer(practise_sessions, many=True)
    return JsonResponse({"data": serializer.data})


@api_view(['GET', 'POST'])
def practise_session_list_all(request):
    if request.method == 'GET':
        practise_sessions = PractiseSession.objects.all()
        serializer = PractiseSessionSerializer(practise_sessions, many=True)
        return JsonResponse({"data": serializer.data})

    if request.method == 'POST':
        serializer = PractiseSessionSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        pk = serializer.data['id']
        try:
            practise_session = PractiseSession.objects.get(pk=pk)
        except PractiseSession.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        try:
            session_topic = practise_session.topic
        except Topic.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        cards = Card.objects.filter(topic=session_topic)
        for card in cards:
            session_card = SessionCard(card=card, practise_session=practise_session, user_answer='')
            session_card.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE'])
def practise_session_detail(request, pk):
    try:
        practise_session = PractiseSession.objects.get(pk=pk)
    except PractiseSession.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PractiseSessionSerializer(practise_session)
        return JsonResponse({"data": serializer.data})

    if request.method == 'DELETE':
        practise_session.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def session_card_list(request, practise_session):
    if request.method == 'GET':
        session_cards = SessionCard.objects.filter(practise_session=practise_session)
        serializer = SessionCardSerializer(session_cards, many=True)
        return JsonResponse({"data": serializer.data})


@api_view(['GET', 'PUT'])
def session_card_detail(request, pk):
    try:
        session_card = SessionCard.objects.get(pk=pk)
    except SessionCard.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SessionCardSerializer(session_card)
        return JsonResponse({"data": serializer.data})

    if request.method == 'PUT':
        serializer = SessionCardSerializer(session_card, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
