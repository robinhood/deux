from __future__ import absolute_import, unicode_literals

import json
import six
import sys
from base64 import b64encode
from mock import patch
from oauth2_provider.models import get_application_model

from django.core.urlresolvers import reverse
from rest_framework import status

from deux.app_settings import mfa_settings
from deux.constants import SMS
from deux.services import generate_mfa_code
from deux.tests.test_base import BaseUserTestCase

if sys.version_info < (3,):
    from urllib import urlencode
else:
    from urllib.parse import urlencode

Application = get_application_model()


class MFAOAuth2TokenTests(BaseUserTestCase):
    url = reverse("oauth2:token")

    def setUp(self):
        self.simpleUserSetup()
        self.application = Application.objects.create(
            name="Test Password Application",
            user=self.user1,
            authorization_grant_type=Application.GRANT_PASSWORD,
        )
        self.headers = self._get_basic_auth_header(
            self.application.client_id, self.application.client_secret)

        self.mfa = mfa_settings.MFA_MODEL.objects.create(user=self.user2)
        self.mfa.enable(SMS)
        self.phone_number = "1234567890"
        self.mfa.phone_number = self.phone_number
        self.mfa.save()
        self.backup_code = self.mfa.refresh_backup_code()
        self.mfa_code = generate_mfa_code(self.mfa.sms_bin_key)

    def test_incorrect_credentials(self):
        data = self._get_data(
            username=self.user1.username, password="wrong password")
        response = self.check_post_response(
            self.url, status.HTTP_400_BAD_REQUEST, data=data,
            headers=self.headers)
        self._assert_error_msg(
            response, "Unable to log in with provided credentials.")

    def test_inactive_user(self):
        self.user1.is_active = False
        self.user1.save()
        data = self._get_data(
            username=self.user1.username, password=self.user1.password)
        response = self.check_post_response(
            self.url, status.HTTP_400_BAD_REQUEST, data=data,
            headers=self.headers)
        self._assert_error_msg(
            response, "Unable to log in with provided credentials.")

    def test_get_token_mfa_object_does_not_exist(self):
        data = self._get_data(
            username=self.user1.username, password=self.password1)
        response = self.check_post_response(
            self.url, status.HTTP_200_OK, data=data, headers=self.headers)
        self._assert_authenticated(response)

    def test_get_token_mfa_not_required(self):
        self.mfa.disable()
        data = self._get_data()
        response = self.check_post_response(
            self.url, status.HTTP_200_OK, data=data, headers=self.headers)
        self._assert_authenticated(response)

    @patch("deux.oauth2.validators.MultiFactorChallenge")
    def test_get_token_mfa_required(self, challenge):
        data = self._get_data()
        response = self.check_post_response(
            self.url, status.HTTP_200_OK, data=data, headers=self.headers)
        content = json.loads(response.content.decode("utf-8"))
        self.assertTrue(content.get("mfa_required"))
        self.assertEqual(content.get("mfa_type"), SMS)
        challenge.assert_called_once_with(self.mfa, SMS)

    def test_login_success_with_mfa_code(self):
        data = self._get_data(mfa_code=self.mfa_code)
        response = self.check_post_response(
            self.url, status.HTTP_200_OK, data=data, headers=self.headers)
        self._assert_authenticated(response)

    def test_login_fail_with_invalid_mfa_code(self):
        bad_code = six.text_type(int(self.mfa_code) + 1)
        data = self._get_data(mfa_code=bad_code)
        response = self.check_post_response(
            self.url, status.HTTP_400_BAD_REQUEST, data=data,
            headers=self.headers)
        self._assert_error_msg(response, "Please enter a valid code.")

    def test_login_success_with_backup_code(self):
        data = self._get_data(backup_code=self.backup_code)
        response = self.check_post_response(
            self.url, status.HTTP_200_OK, data=data, headers=self.headers)
        self._assert_authenticated(response)

    def test_login_fail_with_invalid_backup_code(self):
        bad_backup_code = "abcdef123456"
        data = self._get_data(backup_code=bad_backup_code)
        response = self.check_post_response(
            self.url, status.HTTP_400_BAD_REQUEST, data=data,
            headers=self.headers)
        self._assert_error_msg(response, "Please enter a valid backup code.")

    def test_login_fail_with_both_codes(self):
        data = self._get_data(
            mfa_code=self.mfa_code, backup_code=self.backup_code)
        response = self.check_post_response(
            self.url, status.HTTP_400_BAD_REQUEST, data=data,
            headers=self.headers)
        self._assert_error_msg(
            response,
            "Login does not take both a verification and backup code."
        )

    def test_login_success_with_multipart(self):
        data = self._get_data(backup_code=self.backup_code)
        response = self.check_post_response(
            self.url, status.HTTP_200_OK, data=data, headers=self.headers,
            format="multipart")
        self._assert_authenticated(response)

    def test_login_success_with_urlencoded(self):
        data = self._get_data(backup_code=self.backup_code)
        response = self.check_post_response_with_url_encoded(
            self.url, status.HTTP_200_OK, data=urlencode(data),
            headers=self.headers)
        self._assert_authenticated(response)

    def _assert_authenticated(self, response):
        content = json.loads(response.content.decode("utf-8"))
        self.assertIsNotNone(content.get("access_token"))
        self.assertIsNotNone(content.get("refresh_token"))

    def _assert_error_msg(self, response, msg):
        content = json.loads(response.content.decode("utf-8"))
        self.assertEqual(content["detail"], msg)

    def _get_data(
            self, username=None, password=None, mfa_code=None,
            backup_code=None):
        data = {
            "grant_type": "password",
            "username": username or self.user2.username,
            "password": password or self.password2,
        }
        if mfa_code:
            data["mfa_code"] = mfa_code
        if backup_code:
            data["backup_code"] = backup_code
        return data

    def _get_basic_auth_header(self, client_id, client_secret):
        """
        Return a dict containg the correct headers to set to make HTTP
        an Auth request to Oauth2.
        """
        id_secret = '{id}:{secret}'.format(id=client_id, secret=client_secret)
        auth_string = b64encode(id_secret.encode('utf-8'))
        return {'HTTP_AUTHORIZATION': 'Basic ' + auth_string.decode("utf-8")}
