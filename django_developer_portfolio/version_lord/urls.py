from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(
        r'^api/v1/version_lord/(?P<pk>[0-9]+)$',
        views.get_delete_update_version,
        name='get_delete_update_version'
    ),
    url(
        r'^api/v1/version_lord/$',
        views.get_post_version,
        name='get_post_version'
    ),
    path("", views.version_lord_index, name="version_lord_index")
]