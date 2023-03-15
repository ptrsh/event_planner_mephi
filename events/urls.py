from django.urls import path, include
from events.views import EventViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'events', EventViewSet)

urlpatterns = [
    path('', include(router.urls))
]
