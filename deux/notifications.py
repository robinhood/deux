from __future__ import absolute_import, unicode_literals

from twilio.rest import TwilioRestClient
from twilio.base.exceptions import TwilioRestException
import sendgrid
from sendgrid.helpers.mail import Email, Content, Mail, Substitution

from deux import strings
from deux.app_settings import mfa_settings
from deux.exceptions import InvalidPhoneNumberError, TwilioMessageError, EmailError, InvalidEmailAddressError

try:
    # Python 3
    import urllib.request as urllib
except ImportError:
    # Python 2
    import urllib2 as urllib

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


def send_mfa_code_email(mfa_instance, mfa_code):
    """
    Sends the MFA Code text message to the user.

    :param mfa_instance: :class:`MultiFactorAuth` instance to use.
    :param mfa_code: MFA code in the form of a string.

    :raises deux.exceptions.InvalidEmailError: To tell system that this
        MFA object's email is not a valid email.
    :raises deux.exceptions.EmailError: To tell system that the email failed to send.
    """
    sid = mfa_settings.SENDGRID_API_KEY
    template_id = mfa_settings.SENDGRID_TEMPLATE_ID
    sender_email = mfa_settings.SENDGRID_SENDER_EMAIL
    subject = mfa_settings.SENDGRID_MAIL_SUBJECT
    mfa_text = strings.MFA_CODE_TEXT_MESSAGE.format(code=mfa_code)

    sg = sendgrid.SendGridAPIClient(api_key=sid)
    from_email = Email(sender_email)
    to_email = Email(mfa_instance.email)
    content = Content("text/html", mfa_text)

    mail = Mail(
        from_email=from_email,
        subject=subject,
        to_email=to_email,
        content=content
    )

    if template_id:
        mail.personalizations[0].add_substitution(Substitution('%mfa_text%', mfa_text))
        mail.template_id = template_id

    try:
        sg.client.mail.send.post(request_body=mail.get())
    except urllib.HTTPError:
        raise EmailError()
