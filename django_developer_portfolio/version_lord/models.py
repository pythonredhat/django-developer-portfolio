from django.db import models

class Version(models.Model):
    software = models.CharField(max_length=255)
    current_version = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now=True)




