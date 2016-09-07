from __future__ import absolute_import, unicode_literals

from mock import Mock, patch
from twilio.rest.exceptions import TwilioRestException

from deux.app_settings import mfa_settings
from deux.exceptions import InvalidPhoneNumberError, TwilioMessageError
from deux.notifications import send_mfa_code_text_message

from .test_base import BaseUserTestCase


class SendMFACodeTextMessageTests(BaseUserTestCase):

    def setUp(self):
        self.simpleUserSetup()
        self.mfa = mfa_settings.MFA_MODEL.objects.create(user=self.user1)
        self.mfa.phone_number = "1234567890"
        self.mfa.save()
        self.code = "123456"

    @patch("deux.notifications.TwilioRestClient")
    @patch("deux.notifications.mfa_settings")
    def test_success(self, mfa_settings, twilio_client):
        mfa_settings.TWILIO_ACCOUNT_SID = "sid"
        mfa_settings.TWILIO_AUTH_TOKEN = "authtoken"
        mfa_settings.TWILIO_SMS_POOL_SID = "0987654321"

        twilio_client_instance = Mock()
        twilio_client.return_value = twilio_client_instance
        send_mfa_code_text_message(mfa_instance=self.mfa, mfa_code=self.code)
        twilio_client_instance.messages.create.assert_called_once_with(
            body="Two Factor Authentication Code: 123456",
            to="1234567890",
            from_="0987654321"
        )

    @patch("deux.notifications.TwilioRestClient")
    @patch("deux.notifications.mfa_settings")
    def test_invalid_number(self, mfa_settings, twilio_client):
        mfa_settings.TWILIO_ACCOUNT_SID = "sid"
        mfa_settings.TWILIO_AUTH_TOKEN = "authtoken"
        mfa_settings.TWILIO_SMS_POOL_SID = "0987654321"

        twilio_client_instance = Mock()
        twilio_client_instance.messages.create.side_effect = (
            TwilioRestException(400, "abc", code=21401))
        twilio_client.return_value = twilio_client_instance

        with self.assertRaises(InvalidPhoneNumberError):
            send_mfa_code_text_message(
                mfa_instance=self.mfa, mfa_code=self.code)

    @patch("deux.notifications.TwilioRestClient")
    @patch("deux.notifications.mfa_settings")
    def test_failed_sms_error(self, mfa_settings, twilio_client):
        mfa_settings.TWILIO_ACCOUNT_SID = "sid"
        mfa_settings.TWILIO_AUTH_TOKEN = "authtoken"
        mfa_settings.TWILIO_SMS_POOL_SID = "0987654321"

        twilio_client_instance = Mock()
        twilio_client_instance.messages.create.side_effect = (
            TwilioRestException(400, "abc"))
        twilio_client.return_value = twilio_client_instance

        with self.assertRaises(TwilioMessageError):
            send_mfa_code_text_message(
                mfa_instance=self.mfa, mfa_code=self.code)

    @patch("deux.notifications.TwilioRestClient")
    def test_no_twilio_credentials(self, twilio_client):
        twilio_client_instance = Mock()
        twilio_client.return_value = twilio_client_instance
        send_mfa_code_text_message(mfa_instance=self.mfa, mfa_code=self.code)
        twilio_client_instance.messages.create.assert_not_called()
