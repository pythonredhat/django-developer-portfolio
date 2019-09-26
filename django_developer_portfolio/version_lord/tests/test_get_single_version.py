import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from version_lord.models import Version
from version_lord.serializers import VersionSerializer

client = Client()

class GetSingleVersionTest(TestCase):
    """ Test module for GET single version API """

    def setUp(self):
        self.kubernetesfake = Version.objects.create(
            software='Kubernetesfake',
            current_version='1.15.1')
        self.grafanafake = Version.objects.create(
            software='Grafanafake',
            current_version='2.15.3')
        self.nagiosfake = Version.objects.create(
            software='Nagiosfake',
            current_version='3.4.1')
        self.dockerfake = Version.objects.create(
            software='Dockerfake',
            current_version='5.3.1')

    def test_get_valid_single_version(self):
        response = client.get(
            reverse('get_delete_update_version', kwargs={'pk': self.nagiosfake.pk}))
        version = Version.objects.get(pk=self.nagiosfake.pk)
        serializer = VersionSerializer(version)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_invalid_single_version(self):
        response = client.get(
            reverse('get_delete_update_version', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        