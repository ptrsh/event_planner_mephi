from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ("name", "author", "start", "end", "category",\
            "place", "members_list", "description", "max_members", "active", "free")