import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from version_lord.models import Version
from version_lord.serializers import VersionSerializer

client = Client()

class  UpdateSingleVersionTest(TestCase):
    """ Test module for updating an existing version record """

    def setUp(self):
        self.kubernetesfake = Version.objects.create(
            software='Kubernetesfake',
            current_version='1.15.1')
        self.grafanafake = Version.objects.create(
            software='Grafanafake',
            current_version='2.15.3')
        self.valid_payload = {
            'software': 'Kubernetesfake',
            'current_version': '6.4.2'
        }
        self.invalid_payload = {
            'software': '',
            'current_version': '3.2.1'
        }
        
    def test_valid_update_version(self):
        response = client.put(
            reverse('get_delete_update_version', kwargs={'pk': self.kubernetesfake.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_version(self):
        response = client.put(
            reverse('get_delete_update_version', kwargs={'pk': self.kubernetesfake.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        