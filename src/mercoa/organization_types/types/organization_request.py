# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
import typing_extensions
from ...core.serialization import FieldMetadata
from .payment_methods_request import PaymentMethodsRequest
from .email_provider_request import EmailProviderRequest
from .external_accounting_system_provider_request import (
    ExternalAccountingSystemProviderRequest,
)
from .color_scheme_request import ColorSchemeRequest
from .onboarding_options_request import OnboardingOptionsRequest
from .metadata_schema import MetadataSchema
from .notification_email_template_request import NotificationEmailTemplateRequest
from .role_permission_request import RolePermissionRequest
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class OrganizationRequest(UniversalBaseModel):
    name: typing.Optional[str] = None
    logo: typing.Optional[str] = pydantic.Field(default=None)
    """
    Base64 encoded logo image.
    """

    favicon: typing.Optional[str] = pydantic.Field(default=None)
    """
    Base64 encoded favicon image.
    """

    website_url: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="websiteUrl")] = None
    support_email: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="supportEmail")] = None
    payment_methods: typing_extensions.Annotated[
        typing.Optional[PaymentMethodsRequest], FieldMetadata(alias="paymentMethods")
    ] = None
    email_provider: typing_extensions.Annotated[
        typing.Optional[EmailProviderRequest], FieldMetadata(alias="emailProvider")
    ] = None
    external_accounting_system_provider: typing_extensions.Annotated[
        typing.Optional[ExternalAccountingSystemProviderRequest],
        FieldMetadata(alias="externalAccountingSystemProvider"),
    ] = None
    color_scheme: typing_extensions.Annotated[
        typing.Optional[ColorSchemeRequest], FieldMetadata(alias="colorScheme")
    ] = None
    payee_onboarding_options: typing_extensions.Annotated[
        typing.Optional[OnboardingOptionsRequest],
        FieldMetadata(alias="payeeOnboardingOptions"),
    ] = None
    payor_onboarding_options: typing_extensions.Annotated[
        typing.Optional[OnboardingOptionsRequest],
        FieldMetadata(alias="payorOnboardingOptions"),
    ] = None
    metadata_schema: typing_extensions.Annotated[
        typing.Optional[typing.List[MetadataSchema]],
        FieldMetadata(alias="metadataSchema"),
    ] = None
    notification_email_template: typing_extensions.Annotated[
        typing.Optional[NotificationEmailTemplateRequest],
        FieldMetadata(alias="notificationEmailTemplate"),
    ] = None
    custom_domains: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="customDomains")
    ] = None
    role_permissions: typing_extensions.Annotated[
        typing.Optional[RolePermissionRequest], FieldMetadata(alias="rolePermissions")
    ] = None
    notifications_disabled: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="notificationsDisabled")
    ] = pydantic.Field(default=None)
    """
    If true, all notifications for this organization will be disabled.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
