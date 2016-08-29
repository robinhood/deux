from __future__ import absolute_import, unicode_literals

from deux.app_settings import mfa_settings
from deux.constants import DISABLED, SMS

from .test_base import BaseUserTestCase


class MultiFactorAuthTests(BaseUserTestCase):

    def setUp(self):
        self.simpleUserSetup()
        self.mfa = mfa_settings.MFA_MODEL.objects.create(
            user=self.user1, phone_number="12345678900")

    def test_default_disabled(self):
        self.assertEqual(self.mfa.challenge_type, DISABLED)
        self.assertFalse(self.mfa.enabled)
        self.assertEqual(self.mfa.backup_code, "")

    def test_set_sms_enabled(self):
        self.mfa.enable(SMS)
        self.assertEqual(self.mfa.challenge_type, SMS)
        self.assertTrue(self.mfa.enabled)
        self.assertEqual(
            len(self.mfa.backup_code), mfa_settings.BACKUP_CODE_DIGITS)

    def test_disable(self):
        self.mfa.enable(SMS)
        self.assertEqual(self.mfa.challenge_type, SMS)

        self.mfa.disable()
        self.assertEqual(self.mfa.challenge_type, DISABLED)
        self.assertFalse(self.mfa.enabled)

    def test_phone_number(self):
        self.assertEqual(self.mfa.phone_number, "12345678900")

    def test_backup_code_generation(self):
        # AssertionError if disabled.
        with self.assertRaises(AssertionError):
            self.mfa.refresh_backup_code()

        # Valid backup code if enabled.
        self.mfa.enable(SMS)
        self.assertEqual(
            len(self.mfa.refresh_backup_code()),
            mfa_settings.BACKUP_CODE_DIGITS
        )

        # Codes should not be same after regeneration.
        current_code = self.mfa.backup_code
        new_code = self.mfa.refresh_backup_code()
        self.assertIsNotNone(new_code)
        self.assertNotEquals(current_code, new_code)

    def test_check_and_use_backup_code(self):
        self.mfa.enable(SMS)
        self.mfa.refresh_backup_code()

        # Test for using incorrect code.
        bad_code = "123456abcdef"
        self.assertFalse(self.mfa.check_and_use_backup_code(bad_code))

        # Test for using correct code.
        code = self.mfa.backup_code
        self.assertTrue(self.mfa.check_and_use_backup_code(code))
        instance = mfa_settings.MFA_MODEL.objects.get(user=self.user1)
        self.assertFalse(instance.enabled)
        self.assertEqual(instance.challenge_type, DISABLED)
