from __future__ import absolute_import, unicode_literals

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from deux.oauth2 import views

app_name = 'deux.oauth2'

urlpatterns = [
    url(r'^token/$', views.MFATokenView.as_view(), name="token"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
