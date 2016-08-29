from __future__ import absolute_import, unicode_literals

import six
from binascii import unhexlify
from mock import patch

from django.test import TestCase
from django_otp.util import random_hex

from deux.app_settings import mfa_settings
from deux.constants import SMS
from deux.services import (
    MultiFactorChallenge,
    generate_mfa_code,
    verify_mfa_code,
)

from .test_base import BaseUserTestCase


class GenerateMFACodeTests(TestCase):

    def setUp(self):
        self.bin_key = unhexlify(random_hex())

    def test_generate_mfa_code(self):
        mfa_code = generate_mfa_code(self.bin_key)
        self.assertEqual(len(mfa_code), mfa_settings.MFA_CODE_NUM_DIGITS)

    def test_time_based_mfa_code(self):
        mfa_code_0 = generate_mfa_code(self.bin_key, drift=0)
        mfa_code_1 = generate_mfa_code(self.bin_key, drift=1)
        self.assertNotEquals(mfa_code_0, mfa_code_1)


class VerifyMFACodeTests(TestCase):

    def setUp(self):
        self.bin_key = unhexlify(random_hex())

    def test_verify_mfa_code_success(self):
        mfa_code_tests = (
            generate_mfa_code(self.bin_key, -1),
            generate_mfa_code(self.bin_key, 0),
            generate_mfa_code(self.bin_key, 1)
        )
        for mfa_code in mfa_code_tests:
            self.assertTrue(verify_mfa_code(self.bin_key, mfa_code))

    def test_verify_mfa_code_fail(self):
        int_mfa_code = int(generate_mfa_code(self.bin_key, 0))
        mfa_code_tests = (
            None,
            "",
            generate_mfa_code(self.bin_key, -3),
            generate_mfa_code(self.bin_key, -2),
            generate_mfa_code(self.bin_key, 2),
            generate_mfa_code(self.bin_key, 3),
            six.text_type(int_mfa_code + 1).zfill(
                mfa_settings.MFA_CODE_NUM_DIGITS),
            "abcdef"
        )
        for mfa_code in mfa_code_tests:
            self.assertFalse(verify_mfa_code(self.bin_key, mfa_code))


class MultiFactorChallengeTests(BaseUserTestCase):

    def setUp(self):
        self.simpleUserSetup()
        self.mfa = mfa_settings.MFA_MODEL.objects.create(user=self.user1)

    @patch("deux.services.mfa_settings.SEND_MFA_TEXT_FUNC")
    @patch("deux.services.generate_mfa_code")
    def test_sms_challenge(self, generate_mfa_code, text_function):
        generate_mfa_code.return_value = "123456"
        MultiFactorChallenge(self.mfa, SMS).generate_challenge()
        text_function.assert_called_once_with(
            mfa_instance=self.mfa,
            mfa_code="123456")

    def test_invalid_challenge(self):
        fail_tests = ("SMS", "abc", 123)
        for test in fail_tests:
            with self.assertRaises(AssertionError):
                MultiFactorChallenge(self.mfa, test)
