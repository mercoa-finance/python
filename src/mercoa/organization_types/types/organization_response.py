# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
from .organization_id import OrganizationId
import typing_extensions
import typing
from ...core.serialization import FieldMetadata
from .payment_methods_response import PaymentMethodsResponse
from .email_provider_response import EmailProviderResponse
from .external_accounting_system_provider_response import (
    ExternalAccountingSystemProviderResponse,
)
from .color_scheme_response import ColorSchemeResponse
from .onboarding_options_response import OnboardingOptionsResponse
from .metadata_schema import MetadataSchema
from .notification_email_template_response import NotificationEmailTemplateResponse
from ...entity_types.types.entity_id import EntityId
from .role_permission_response import RolePermissionResponse
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class OrganizationResponse(UniversalBaseModel):
    id: OrganizationId
    sandbox: bool
    name: str
    logo_url: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="logoUrl")] = None
    website_url: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="websiteUrl")] = None
    support_email: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="supportEmail")] = None
    payment_methods: typing_extensions.Annotated[
        typing.Optional[PaymentMethodsResponse], FieldMetadata(alias="paymentMethods")
    ] = None
    email_provider: typing_extensions.Annotated[
        typing.Optional[EmailProviderResponse], FieldMetadata(alias="emailProvider")
    ] = None
    external_accounting_system_provider: typing_extensions.Annotated[
        typing.Optional[ExternalAccountingSystemProviderResponse],
        FieldMetadata(alias="externalAccountingSystemProvider"),
    ] = None
    color_scheme: typing_extensions.Annotated[
        typing.Optional[ColorSchemeResponse], FieldMetadata(alias="colorScheme")
    ] = None
    payee_onboarding_options: typing_extensions.Annotated[
        typing.Optional[OnboardingOptionsResponse],
        FieldMetadata(alias="payeeOnboardingOptions"),
    ] = None
    payor_onboarding_options: typing_extensions.Annotated[
        typing.Optional[OnboardingOptionsResponse],
        FieldMetadata(alias="payorOnboardingOptions"),
    ] = None
    metadata_schema: typing_extensions.Annotated[
        typing.Optional[typing.List[MetadataSchema]],
        FieldMetadata(alias="metadataSchema"),
    ] = None
    notification_email_template: typing_extensions.Annotated[
        typing.Optional[NotificationEmailTemplateResponse],
        FieldMetadata(alias="notificationEmailTemplate"),
    ] = None
    custom_domains: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="customDomains")
    ] = None
    organization_entity_id: typing_extensions.Annotated[
        typing.Optional[EntityId], FieldMetadata(alias="organizationEntityId")
    ] = None
    role_permissions: typing_extensions.Annotated[
        typing.Optional[RolePermissionResponse], FieldMetadata(alias="rolePermissions")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
