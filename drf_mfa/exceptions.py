from __future__ import absolute_import, unicode_literals

from drf_mfa import strings


class FailedChallengeError(Exception):
    """Generic exception for a failed challenge execution."""
    pass


class NotSMSNumberError(FailedChallengeError):
    """
    Exception for SMS that fails because phone number is not a valid
    number for receiving SMS's.
    """

    def __init__(self, message=strings.NOT_SMS_PHONE_NUMBER_ERROR):
        super(NotSMSNumberError, self).__init__(message)


class TwilioMessageError(FailedChallengeError):
    """
    Exception that Twilio failed to send the text message for reasons
    other than ``NotSMSNumberError``.
    """

    def __init__(self, message=strings.SMS_SEND_ERROR):
        super(TwilioMessageError, self).__init__(message)
