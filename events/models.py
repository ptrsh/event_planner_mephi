from django.db import models
from django.utils.timezone import now
from users.models import User 

def create_default_place():
    place = Place.objects.get_or_create(name='Undefined')[0]
    return place.id

class Category(models.TextChoices):
    ONLINE = "ONL", "Online"
    OFFLINE = "OFF", "Offline"

class Event(models.Model):
    name = models.CharField(max_length=128, unique=True)
    #author = models.ForeignKey('Author', on_delete=models.PROTECT,  default=create_default_author)
    author = models.ForeignKey(User, related_name="event_author", on_delete=models.CASCADE)
    start = models.DateTimeField(default=now) 
    end = models.DateTimeField(default=now) 
    category = models.CharField(
        max_length=3,
        choices=Category.choices,
        default=Category.OFFLINE,
    )
    place = models.ForeignKey('Place', on_delete=models.PROTECT, default=create_default_place)
    #members_list = models.ManyToManyField("Author", related_name="subscribess", blank=True)
    members_list = models.ManyToManyField(User, related_name="event_members", blank=True)
    description = models.TextField(blank=True)
    max_members = models.PositiveIntegerField(default=100)
    active = models.BooleanField(default=True)
    free = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Place(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name
