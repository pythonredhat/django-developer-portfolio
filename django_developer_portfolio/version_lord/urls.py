from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^api/v1/version_lord/(?P<pk>[0-9]+)$',
        views.update_version,
        name='update_version'
    ),
    url(
        r'^api/v1/version_lord/$',
        views.get_post_version,
        name='get_post_version'
    )
]