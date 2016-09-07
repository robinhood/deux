from __future__ import absolute_import, unicode_literals

import six
from uuid import uuid4

from django.utils.crypto import constant_time_compare
from django_otp.oath import totp

from deux.app_settings import mfa_settings
from deux.constants import CHALLENGE_TYPES, SMS


def generate_mfa_code(bin_key, drift=0):
    """
    Generates an MFA code based on the ``bin_key`` for the current timestamp
    offset by the ``drift``.

    :param bin_key: The secret key to be converted into an MFA code
    :param drift: Number of time steps to shift the conversion.
    """
    return six.text_type(totp(
        bin_key,
        step=mfa_settings.STEP_SIZE,
        digits=mfa_settings.MFA_CODE_NUM_DIGITS,
        drift=drift
    )).zfill(mfa_settings.MFA_CODE_NUM_DIGITS)


def generate_key():
    """Generates a key used for secret keys."""
    return uuid4().hex


def verify_mfa_code(bin_key, mfa_code):
    """
    Verifies that the inputted ``mfa_code`` is a valid code for the given
    secret key. We check the ``mfa_code`` against the current time stamp as
    well as one time step before and after.

    :param bin_key: The secret key to verify the MFA code again.
    :param mfa_code: The code whose validity this function tests.
    """
    if not mfa_code:
        return False
    try:
        mfa_code = int(mfa_code)
    except ValueError:
        return False
    else:
        totp_check = lambda drift: int(
            generate_mfa_code(bin_key=bin_key, drift=drift))
        return any(
            constant_time_compare(totp_check(drift), mfa_code)
            for drift in [-1, 0, 1]
        )


class MultiFactorChallenge(object):
    """
    A class that represents a supported challenge and has the ability to
    execute the challenge.

    :param instance: :class:`MultiFactorAuth` instance to use.
    :param challenge_type: Challenge type being used for this object.
    :raises AssertionError: If ``challenge_type`` is not a supported
        challenge type.
    """

    def __init__(self, instance, challenge_type):
        assert challenge_type in CHALLENGE_TYPES, (
            "Inputted challenge type is not supported."
        )
        self.instance = instance
        self.challenge_type = challenge_type

    def generate_challenge(self):
        """
        Generates and executes the challenge object based on the challenge
        type of this object.
        """
        dispatch = {
            SMS: self._sms_challenge
        }
        for challenge in CHALLENGE_TYPES:
            assert challenge in dispatch, (
                "'{challenge}' does not have a challenge dispatch "
                "method.".format(challenge=challenge)
            )
        return dispatch[self.challenge_type]()

    def _sms_challenge(self):
        """Executes the SMS challenge."""
        code = generate_mfa_code(bin_key=self.instance.sms_bin_key)
        mfa_settings.SEND_MFA_TEXT_FUNC(
            mfa_instance=self.instance, mfa_code=code)
