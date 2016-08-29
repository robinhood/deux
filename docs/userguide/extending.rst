.. _custom-guide:

=============================================================================
                                Extending
=============================================================================

Notifications
=============

The send SMS function can be directly overridden by a custom function. You can
configure the function in your ``SEND_MFA_TEXT_FUNC`` setting.

Your SMS function should throw :class:`deux.exceptions.FailedChallengeError` for any errors to be caught by this library's functions.

Your function can look something like this:

    .. code-block:: python

        def custom_send_function(mfa_instance, mfa_code):
            ...

To use the function, in your ``settings.py``:

    .. code-block:: python

        DEUX = {
            ...
            "SEND_MFA_TEXT_FUNC": "<module_path>.custom_send_function",
        }


Models
======

You can write your own custom model that extends :class:`deux.abstract_models.AbstractMultiFactorAuth` and configure the model in your ``MFA_MODEL`` setting.

Your model can look something like this:

    .. code-block:: python

        class CustomMultiFactorAuth(AbstractMultiFactorAuth):
            ...

To use the function, in your ``settings.py``:

    .. code-block:: python

        DEUX = {
            ...
            "MFA_MODEL": "<module_path>.CustomMultiFactorAuth",
        }


Authentication Protocols
========================

Currently, the package supports ``authtoken`` and ``oauth2``. You can easily
extend the package to support your authentication protocol of choice.

Create a new sub-directory under the main application for your authentication and
create a new login endpoint that follows the same two factor login protocol as
the rest of the package.

Register your new endpoint in the ``test_proj/urls.py`` file like this:

    .. code-block:: python

        url(r"^mfa/<protocol>/",
            include("deux.<protocol>.urls", namespace="<protocol>"),
        ),

Look at :class:`deux.authtoken` or :class:`deux.oauth2` for examples.


Challenge Methods
=================

Currently, the package supports two factor over text message. However, it is easy to add your own challenge method for two factor (i.e. Google Authenticator or email).

Create a new challenge type in :class:`deux.constants`.

    .. code-block:: python

        YOUR_CHALLENGE_METHOD = "<Your challenge method.>"

        CHALLENGE_TYPES = (SMS, YOUR_CHALLENGE_METHOD)


Then, add a new challenge method to the :class:`deux.services.MultiFactorChallenge` class.

    .. code-block:: python

        class MultiFactorChallenge(object):
            ...

            def generate_challenge(self):
                """
                Generates and executes the challenge object based on the challenge
                type of this object.
                """
                dispatch = {
                    SMS: self._sms_challenge,
                    YOUR_CHALLENGE_METHOD: self._your_challenge_method,
                }

            ...

            def _your_challenge_method(self):
                """Executes your challenge method."""
                ...


Then, add the necessary endpoints around requesting and verifying Two Factor with this challenge method.

    .. code-block:: python

        url(r"^your_challenge_method/request/$",
            views.YourChallengeMethodRequestDetail.as_view(),
            name="your_challenge_method_request-detail"
        ),
        url(r"^your_challenge_method/verify/$",
            views.YourChallengeMethodVerifyDetail.as_view(),
            name="your_challenge_method_verify-detail"
        ),
        url(r"^sms/verify/$", views.SMSChallengeVerifyDetail.as_view(),
            name="sms_verify-detail"),
