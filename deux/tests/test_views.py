from __future__ import absolute_import, unicode_literals

from mock import patch

from django.core.urlresolvers import reverse
from rest_framework import status

from deux.app_settings import mfa_settings
from deux.constants import DISABLED, SMS
from deux.exceptions import FailedChallengeError
from deux.services import generate_mfa_code
from deux import strings

from .test_base import BaseUserTestCase


class _BaseMFAViewTest(BaseUserTestCase):

    def setUp(self):
        self.simpleUserSetup()
        self.mfa_1 = mfa_settings.MFA_MODEL.objects.create(user=self.user1)
        self.mfa_2 = mfa_settings.MFA_MODEL.objects.create(user=self.user2)
        self.mfa_2.enable(SMS)
        self.phone_number = "1234567890"
        self.mfa_2.phone_number = self.phone_number
        self.mfa_2.save()


class MultiFactorAuthViewTest(_BaseMFAViewTest):
    url = reverse("multi_factor_auth-detail")

    def test_get(self):
        # Check for HTTP401.
        self.check_get_response(self.url, status.HTTP_403_FORBIDDEN)

        # Check for HTTP200 - MFA for a disabled user.
        resp = self.check_get_response(
            self.url, status.HTTP_200_OK, user=self.user1
        )
        resp_json = resp.data
        self.assertEqual(resp_json["enabled"], False)
        with self.assertRaises(KeyError):
            resp_json["challenge_type"]

        # Check for HTTP200 - MFA Enabled User.
        resp = self.check_get_response(
            self.url, status.HTTP_200_OK, user=self.user2
        )
        resp_json = resp.data
        self.assertEqual(resp_json["enabled"], True)
        self.assertEqual(resp_json["challenge_type"], SMS)

    def test_delete(self):
        # Check for HTTP401.
        self.check_delete_response(self.url, status.HTTP_403_FORBIDDEN)

        # Check for HTTP400 - MFA for a disabled user.
        resp = self.check_delete_response(
            self.url, status.HTTP_400_BAD_REQUEST, user=self.user1)
        self.assertEqual(resp.data, {
            "detail": strings.DISABLED_ERROR
        })

        # Check for HTTP200.
        self.mfa_2.refresh_backup_code()
        self.check_delete_response(
            self.url, status.HTTP_204_NO_CONTENT, user=self.user2)
        instance = mfa_settings.MFA_MODEL.objects.get(user=self.user2)
        self.assertFalse(instance.enabled)
        self.assertEqual(instance.challenge_type, DISABLED)
        self.assertEqual(instance.backup_code, "")
        self.assertEqual(instance.phone_number, "")


class SMSChallengeRequestViewTest(_BaseMFAViewTest):
    url = reverse("sms_request-detail")

    def test_unauthorized(self):
        self.check_put_response(self.url, status.HTTP_403_FORBIDDEN)

    def test_already_enabled(self):
        resp = self.check_put_response(
            self.url, status.HTTP_400_BAD_REQUEST, user=self.user2,
            data={"phone_number": self.phone_number})
        self.assertEqual(resp.data, {"detail": [strings.ENABLED_ERROR]})

    def test_bad_phone_numbers(self):
        # No phone number inputted.
        resp = self.check_put_response(
            self.url, status.HTTP_400_BAD_REQUEST, user=self.user1)
        self.assertEqual(resp.data, {
            "phone_number": ["This field is required."]
        })

        # Invalid phone number.
        resp = self.check_put_response(
            self.url, status.HTTP_400_BAD_REQUEST, user=self.user1,
            data={"phone_number": "bad_number"})
        self.assertEqual(resp.data, {
            "phone_number": [strings.INVALID_PHONE_NUMBER_ERROR]
        })

    @patch("deux.serializers.MultiFactorChallenge")
    def test_failed_sms_error(self, challenge):
        challenge.return_value.generate_challenge.side_effect = (
            FailedChallengeError("Error Message."))
        resp = self.check_put_response(
            self.url, status.HTTP_400_BAD_REQUEST, user=self.user1,
            data={"phone_number": self.phone_number})
        self.assertEqual(resp.data, {
            "detail": "Error Message."
        })

    @patch("deux.serializers.MultiFactorChallenge")
    def test_success(self, challenge):
        resp = self.check_put_response(
            self.url, status.HTTP_200_OK, user=self.user1,
            data={"phone_number": self.phone_number})
        self.assertEqual(resp.data, {
            "enabled": False, "phone_number": self.phone_number
        })
        challenge.assert_called_once_with(self.mfa_1, SMS)
        challenge.return_value.generate_challenge.assert_called_once_with()


class SMSChallengeVerifyViewTest(_BaseMFAViewTest):
    url = reverse("sms_verify-detail")

    def test_unauthorized(self):
        self.check_put_response(self.url, status.HTTP_403_FORBIDDEN)

    def test_already_enabled(self):
        resp = self.check_put_response(
            self.url, status.HTTP_400_BAD_REQUEST, user=self.user2,
            data={"mfa_code": "code"})
        self.assertEqual(resp.data, {"detail": [strings.ENABLED_ERROR]})

    def test_incorrect_mfa_codes(self):
        # Check for failure with incorrect mfa_code.
        resp = self.check_put_response(
            self.url, status.HTTP_400_BAD_REQUEST, user=self.user1,
            data={"mfa_code": "bad_code"}
        )
        self.assertEqual(resp.data, {
            "mfa_code": [strings.INVALID_MFA_CODE_ERROR]
        })

        # Check for failure with None mfa_code.
        self.check_put_response(
            self.url, status.HTTP_400_BAD_REQUEST,
            user=self.user1, data=None
        )
        self.assertEqual(resp.data, {
            "mfa_code": [strings.INVALID_MFA_CODE_ERROR]
        })

    def test_success(self):
        mfa_code = generate_mfa_code(self.mfa_1.sms_bin_key)
        resp = self.check_put_response(
            self.url, status.HTTP_200_OK, user=self.user1,
            data={"mfa_code": mfa_code}
        )
        resp_json = resp.data
        self.assertEqual(resp_json["enabled"], True)
        self.assertEqual(resp_json["challenge_type"], SMS)
        instance = mfa_settings.MFA_MODEL.objects.get(user=self.user1)
        self.assertTrue(instance.enabled)
        self.assertEqual(instance.challenge_type, SMS)


class BackupCodesViewTest(_BaseMFAViewTest):
    url = reverse("backup_code-detail")

    def test_get(self):
        # Check for HTTP401.
        self.check_get_response(self.url, status.HTTP_403_FORBIDDEN)

        # Check for HTTP400 - MFA for a disabled user.
        resp = self.check_get_response(
            self.url, status.HTTP_400_BAD_REQUEST, user=self.user1)
        self.assertEqual(resp.data, {
            "backup_code": strings.DISABLED_ERROR
        })

        # Check for HTTP200.
        resp = self.check_get_response(
            self.url, status.HTTP_200_OK, user=self.user2)
        self.assertEqual(
            len(resp.data["backup_code"]), mfa_settings.BACKUP_CODE_DIGITS)
