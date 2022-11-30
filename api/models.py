from django.db import models
from django.utils.timezone import now 

class Category(models.TextChoices):
    ONLINE = "ONL", "Online"
    OFFLINE = "OFF", "Offline"

class Event(models.Model):
    name = models.CharField(max_length=128, unique=True)
    author = models.ForeignKey('Author', on_delete=models.PROTECT, null=True)
    start = models.DateTimeField(default=now) 
    end = models.DateTimeField(default=now) 
    category = models.CharField(
        max_length=3,
        choices=Category.choices,
        default=Category.OFFLINE,
    )
    place = models.ForeignKey('Place', on_delete=models.PROTECT, null=True)
    #members_list
    description = models.TextField(blank=True)
    max_members = models.PositiveIntegerField(default=100)
    active = models.BooleanField(default=True)
    free = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name

class Place(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name
