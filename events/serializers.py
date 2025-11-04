from rest_framework import serializers
from .models import Event, RSVP, Review
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class EventSerializer(serializers.ModelSerializer):
    organizer = UserSerializer(read_only=True)
    
    class Meta:
        model = Event
        fields = '__all__'
        read_only_fields = ['organizer', 'created_at', 'updated_at']

class RSVPSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    event = EventSerializer(read_only=True)
    
    class Meta:
        model = RSVP
        fields = '__all__'
        read_only_fields = ['user', 'event']

class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ['user', 'event', 'created_at']
