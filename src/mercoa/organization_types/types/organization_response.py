# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
from .organization_id import OrganizationId
import typing
import pydantic
from .payment_methods_response import PaymentMethodsResponse
from .email_provider_response import EmailProviderResponse
from .external_accounting_system_provider_response import ExternalAccountingSystemProviderResponse
from .color_scheme_response import ColorSchemeResponse
from .onboarding_options_response import OnboardingOptionsResponse
from .metadata_schema import MetadataSchema
from .notification_email_template_response import NotificationEmailTemplateResponse
from ...entity_types.types.entity_id import EntityId
from .role_permission_response import RolePermissionResponse
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class OrganizationResponse(UniversalBaseModel):
    id: OrganizationId
    sandbox: bool
    name: str
    logo_url: typing.Optional[str] = pydantic.Field(alias="logoUrl", default=None)
    website_url: typing.Optional[str] = pydantic.Field(alias="websiteUrl", default=None)
    support_email: typing.Optional[str] = pydantic.Field(alias="supportEmail", default=None)
    payment_methods: typing.Optional[PaymentMethodsResponse] = pydantic.Field(alias="paymentMethods", default=None)
    email_provider: typing.Optional[EmailProviderResponse] = pydantic.Field(alias="emailProvider", default=None)
    external_accounting_system_provider: typing.Optional[ExternalAccountingSystemProviderResponse] = pydantic.Field(
        alias="externalAccountingSystemProvider", default=None
    )
    color_scheme: typing.Optional[ColorSchemeResponse] = pydantic.Field(alias="colorScheme", default=None)
    payee_onboarding_options: typing.Optional[OnboardingOptionsResponse] = pydantic.Field(
        alias="payeeOnboardingOptions", default=None
    )
    payor_onboarding_options: typing.Optional[OnboardingOptionsResponse] = pydantic.Field(
        alias="payorOnboardingOptions", default=None
    )
    metadata_schema: typing.Optional[typing.List[MetadataSchema]] = pydantic.Field(alias="metadataSchema", default=None)
    notification_email_template: typing.Optional[NotificationEmailTemplateResponse] = pydantic.Field(
        alias="notificationEmailTemplate", default=None
    )
    custom_domains: typing.Optional[typing.List[str]] = pydantic.Field(alias="customDomains", default=None)
    organization_entity_id: typing.Optional[EntityId] = pydantic.Field(alias="organizationEntityId", default=None)
    role_permissions: typing.Optional[RolePermissionResponse] = pydantic.Field(alias="rolePermissions", default=None)

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
