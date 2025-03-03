# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ...core.serialization import FieldMetadata
import pydantic
from .account_type import AccountType
from .profile_request import ProfileRequest
from .entity_id import EntityId
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class EntityUpdateRequest(UniversalBaseModel):
    """
    Examples
    --------
    from mercoa.commons import Address, PhoneNumber
    from mercoa.entity_types import (
        BusinessProfileRequest,
        Ein,
        EntityUpdateRequest,
        ProfileRequest,
        TaxId,
    )

    EntityUpdateRequest(
        is_customer=True,
        is_payor=True,
        is_payee=False,
        account_type="business",
        foreign_id="MY-DB-ID-12345",
        profile=ProfileRequest(
            business=BusinessProfileRequest(
                email="customer@acme.com",
                legal_business_name="Acme Inc.",
                website="http://www.acme.com",
                business_type="llc",
                phone=PhoneNumber(
                    country_code="1",
                    number="4155551234",
                ),
                address=Address(
                    address_line_1="123 Main St",
                    address_line_2="Unit 1",
                    city="San Francisco",
                    state_or_province="CA",
                    postal_code="94105",
                    country="US",
                ),
                tax_id=TaxId(
                    ein=Ein(
                        number="12-3456789",
                    ),
                ),
            ),
        ),
    )
    """

    foreign_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="foreignId")] = pydantic.Field(
        default=None
    )
    """
    The ID used to identify this entity in your system. This ID must be unique across all entities in your system.
    """

    email_to: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="emailTo")] = pydantic.Field(
        default=None
    )
    """
    Sets the email address to which to send invoices to be added to the Invoice Inbox. Only provide the local-part/username of the email address, do not include the @domain.com
    """

    email_to_alias: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="emailToAlias")
    ] = pydantic.Field(default=None)
    """
    Email inbox alias addresses. Used when forwarding emails to the emailTo address from an alias. Include the full email address.
    """

    is_customer: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="isCustomer")] = pydantic.Field(
        default=None
    )
    """
    If this entity has a direct relationship with your organization (e.g your direct customer or client), set this to true. Otherwise, set to false (e.g your customer's vendors).
    """

    account_type: typing_extensions.Annotated[typing.Optional[AccountType], FieldMetadata(alias="accountType")] = None
    profile: typing.Optional[ProfileRequest] = None
    is_payor: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="isPayor")] = pydantic.Field(
        default=None
    )
    """
    If this entity will be paying invoices, set this to true.
    """

    is_payee: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="isPayee")] = pydantic.Field(
        default=None
    )
    """
    If this entity will be receiving payments, set this to true.
    """

    is_network_payor: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="isNetworkPayor")] = (
        pydantic.Field(default=None)
    )
    """
    Control if this entity should be available as a payor to any entity on your platform. If set to false, this entity will only be available as a payor to entities that have a direct relationship with this entity. Defaults to false.
    """

    is_network_payee: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="isNetworkPayee")] = (
        pydantic.Field(default=None)
    )
    """
    Control if this entity should be available as a payee to any entity on your platform. If set to false, this entity will only be available as a payee to entities that have a direct relationship with this entity. Defaults to false.
    """

    logo: typing.Optional[str] = pydantic.Field(default=None)
    """
    Base64 data URL of the entity logo. Must be in the `data:image/*;base64,XXXX` format. We recommend a PNG image under 100KB. Supported file types are `png`, `jpeg`, `gif`, `svg`.
    """

    metadata: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    Simple key/value metadata associated with this entity. For more complex metadata, use the Metadata API.
    """

    connected_entity_id: typing_extensions.Annotated[
        typing.Optional[EntityId], FieldMetadata(alias="connectedEntityId")
    ] = pydantic.Field(default=None)
    """
    The ID of the entity that this entity is connected to. This is used to trigger notifications to the connected entity when this entity is updated.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
