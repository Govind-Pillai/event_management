from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, RSVPViewSet

router = DefaultRouter()
router.register(r'events', EventViewSet, basename='event')
router.register(r'rsvps', RSVPViewSet, basename='rsvp')

urlpatterns = [
    path('', include(router.urls)),
]
