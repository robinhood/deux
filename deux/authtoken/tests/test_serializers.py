from __future__ import absolute_import, unicode_literals

import six
from mock import patch

from deux.app_settings import mfa_settings
from deux.constants import DISABLED, SMS
from deux.authtoken.serializers import MFAAuthTokenSerializer
from deux.services import generate_mfa_code
from deux.tests.test_base import BaseUserTestCase


class MFAAuthTokenSerializerTest(BaseUserTestCase):

    def setUp(self):
        self.simpleUserSetup()
        self.mfa = mfa_settings.MFA_MODEL.objects.create(user=self.user2)

    def test_login_with_no_mfa_object(self):
        serializer = MFAAuthTokenSerializer(data={
            "username": self.user1.username,
            "password": "incorrect_password",
        })
        self.assertFalse(serializer.is_valid())

        serializer = MFAAuthTokenSerializer(data={
            "username": self.user1.username,
            "password": self.password1
        })
        self.assertTrue(serializer.is_valid())

    def test_login_with_disabled_mfa_object(self):
        serializer = MFAAuthTokenSerializer(data={
            "username": self.user2.username,
            "password": "incorrect_password",
        })
        self.assertFalse(serializer.is_valid())

        serializer = MFAAuthTokenSerializer(data={
            "username": self.user2.username,
            "password": self.password2
        })
        self.assertTrue(serializer.is_valid())

    def test_login_fail_with_both_codes(self):
        self.mfa.enable(SMS)
        self.mfa.refresh_backup_code()

        mfa_code = generate_mfa_code(self.mfa.sms_bin_key)
        backup_code = self.mfa.backup_code

        serializer = MFAAuthTokenSerializer(data={
            "username": self.user2.username,
            "password": self.password2,
            "mfa_code": mfa_code,
            "backup_code": backup_code
        })
        self.assertFalse(serializer.is_valid())

    def test_login_with_mfa_code(self):
        self.mfa.enable(SMS)
        mfa_code = generate_mfa_code(self.mfa.sms_bin_key)
        serializer = MFAAuthTokenSerializer(data={
            "username": self.user2.username,
            "password": self.password2,
            "mfa_code": mfa_code
        })
        self.assertTrue(serializer.is_valid())

        bad_code = six.text_type(int(mfa_code) + 1)
        serializer = MFAAuthTokenSerializer(data={
            "username": self.user2.username,
            "password": self.password2,
            "mfa_code": bad_code
        })
        self.assertFalse(serializer.is_valid())

    def test_login_with_backup_code(self):
        self.mfa.enable(SMS)
        bad_code = "abcdef123456"
        serializer = MFAAuthTokenSerializer(data={
            "username": self.user2.username,
            "password": self.password2,
            "backup_code": bad_code
        })
        self.assertFalse(serializer.is_valid())

        backup_code = self.mfa.backup_code
        serializer = MFAAuthTokenSerializer(data={
            "username": self.user2.username,
            "password": self.password2,
            "backup_code": backup_code
        })
        self.assertTrue(serializer.is_valid(raise_exception=True))
        instance = mfa_settings.MFA_MODEL.objects.get(user=self.user2)
        self.assertFalse(instance.enabled)
        self.assertEqual(instance.challenge_type, DISABLED)
        self.assertEqual(instance.backup_code, "")

    @patch("deux.authtoken.serializers.MultiFactorChallenge")
    def test_login_and_continue_with_challenge(self, challenge):
        self.mfa.enable(SMS)
        self.mfa.phone_number = "1234567890"
        self.mfa.save()
        serializer = MFAAuthTokenSerializer(data={
            "username": self.user2.username,
            "password": "incorrect_password",
        })
        self.assertFalse(serializer.is_valid())

        # With correct username and password, response should require MFA.
        serializer = MFAAuthTokenSerializer(data={
            "username": self.user2.username,
            "password": self.password2
        })
        self.assertTrue(serializer.is_valid())
        data = serializer.validated_data
        self.assertTrue(data["mfa_required"])
        self.assertEqual(data["mfa_type"], SMS)
        challenge.assert_called_once_with(self.mfa, SMS)
        challenge.return_value.generate_challenge.assert_called_once_with()

    def test_login_with_other_users_code(self):
        mfa_1 = mfa_settings.MFA_MODEL.objects.create(user=self.user1)
        mfa_2 = self.mfa

        mfa_1.enable(SMS)
        mfa_2.enable(SMS)

        # User 1 using User 2's MFA Code should fail.
        mfa_2_code = generate_mfa_code(mfa_2.sms_bin_key)
        serializer = MFAAuthTokenSerializer(data={
            "username": self.user1.username,
            "password": self.password1,
            "mfa_code": mfa_2_code
        })
        self.assertFalse(serializer.is_valid())

        # User 1 using User 2's Backup Code should fail.
        mfa_2_backup = mfa_2.backup_code
        serializer = MFAAuthTokenSerializer(data={
            "username": self.user1.username,
            "password": self.password1,
            "backup_code": mfa_2_backup
        })
        self.assertFalse(serializer.is_valid())
