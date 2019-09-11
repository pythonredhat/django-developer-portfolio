from rest_framework import serializers
from .models import Version

class VersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Version
        fields = ('software', 'current_version', 'last_updated')