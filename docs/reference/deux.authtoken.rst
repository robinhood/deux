=====================================================
 deux.authtoken
=====================================================

.. currentmodule:: deux.authtoken

.. automodule:: deux.authtoken
    :members:
    :undoc-members:


POST /mfa/authtoken/login/
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Expected Request**

    .. code-block:: none

        {
            "username": "testuser",
            "password": "mypassword",
            "mfa_code": "123456", (Optional)
            "backup_code": "123456789012" (Optional)
        }

**Expected Response if Authenticated**

    .. code-block:: none

        200 OK
        {
            "token": "<token>",
        }

**Expected Response if MFA Required**

    .. code-block:: none

        200 OK
        {
            "mfa_required": True,
            "mfa_type": "sms"
        }
