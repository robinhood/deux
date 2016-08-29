=====================================================
 deux.oauth2
=====================================================

.. currentmodule:: deux.oauth2

.. automodule:: deux.oauth2
    :members:
    :undoc-members:


POST /mfa/oauth2/token/
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Expected Request**

    .. code-block:: none

        {
            "grant_type": "password"
            "username": "testuser",
            "password": "mypassword",
            "mfa_code": "123456", (Optional)
            "backup_code": "123456789012" (Optional)
        }

**Expected Response if Authenticated**

    .. code-block:: none

        200 OK
        {
            "access_token": "<token>",
            "expires_in": "<seconds>",
            "token_type": "Bearer",
            "scope": "<scope>",
            "refresh_token": "<token>"
        }

**Expected Response if MFA Required**

    .. code-block:: none

        200 OK
        {
            "mfa_required": True,
            "mfa_type": "sms"
        }
