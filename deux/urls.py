from __future__ import absolute_import, unicode_literals

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from deux import views

urlpatterns = [
    url(r"^$", views.MultiFactorAuthDetail.as_view(),
        name="multi_factor_auth-detail"),
    url(r"^sms/request/$", views.SMSChallengeRequestDetail.as_view(),
        name="sms_request-detail"),
    url(r"^sms/verify/$", views.SMSChallengeVerifyDetail.as_view(),
        name="sms_verify-detail"),
    url(r"^recovery/$", views.BackupCodeDetail.as_view(),
        name="backup_code-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
