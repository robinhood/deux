.. _django-guide:

=============================================================================
                             DRF Integration
=============================================================================

.. _django-installation:

Setup
=====

.. _guide: http://www.django-rest-framework.org/
.. _INSTALLED_APPS: https://docs.djangoproject.com/en/1.9/ref/settings/#std:setting-INSTALLED_APPS

To set up ``deux`` for your Django Rest Framework application, follow these steps. For help setting up a DRF project, see guide_ here.

#. Install deux.

   .. code-block:: console

        $ pip install deux

#. Add ``deux`` to INSTALLED_APPS_ after ``rest_framework.authtoken``
   and ``oauth2_provider``, depending on which authentication protocol you use.

   .. code-block:: python

        INSTALLED_APPS = (
            # ...,
            'rest_framework.authtoken',
            'oauth2_provider',
            # ...,
            'deux',
        )

#. Migrate your database to add the ``MultiFactorAuth`` model.

    .. code-block:: console

        $ python manage.py migrate

#. Configure your ``settings.py`` file, as described in :ref:`settings`.

.. _api:

Views
=====

The library comes with a standard set of views you can add to your
Django Rest Framework API, that allows your users to enable/disable
multifactor authentication.

To enable them, add the following configuration to your file :file:`urls.py`:

.. code-block:: python

    url(r"^mfa/", include("deux.urls", namespace="mfa")),

The library also provides views for authenticating through multifactor
authentication depending on your authentication protocol.

#. For ``authtoken``, add the following to :file:`urls.py`:

    .. code-block:: python

        url(r"^mfa/authtoken/", include(
            "deux.authtoken.urls", namespace="mfa-authtoken:login")),

#. For ``oauth2``, add the following to :file:`urls.py`:

    .. code-block:: python

        url(r"^mfa/oauth2/", include(
            "deux.oauth2.urls", namespace="mfa-oauth2:login")),

.. _settings:

Settings
========

The library takes the following settings object. The default values are as
followed:

    .. code-block:: python

        DEUX = {
            "BACKUP_CODE_DIGITS": 12,
            "MFA_CODE_NUM_DIGITS": 6,
            "STEP_SIZE": 30,
            "MFA_MODEL": "deux.models.MultiFactorAuth",
            "SEND_MFA_TEXT_FUNC": "deux.notifications.send_mfa_code_text_message",
            "TWILIO_ACCOUNT_SID": "",
            "TWILIO_AUTH_TOKEN": "",
            "TWILIO_PHONE_NUMBER": "",
        }

MFA Optional Settings
---------------------

#. ``BACKUP_CODE_DIGITS``: The length of multifactor backup code.

    - **Default**: ``12``

#. ``MFA_CODE_NUM_DIGITS``: The length of a multifactor authentication code.

    - **Default**: ``6``

#. ``STEP_SIZE``: The length of an authentication window in seconds.

    - **Usage**: An authentication code is valid for 3 windows: the window in which the code is generated, the window before, and the window after.
    - **Default**: ``6``

#. ``MFA_MODEL``: The model used for multifactor authentication

    - **Default**: ``models.MultiFactorAuth``
    - **Descrtiption**: The default model is a blank extension of
      ``abstract_models.AbstractMultiFactorAuth``

Twilio Driver Settings
----------------------

#. ``SEND_MFA_TEXT_FUNC``: The function used for sending text messages to users.

    - **Default**: ``deux.notifications.send_mfa_code_text_message``

If you use our default Twilio driver, you must also include your Twilio
credentials in the settings object.

    #. ``TWILIO_ACCOUNT_SID``: Your Twilio account's SID.

    #. ``TWILIO_AUTH_TOKEN``: Your Twilio account's authentication token.

    #. ``TWILIO_PHONE_NUMBER``: Your Twilio account's phone number.
