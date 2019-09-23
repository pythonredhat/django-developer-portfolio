from version_lord.models import Version
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User


class Command(BaseCommand): 
    help = 'Populates the postgresql database with fake version_lord data'

    def handle(self, *args, **options):
      v1 = Version(
        software='Kubernetes',
        current_version='1.12.1'
        )

      v2 = Version(
        software='Python',
        current_version='3.7.8'
        )

      v3 = Version(
        software='Grafana',
        current_version='4.1.0'
        )
               
      v1.save()
      v2.save()
      v3.save()
