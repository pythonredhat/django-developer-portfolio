from blog.models import Category
from blog.models import Post
#from django.contrib.auth.models import User

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

if __name__ == "__main__":
    c1.save()
    c2.save()
    p1.save()
    p2.save()

