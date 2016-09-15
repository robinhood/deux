from __future__ import absolute_import, unicode_literals

from django.utils.translation import ugettext_lazy as _

#: Error if user submits both MFA and backup code for authentication.
BOTH_CODES_ERROR = _(
    "Login does not take both a verification and backup code.")

#: Error if MFA is unexpectedly in a disabled state.
DISABLED_ERROR = _("Two factor authentication is not enabled.")

#: Error if MFA is unexpectedly in an enabled state.
ENABLED_ERROR = _("Two factor authentication is already enabled.")

#: Error if an invalid backup code is entered.
INVALID_BACKUP_CODE_ERROR = _("Please enter a valid backup code.")

#: Error if a user provides an invalid username/password combination.
INVALID_CREDENTIALS_ERROR = _("Unable to log in with provided credentials.")

#: Error if an invalid MFA code is entered.
INVALID_MFA_CODE_ERROR = _("Please enter a valid code.")

#: Error if an invalid phone number is entered.
INVALID_PHONE_NUMBER_ERROR = _("Please enter a valid phone number.")

#: Error if phone number is not set for a challenge that requires it.
PHONE_NUMBER_NOT_SET_ERROR = _(
    "MFA phone number must be set for this challenge.")

#: Error if SMS fails to send.
SMS_SEND_ERROR = _("SMS failed to send.")

#: Message body for a MFA code.
MFA_CODE_TEXT_MESSAGE = _("Two Factor Authentication Code: {code}")
