from __future__ import unicode_literals

from django.urls import re_path

from .views import Rate
from . import app_settings


urlpatterns = [
    re_path(r'(?P<content_type_id>\d+)/(?P<object_id>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/', Rate.as_view(), name='rate'),
]

app_name = 'star_ratings'
