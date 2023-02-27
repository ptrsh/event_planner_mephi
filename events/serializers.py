from .models import Event
from action_serializer import ModelActionSerializer

class EventSerializer(ModelActionSerializer):
    class Meta:
        model = Event
        fields = ("id","name", "author", "start", "end", "category",\
            "place", "members_list", "description", "max_members",\
            "active", "free")
        #.list(), .retrieve(), .create(), .update(), .partial_update(), and .destroy()
        action_fields = {
            'list': {'fields': ("id", "name", "author", "start", "end", "category",\
            "place", "description", "max_members",\
            "active", "free")}
        }