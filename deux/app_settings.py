from __future__ import absolute_import, unicode_literals

import importlib
import six

from django.conf import settings


USER_SETTINGS = getattr(settings, 'DEUX', None)

DEFAULTS = {
    "BACKUP_CODE_DIGITS": 12,
    "MFA_CODE_NUM_DIGITS": 6,
    "MFA_MODEL": "deux.models.MultiFactorAuth",
    "SEND_MFA_TEXT_FUNC": "deux.notifications.send_mfa_code_text_message",
    "STEP_SIZE": 30,
    "TWILIO_ACCOUNT_SID": "",
    "TWILIO_AUTH_TOKEN": "",
    "TWILIO_SMS_POOL_SID": "",
}

# List of settings that cannot be empty.
MANDATORY = ()

# List of settings that may be in string import notation.
IMPORT_STRINGS = (
    'MFA_MODEL',
    'SEND_MFA_TEXT_FUNC',
)


def perform_import(val, setting_name):

    if isinstance(val, six.string_types):
        return import_from_string(val, setting_name)
    elif isinstance(val, (list, tuple)):
        return [import_from_string(item, setting_name) for item in val]
    return val


def import_from_string(val, setting_name):

    try:
        parts = val.split('.')
        module_path, class_name = '.'.join(parts[:-1]), parts[-1]
        module = importlib.import_module(module_path)
        return getattr(module, class_name)
    except ImportError:
        msg = "Coud not import {val} for setting {setting_name}".format(
            val=val, setting_name=setting_name)
        raise ImportError(msg)


class MFASettings(object):

    def __init__(self, user_settings=None, defaults=None, import_strings=None,
                 mandatory=None):
        self.user_settings = user_settings or {}
        self.defaults = defaults or {}
        self.import_strings = import_strings or ()
        self.mandatory = mandatory or ()

    def __getattr__(self, attr):
        if attr not in self.defaults.keys():
            raise AttributeError("Invalid deux setting: '%s'" % attr)

        try:
            # Check if present in user settings
            val = self.user_settings[attr]
        except KeyError:
            # Fall back to defaults
            val = self.defaults[attr]

        # Coerce import strings into classes
        if val and attr in self.import_strings:
            val = perform_import(val, attr)

        self.validate_setting(attr, val)

        # Cache the result
        setattr(self, attr, val)
        return val

    def validate_setting(self, attr, val):
        if not val and attr in self.mandatory:
            raise AttributeError("deux setting: '%s' is mandatory" % attr)


mfa_settings = MFASettings(USER_SETTINGS, DEFAULTS, IMPORT_STRINGS, MANDATORY)
