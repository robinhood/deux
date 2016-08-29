from __future__ import absolute_import, unicode_literals

from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated

from deux import strings
from deux.app_settings import mfa_settings
from deux.constants import SMS
from deux.serializers import (
    BackupCodeSerializer,
    MultiFactorAuthSerializer,
    SMSChallengeRequestSerializer,
    SMSChallengeVerifySerializer,
)


class MultiFactorAuthMixin(object):
    """
    class::MultiFactorAuthMixin()

    Mixin that defines queries for MFA objects.
    """

    def get_object(self):
        """Gets the current user's MFA instance"""
        instance, created = mfa_settings.MFA_MODEL.objects.get_or_create(
            user=self.request.user)
        return instance


class MultiFactorAuthDetail(
        MultiFactorAuthMixin, generics.RetrieveDestroyAPIView):
    """
    class::MultiFactorAuthDetail()

    View for requesting data about MultiFactorAuth and disabling MFA.
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = MultiFactorAuthSerializer

    def perform_destroy(self, instance):
        """
        The delete method should disable MFA for this user.

        :raises rest_framework.exceptions.ValidationError: If MFA is not
            enabled.
        """
        if not instance.enabled:
            raise ValidationError({
                "detail": strings.DISABLED_ERROR
            })
        instance.disable()


class _BaseChallengeView(MultiFactorAuthMixin, generics.UpdateAPIView):
    """
    class::_BaseChallengeView()

    Base view for different challenges.
    """
    permission_classes = (IsAuthenticated,)

    @property
    def challenge_type(self):
        """
        Represents the challenge type this serializer represents.

        :raises NotImplemented: If the extending class does not define
            ``challenge_type``.
        """
        raise NotImplemented  # pragma: no cover


class SMSChallengeRequestDetail(_BaseChallengeView):
    """
    class::SMSChallengeRequestDetail()

    View for requesting SMS challenges to enable MFA through SMS.
    """
    challenge_type = SMS
    serializer_class = SMSChallengeRequestSerializer


class SMSChallengeVerifyDetail(_BaseChallengeView):
    """
    class::SMSChallengeVerifyDetail()

    View for verify SMS challenges to enable MFA through SMS.
    """
    challenge_type = SMS
    serializer_class = SMSChallengeVerifySerializer


class BackupCodeDetail(MultiFactorAuthMixin, generics.RetrieveAPIView):
    """
    class::BackupCodeDetail()

    View for retrieving the user's backup code.
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = BackupCodeSerializer
