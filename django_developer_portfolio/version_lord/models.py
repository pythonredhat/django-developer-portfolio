from django.db import models

import semantic_version

class Version(models.Model):
    software = models.CharField(max_length=255)
    current_version = semantic_version.django_fields.SemVerField()
    last_updated = models.DateTimeField(auto_now=True)


