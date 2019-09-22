from blog.models import Category
from blog.models import Post
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User


class Command(BaseCommand): 
    help = 'Populates the postgresql database with fake blog data'

    def handle(self, *args, **options):
      c1 = Category(
        name='web'
        )

      c2 = Category(
        name='big data'
        )

      p1 = Post(
        title="Web post test",
        body="A fake blog post for the web",
        #categories="web"
        )

      p2 = Post(
        title="Big data post test",
        body="A fake blog post for big data",
        #categories="big data"
        )
           
      c1.save()
      c2.save()
      p1.save()
      p2.save()

