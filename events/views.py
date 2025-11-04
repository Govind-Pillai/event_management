from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Event, RSVP, Review
from .serializers import EventSerializer, RSVPSerializer, ReviewSerializer
from .permissions import IsOrganizerOrReadOnly, IsPrivateEventParticipant

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated, IsOrganizerOrReadOnly, IsPrivateEventParticipant]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Event.objects.filter(is_public=True) | Event.objects.filter(invited_users=self.request.user)
        return Event.objects.filter(is_public=True)

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)

    @action(detail=True, methods=['post'])
    def rsvp(self, request, pk=None):
        event = self.get_object()
        rsvp, created = RSVP.objects.get_or_create(event=event, user=request.user)
        serializer = RSVPSerializer(rsvp, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            status_code = status.HTTP_201_CREATED if created else status.HTTP_200_OK
            return Response(serializer.data, status=status_code)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get', 'post'])
    def reviews(self, request, pk=None):
        event = self.get_object()
        if request.method == 'GET':
            reviews = Review.objects.filter(event=event)
            serializer = ReviewSerializer(reviews, many=True)
            return Response(serializer.data)
        elif request.method == 'POST':
            serializer = ReviewSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(event=event, user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RSVPViewSet(viewsets.ModelViewSet):
    queryset = RSVP.objects.all()
    serializer_class = RSVPSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return RSVP.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
