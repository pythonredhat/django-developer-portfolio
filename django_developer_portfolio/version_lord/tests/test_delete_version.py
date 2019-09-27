import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from version_lord.models import Version
from version_lord.serializers import VersionSerializer

client = Client()

class DeleteSingleVersionTest(TestCase):
    """ Test module for deleting an existing version record """

    def setUp(self):
        self.kubernetesfake = Version.objects.create(
            software='Kubernetesfake',
            current_version='1.15.1')
        self.grafanafake = Version.objects.create(
            software='Grafanafake',
            current_version='2.15.3')

    def test_valid_delete_version(self):
        response = client.delete(
            reverse('get_delete_update_version', kwargs={'pk': self.kubernetesfake.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_version(self):
        response = client.delete(
            reverse('get_delete_update_version', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)