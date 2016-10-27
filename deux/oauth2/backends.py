from __future__ import absolute_import, unicode_literals

import sys
from oauth2_provider.oauth2_backends import OAuthLibCore

from rest_framework.request import Request as DRFRequest
from rest_framework.views import APIView

if sys.version_info < (3,):
    from urlparse import parse_qs
else:
    from urllib.parse import parse_qs


class MFARequestBackend(OAuthLibCore):
    """
    class::MFARequestBackend()

    OAuth2 backend class for MFA extending ``JSONOAuthLibCore``. It extracts
    extra credentials (``mfa_code`` and ``backup_code``) from the request body.
    """

    def extract_body(self, request):
        """
        Extract request body by coercing the request to a Django Rest
        Framework Request.

        :params request: The request to extract the body from.
        :returns: Returns the items in the requests body.
        """
        if not isinstance(request, DRFRequest):
            request = APIView().initialize_request(request)
        # our custom authorization view is already using DRF
        return request.data.items() if request.data else []

    def _get_extra_credentials(self, body):
        """
        Gets dictionary of ``mfa_code`` and ``backup_code`` from the body.

        :param body: The request body in url encoded form.
        :returns: Dictionary with ``mfa_code`` and ``backup_code``.
        """
        params = {key: value[0] for key, value in parse_qs(body).items()}
        return {
            "mfa_code": params.get("mfa_code"),
            "backup_code": params.get("backup_code"),
        }

    def create_token_response(self, request):
        """
        Overrides the base method to pass in the request body instead of the
        request because Django only allows the request data stream to be read
        once.

        :param request: The request to create a token response from.
        :returns: The redirect uri, headers, body, and status of the response.
        """
        uri, http_method, body, headers = self._extract_params(request)
        extra_credentials = self._get_extra_credentials(body)

        headers, body, status = self.server.create_token_response(
            uri, http_method, body, headers, extra_credentials)
        uri = headers.get("Location", None)
        return uri, headers, body, status
