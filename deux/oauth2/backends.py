from __future__ import absolute_import, unicode_literals

import json

from oauth2_provider.oauth2_backends import JSONOAuthLibCore


class MFARequestBackend(JSONOAuthLibCore):
    """
    class::MFARequestBackend()

    OAuth2 backend class for MFA extending ``JSONOAuthLibCore``. It extracts
    extra credentials (``mfa_code`` and ``backup_code``) from the request body.
    """

    def _get_extra_credentials(self, request):
        """
        Gets dictionary of ``mfa_code`` and ``backup_code`` from the request.

        :param request: The API request to this MFA backend class.
        :returns: Dictionary with ``mfa_code`` and ``backup_code``.
        """
        body = json.loads(request.body.decode("utf-8"))
        return {
            "mfa_code": body.get("mfa_code"),
            "backup_code": body.get("backup_code"),
        }
