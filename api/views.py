from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView


from .models import Event
from .serializers import EventSerializer


class EventAPIList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
