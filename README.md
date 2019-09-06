# django developer portfolio setup

### Dev environment setup:
```bash
#in project directory:
virtualenv --python python3 envdjangodeveloperportfolio
source envdjangodeveloperportfolio/bin/activate
deactivate
```

### Django install:
```bash
#in virtualenv:
pip install Django==2.0.5
```

### Django validate and verify:
```bash
#in python3 shell
import django
django.get_version()
```

### Dependency management:
```bash
#pin depedencies in current project:
pip freeze > requirements.txt

#download dependencies when working in different environment:
pip install -r requirements.txt
```

### install drf
```bash
pip install djangorestframework
```

### create django project
```bash
django-admin.py startproject api .
```

### create django app
```bash
django-admin.py startapp stockapi
```

### sync db
```bash
python manage.py migrate
```

### create user
```bash
python manage.py createsuperuser --email admin@example.com --username admin
```

### add to settings.py rest_framework and music app:
```bash
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'stockapi'
]
```

### add to urls.py the music app urls:
```bash
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path(''), include('stock.urls'))
]
```

### mac port killer
```
lsof -nP -i4TCP:8000
```

### access rest api
http://localhost:8000/api/v1/stocks

### run test suite
```bash
python manage.py test
```

### add .gitignore file in root directory of repo
```bash
*.pyc
```
Need to do this in order to not have merge conflicts:
https://coderwall.com/p/wrxwog/why-not-to-commit-pyc-files-into-git-and-how-to-fix-if-you-already-did

If you already have .pyc files in your git repo, pull down the master branch and remove them this way:
```bash
Remove .pyc files using git rm *.pyc. If this not work use git rm -f *.pyc
Commit git commit -a -m 'all pyc files removed'
Push git push
In future commits you can ignore .pyc files by creating a .gitignore file
```

### query django db for data of object
```bash
python manage.py shell
from projects.models import Project
#get all objects
Project.objects.all()
#lookup specific field
Project.objects.all().values_list('image')
```

### blog app superuser name
admin

### purpose of admin.py in apps
here you can add data to your models via gui instead of python shell

### reference
https://realpython.com/get-started-with-django-1/