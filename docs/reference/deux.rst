=====================================================
 deux
=====================================================

.. currentmodule:: deux

.. automodule:: deux
    :members:
    :undoc-members:

GET /mfa/
~~~~~~~~~

**Sample Response**

    .. code-block:: none

        200 OK
        {
            "enabled": True or False,
            "challenge_type": "sms"
            "phone_number": "14085862744"
        }

DELETE /mfa/
~~~~~~~~~~~~

**Expected Response**

    .. code-block:: none

        204 NO CONTENT

PUT /mfa/sms/request/
~~~~~~~~~~~~~~~~~~~~~

**Expected Request**

    .. code-block:: none

        {
            "phone_number": "14085862744"
        }

**Expected Response**

    .. code-block:: none

        200 OK
        {
            "enabled":  False,
            "challenge_type": ""
            "phone_number": "14085862744"
        }

PUT /mfa/sms/verify/
~~~~~~~~~~~~~~~~~~~~

**Expected Request**

    .. code-block:: none

        {
            "mfa_code": "123456"
        }

**Expected Response**

    .. code-block:: none

        200 OK
        {
            "enabled":  True,
            "challenge_type": "sms"
            "phone_number": "14085862744"
        }

GET /mfa/recovery/
~~~~~~~~~~~~~~~~~~

**Expected Response**

    .. code-block:: none

        200 OK
        {
            "backup_code: "123456789012"
        }
