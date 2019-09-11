from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Version
from .serializers import VersionSerializer

@api_view(['PUT'])
def updated_version(request, pk):
    try:
        version = Version.objects.get(pk=pk)
    except Version.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    #update details of a single version
    if request.method == 'PUT':
        return Response({})

@api_view(['GET', 'POST'])
def get_post_version(request):
    #get all versions
    if request.method == 'GET':
        return Response({})
    #insert a new version for a piece of software
    elif request.method == 'POST':
        return Response({})
