from __future__ import absolute_import, unicode_literals

from binascii import unhexlify

from django.contrib.auth.models import User
from django.db import models
from django.utils.crypto import constant_time_compare

from deux.app_settings import mfa_settings
from deux.constants import CHALLENGE_TYPES, DISABLED, SMS
from deux.services import generate_key
from deux.validators import phone_number_validator


class AbstractMultiFactorAuth(models.Model):
    """
    class::AbstractMultiFactorAuth()

    This abstract class holds user information, MFA status, and secret
    keys for the user.
    """

    #: Different status options for this MFA object.
    CHALLENGE_CHOICES = (
        (SMS, "SMS"),
        (DISABLED, "Off"),
    )

    #: User this MFA object represents.
    user = models.OneToOneField(
        User, related_name="multi_factor_auth", primary_key=True)

    #: User's phone number.
    phone_number = models.CharField(
        max_length=15, default="", blank=True,
        validators=[phone_number_validator])

    #: Challenge type used for MFA.
    challenge_type = models.CharField(
        max_length=16, default=DISABLED,
        blank=True, choices=CHALLENGE_CHOICES
    )

    #: Secret key used for backup code.
    backup_key = models.CharField(
        max_length=32, default="", blank=True,
        help_text="Hex-Encoded Secret Key"
    )

    #: Secret key used for SMS codes.
    sms_secret_key = models.CharField(
        max_length=32, default=generate_key,
        help_text="Hex-Encoded Secret Key"
    )

    @property
    def sms_bin_key(self):
        """Returns binary data of the SMS secret key."""
        return unhexlify(self.sms_secret_key)

    @property
    def enabled(self):
        """Returns if MFA is enabled."""
        return self.challenge_type in CHALLENGE_TYPES

    @property
    def backup_code(self):
        """Returns the users backup code."""
        return self.backup_key.upper()[:mfa_settings.BACKUP_CODE_DIGITS]

    def get_bin_key(self, challenge_type):
        """
        Returns the key associated with the inputted challenge type.

        :param challenge_type: The challenge type the key is requested for.
                               The type must be in the supported
                               `CHALLENGE_TYPES`.
        :raises AssertionError: If ``challenge_type`` is not a supported
                                challenge type.
        """
        assert challenge_type in CHALLENGE_TYPES, (
            "'{challenge}' is not a valid challenge type.".format(
                challenge=challenge_type)
        )
        return {
            SMS: self.sms_bin_key
        }.get(challenge_type, None)

    def enable(self, challenge_type):
        """
        Enables MFA for this user with the inputted challenge type.

        The enabling process includes setting this objects challenge type and
        generating a new backup key.

        :param challenge_type: Enable MFA for this type of challenge. The type
                               must be in the supported `CHALLENGE_TYPES`.
        :raises AssertionError: If ``challenge_type`` is not a supported
                                challenge type.
        """
        assert challenge_type in CHALLENGE_TYPES, (
            "'{challenge}' is not a valid challenge type.".format(
                challenge=challenge_type)
        )
        self.challenge_type = challenge_type
        self.backup_key = generate_key()
        self.save()

    def disable(self):
        """
        Disables MFA for this user.

        The disabling process includes setting the objects challenge type to
        `DISABLED`, and removing the `backup_key` and `phone_number`.
        """
        self.challenge_type = DISABLED
        self.backup_key = ""
        self.phone_number = ""
        self.save()

    def refresh_backup_code(self):
        """
        Refreshes the users backup key and returns a new backup code.

        This method should be used to request new backup codes for the user.
        """
        assert self.enabled, (
            "MFA must be on to run refresh_backup_codes."
        )
        self.backup_key = generate_key()
        self.save()
        return self.backup_code

    def check_and_use_backup_code(self, code):
        """
        Checks if the inputted backup code is correct and disables MFA if
        the code is correct.

        This method should be used for authenticating with a backup code. Using
        a backup code to authenticate disables MFA as a side effect.
        """
        backup = self.backup_code
        if code and constant_time_compare(code, backup):
            self.disable()
            return True
        return False

    class Meta:
        abstract = True
