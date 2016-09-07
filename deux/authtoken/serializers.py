from __future__ import absolute_import, unicode_literals

from django.utils.encoding import force_text
from rest_framework import serializers
from rest_framework.authtoken.serializers import AuthTokenSerializer

from deux import strings
from deux.services import MultiFactorChallenge, verify_mfa_code


class MFAAuthTokenSerializer(AuthTokenSerializer):
    """
    class::MFAAuthTokenSerializer()

    This extends the ``AuthTokenSerializer`` to support multifactor
    authentication.
    """

    #: Serializer field for MFA code field.
    mfa_code = serializers.CharField(required=False)

    #: Serializer field for Backup code.
    backup_code = serializers.CharField(required=False)

    def validate(self, attrs):
        """
        Extends the AuthTokenSerializer validate method to implement multi
        factor authentication.

        If MFA is disabled, authentication requires just a username and
        password.

        If MFA is enabled, authentication requires a username, password,
        and either a MFA code or a backup code. If the request only provides
        the username and password, the server will generate an appropriate
        challenge and respond with `mfa_required = True`.

        Upon using a backup code to authenticate, MFA will be disabled.

        :param attrs: Dictionary of data inputted by the user.
        :raises serializers.ValidationError: If invalid MFA code or backup code
            are submitted. Also if both types of code are submitted
            simultaneously.
        """
        attrs = super(MFAAuthTokenSerializer, self).validate(attrs)
        # User must exist if super method didn't throw error.
        user = attrs["user"]
        assert user is not None, "User should exist after super call."

        mfa = getattr(user, "multi_factor_auth", None)

        if mfa and mfa.enabled:
            mfa_code = attrs.get("mfa_code")
            backup_code = attrs.get("backup_code")

            if mfa_code and backup_code:
                raise serializers.ValidationError(
                    force_text(strings.BOTH_CODES_ERROR))
            elif mfa_code:
                bin_key = mfa.get_bin_key(mfa.challenge_type)
                if not verify_mfa_code(bin_key, mfa_code):
                    raise serializers.ValidationError(
                        force_text(strings.INVALID_MFA_CODE_ERROR))
            elif backup_code:
                if not mfa.check_and_use_backup_code(backup_code):
                    raise serializers.ValidationError(
                        force_text(strings.INVALID_BACKUP_CODE_ERROR))
            else:
                challenge = MultiFactorChallenge(mfa, mfa.challenge_type)
                challenge.generate_challenge()
                attrs["mfa_required"] = True
                attrs["mfa_type"] = mfa.challenge_type
        return attrs
