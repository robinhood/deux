from __future__ import absolute_import, unicode_literals

from django.core.exceptions import ValidationError
from django.test import TestCase

from deux.validators import phone_number_validator


class PhoneNumberValidatorTest(TestCase):

    def test_success(self):
        number = "123456789012345"
        success_tests = (number[:i] for i in range(7, 16))
        for phone_number in success_tests:
            phone_number_validator(phone_number)

    def test_fail(self):
        fail_tests = (
            None,
            "1",
            "123456",
            "123-321-1234",
            "123-123-1234x4321",
            "asdfghjkl;",
            "",
            "123456",
            "12345678901234567"
        )
        for phone_number in fail_tests:
            with self.assertRaises(ValidationError):
                phone_number_validator(phone_number)
