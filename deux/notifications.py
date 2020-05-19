from __future__ import absolute_import, unicode_literals

from twilio.rest import TwilioRestClient
from twilio.base.exceptions import TwilioRestException

from deux import strings
from deux.app_settings import mfa_settings
from deux.exceptions import InvalidPhoneNumberError, TwilioMessageError

#: Error code from Twilio to indicate at ``InvalidPhoneNumberError``
NOT_SMS_DEVICE_CODE = 21401


def send_mfa_code_text_message(mfa_instance, mfa_code):
    """
    Sends the MFA Code text message to the user.

    :param mfa_instance: :class:`MultiFactorAuth` instance to use.
    :param mfa_code: MFA code in the form of a string.

    :raises deux.exceptions.InvalidPhoneNumberError: To tell system that this
        MFA object's phone number if not a valid number to receive SMS's.
    :raises deux.exceptions.TwilioMessageError: To tell system that Twilio
        failed to send message.
    """

    sid = mfa_settings.TWILIO_ACCOUNT_SID
    token = mfa_settings.TWILIO_AUTH_TOKEN
    twilio_num = mfa_settings.TWILIO_SMS_POOL_SID
    if not sid or not token or not twilio_num:
        print("Please provide Twilio credentials to send text messages. For "
              "testing purposes, the MFA code is {code}".format(code=mfa_code))
        return

    twilio_client = TwilioRestClient(sid, token)
    try:
        twilio_client.messages.create(
            body=strings.MFA_CODE_TEXT_MESSAGE.format(code=mfa_code),
            to=mfa_instance.phone_number,
            from_=twilio_num
        )
    except TwilioRestException as e:
        if e.code == NOT_SMS_DEVICE_CODE:
            raise InvalidPhoneNumberError()
        raise TwilioMessageError()
