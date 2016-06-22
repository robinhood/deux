from __future__ import absolute_import, unicode_literals

from oauth2_provider.views import TokenView

from drf_mfa.oauth2.backends import MFARequestBackend
from drf_mfa.oauth2.validators import MFAOAuth2Validator


class MFATokenView(TokenView):
    """
    class::MFATokenView()

    Extends OAuth's base TokenView to support MFA.
    """

    #: Use DRF_MFA's custom backend for the MFA OAuth api.
    oauthlib_backend_class = MFARequestBackend

    #: Use DRF_MFA's custom validator for the MFA OAuth api.
    validator_class = MFAOAuth2Validator
