from __future__ import absolute_import, unicode_literals

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from deux.authtoken import views

urlpatterns = [
    url(r"^login/$", views.ObtainMFAAuthToken.as_view(),
        name="login"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
