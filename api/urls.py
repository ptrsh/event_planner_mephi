from django.urls import path
from api.views import EventAPIList, EventAPIDetailView

urlpatterns = [
    path('events/', EventAPIList.as_view()),
    path('events/<int:pk>/', EventAPIDetailView.as_view())
]
