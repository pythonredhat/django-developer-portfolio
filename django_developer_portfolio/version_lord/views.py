from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Version
from .serializers import VersionSerializer

@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_version(request, pk):
    try:
        version = Version.objects.get(pk=pk)
    except Version.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    #get details of a single version
    if request.method == 'GET':
        serializer = VersionSerializer(version)
        return Response(serializer.data)
    
    #update details of a single version
    elif request.method == 'PUT':
        serializer = VersionSerializer(version, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #delete a single version
    elif request.method == 'DELETE':
        return Response({})

@api_view(['GET', 'POST'])
def get_post_version(request):
    #get all versions
    if request.method == 'GET':
        versions = Version.objects.all()
        serializer = VersionSerializer(versions, many=True)
        return Response(serializer.data)
    #insert a new version for a piece of software
    elif request.method == 'POST':
        data = {
            'software': request.data.get('software'),
            'current_version': request.data.get('current_version')
        }
        serializer = VersionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
