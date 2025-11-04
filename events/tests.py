from django.test import TestCase
from django.contrib.auth.models import User
from .models import Event, RSVP, Review
from rest_framework.test import APITestCase
from rest_framework import status

class EventModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.event = Event.objects.create(
            title='Test Event',
            description='Test Description',
            organizer=self.user,
            location='Test Location',
            start_time='2023-01-01T10:00:00Z',
            end_time='2023-01-01T12:00:00Z'
        )

    def test_event_creation(self):
        self.assertEqual(self.event.title, 'Test Event')
        self.assertEqual(self.event.organizer.username, 'testuser')

class EventAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.event = Event.objects.create(
            title='Test Event',
            description='Test Description',
            organizer=self.user,
            location='Test Location',
            start_time='2023-01-01T10:00:00Z',
            end_time='2023-01-01T12:00:00Z'
        )

    def test_get_events(self):
        response = self.client.get('/api/events/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
