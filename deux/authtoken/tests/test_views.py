from __future__ import absolute_import, unicode_literals

import six
from mock import patch

from django.core.urlresolvers import reverse
from rest_framework import status

from deux.app_settings import mfa_settings
from deux.constants import SMS
from deux.tests.test_base import BaseUserTestCase


class _BaseMFAViewTest(BaseUserTestCase):

    def setUp(self):
        self.simpleUserSetup()
        self.mfa_1 = mfa_settings.MFA_MODEL.objects.create(user=self.user1)
        self.mfa_2 = mfa_settings.MFA_MODEL.objects.create(user=self.user2)
        self.mfa_2.enable(SMS)
        self.phone_number = "1234567890"
        self.mfa_2.phone_number = self.phone_number
        self.mfa_2.save()


class ObtainMFAAuthTokenTest(_BaseMFAViewTest):
    url = reverse("authtoken:login")

    @patch("deux.authtoken.serializers.MultiFactorChallenge")
    def test_login_mfa_required(self, multifactorchallenge):
        # Correct credentials without MFA code.
        data = {
            "username": self.user2.username,
            "password": self.password2
        }
        resp = self.check_post_response(
            self.url, status.HTTP_200_OK, data=data)
        self.assertEqual(resp.data, {
            "mfa_type": SMS,
            "mfa_required": True
        })
        with self.assertRaises(KeyError):
            resp.data["token"]

    def test_login_mfa_not_required(self):
        # Incorrect password.
        data = {"username": self.user1.username,
                "password": "incorrect_password"}
        resp = self.check_post_response(
            self.url, status.HTTP_400_BAD_REQUEST, data=data)
        self.assertEqual(resp.data, {
            "non_field_errors": [
                "Unable to log in with provided credentials."
            ]
        })

        # Correct password.
        data["password"] = self.password1
        resp = self.check_post_response(
            self.url, status.HTTP_200_OK, data=data)
        self.assertEqual(resp.data, {
            "token": six.text_type(self.user1.auth_token),
        })
