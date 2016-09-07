from __future__ import absolute_import, unicode_literals

from deux import strings


class FailedChallengeError(Exception):
    """Generic exception for a failed challenge execution."""
    pass


class InvalidPhoneNumberError(FailedChallengeError):
    """
    Exception for SMS that fails because phone number is not a valid
    number for receiving SMS's.
    """

    def __init__(self, message=strings.INVALID_PHONE_NUMBER_ERROR):
        super(InvalidPhoneNumberError, self).__init__(message)


class TwilioMessageError(FailedChallengeError):
    """
    Exception that Twilio failed to send the text message for reasons
    other than ``NotSMSNumberError``.
    """

    def __init__(self, message=strings.SMS_SEND_ERROR):
        super(TwilioMessageError, self).__init__(message)
