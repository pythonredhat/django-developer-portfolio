import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from version_lord.models import Version
from version_lord.serializers import VersionSerializer

client = Client()

class GetAllVersions(TestCase):
    """ Test module for GET all versions API """

    def setUp(self):
        Version.objects.create(
            software='Kubernetes', current_version='1.12.1')
        Version.objects.create(
            software='Grafana', current_version='4.2.3')
        Version.objects.create(
            software='Nagios', current_version='7.8')
        
    def test_get_all_versions(self):
        #get API response
        response = client.get(reverse('get_post_version'))
        #get data from db
        versions = Version.objects.all()
        serializer = VersionSerializer(versions, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
     