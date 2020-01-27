from __future__ import absolute_import, unicode_literals

from django.core.validators import RegexValidator

from deux import strings

#: Regex validator for phone numbers.
phone_number_validator = RegexValidator(
    regex=r"^\+[1-9]\d{1,14}$",
    message=strings.INVALID_PHONE_NUMBER_ERROR)
