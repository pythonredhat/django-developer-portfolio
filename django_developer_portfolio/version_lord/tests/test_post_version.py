import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from version_lord.models import Version
from version_lord.serializers import VersionSerializer

client = Client()

class CreateNewVersionTest(TestCase):
    """ Test module for inserting a new version """

    def setUp(self):
        self.valid_payload = {
            'software': 'Kubernetesfake',
            'current_version': '6.4.2'
        }
        self.invalid_payload = {
            'software': '',
            'current_version': '3.2.1'
        }

    def test_create_valid_version(self):
        response = client.post(
            reverse('get_post_version'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_version(self):
        response = client.post(
            reverse('get_post_version'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
      