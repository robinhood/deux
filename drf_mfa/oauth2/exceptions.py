from __future__ import absolute_import, unicode_literals

from oauthlib.oauth2 import OAuth2Error

from rest_framework import status


class InvalidLoginError(OAuth2Error):
    """
    Generic exception for a failed login attempt through OAuth2. This exception
    will result in a 400 Bad Request error in the OAuth API.
    """

    def __init__(self, error_msg):
        """
        Initializes this error with the given error message.

        :param error_msg: The error message describing this exception.
        """
        self.error_msg = error_msg

    @property
    def twotuples(self):
        """
        Returns a list of tuples that will be converted to the error response.
        This method override the ``two_tuples`` method from ``OAuth2Error``.
        """
        return [("detail", self.error_msg)]


class ChallengeRequiredMessage(OAuth2Error):
    """
    This exception is used to prompt the user for an MFA code.

    This exception is used when a user passes in their username and password,
    and they have MFA enabled.
    """

    #: This exception returns a 200 response.
    status_code = status.HTTP_200_OK

    def __init__(self, challenge_type):
        """
        Initalizes this exception class with a challenge type.

        :param challenge_type: The challenge type the user should expect.
        """
        self.challenge_type = challenge_type

    @property
    def twotuples(self):
        """
        Returns a list of tuples that will be converted to the error response.
        This method override the ``two_tuples`` method from ``OAuth2Error``.
        """
        return [
            ("mfa_required", True),
            ("mfa_type", self.challenge_type),
        ]
