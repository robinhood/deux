from __future__ import absolute_import, unicode_literals

from django.core.validators import RegexValidator, EmailValidator

from deux import strings

#: Regex validator for phone numbers.
phone_number_validator = RegexValidator(
    regex=r"^(\+?\d{7,15})$",
    message=strings.INVALID_PHONE_NUMBER_ERROR)

email_address_validator = EmailValidator()
