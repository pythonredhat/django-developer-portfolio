# django developer portfolio setup

### pipenv setup
```bash
pip3 install pipenv
cd ~/Desktop
mkdir django-project
cd django-project

#check python versions
python3 --version

#setup virtual enviornment
pipenv --three
#or:
pipenv --python 3.6

#enter virtual enviornment
pipenv shell
pipenv install django='1.11.*'
```

### extra pipenv
```bash
#only install dependency for dev
pipenv install pytest --dev

#lock dependencies
pipenv lock

#prod install
pipenv install --ignore-pipfile

#dev install
pipenv install --dev
```

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

### gitlab cicd intregration steps
https://docs.gitlab.com/ee/ci/ci_cd_for_external_repos/github_integration.html

when setting up in github webhooks of repo:
```
Payload URL:
https://gitlab.com/api/v4/projects/<NAMESPACE>%2F<PROJECTNAME>/mirror/pull?private_token=<PERSONALACCESSTOKEN>

Content Type: application/json

Secret: (leave empty)

SSL verification: Enable SSL verification

Which events would you like to trigger this webhook?
Just the push event

Active
```



### docker, postgres, django setup
https://wsvincent.com/django-docker-postgresql/

### docker build and run procedures
```bash
#build image
docker-compose build
#launch daemon
docker-compose up -d
```

### postgresql centos7 install procedure from Postgres repos
```bash
wget https://download.postgresql.org/pub/repos/yum/9.6/redhat/rhel-7-x86_64/pgdg-centos96-9.6-3.noarch.rpm
yum install pgdg-centos96-9.6-3.noarch.rpm epel-release
yum update
yum install postgresql96-server postgresql96-contrib
/usr/pgsql-9.6/bin/postgresql96-setup initdb
systemctl start postgresql-9.6
sudo systemctl enable postgresql-9.6
```
resource: https://www.linode.com/docs/databases/postgresql/how-to-install-postgresql-relational-databases-on-centos-7/


### dockerize django and add postgres,gunicorn,nginx
https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/#gunicorn

### dockerize and add to gitlab cicd
https://testdriven.io/blog/deploying-django-to-digitalocean-with-docker-and-gitlab/

### docker postgres verification procedure
```bash
#connect to db
docker-compose exec db psql --username=hello_django --dbname=hello_django_dev
#list databases
\l
#connect to database
\c hello_django_dev;
#describe tables in database
\dt 
#describe schema of table
\d version_lord_version
docker volume inspect django-developer-portfolio_postgres_data
```

### current build procedures for Docker as of 9/13
```bash
#build web server and database
docker-compose up -d --build
#migrate database
docker-compose exec web python ./django_developer_portfolio/manage.py migrate --noinput
#run through postgres verification procedures above to ensure database has populated
```

### test connection methods
http://fibrevillage.com/sysadmin/80-quick-ways-to-test-remote-machine-port-availability

### go inside container and work
```bash
docker exec -it django-developer-portfolio_web_1 bash
```

### quick way to POST data to db via python shell
```bash
import requests
import json
weburl = 'http://localhost:8000/api/v1/version_lord/'
data = {'current_version': '7.1.1', 'software': 'Red Hat Enterprise Linux 7'}
payload = requests.post(url=weburl, data=json.dumps(data), headers={'Content-Type': 'application/json'})
print (payload.status_code)
print(payload.content)
```

### how gunicorn and nginx work together
```bash
https://vsupalov.com/gunicorn-and-nginx/
```

### how to serve static files with nginx, django, docker
```bash
https://ruddra.com/posts/serve-static-files-by-nginx-from-django-using-docker/
```

### integrate prometheus into django (DONE)
```bash
https://labs.meanpug.com/custom-application-metrics-with-django-prometheus-and-kubernetes/
```

### integrate wsgi,nginx monitoring into Django and then Kubernetes
```bash
https://www.apsl.net/blog/2018/10/01/using-prometheus-monitoring-django-applications-kubernetes/
```