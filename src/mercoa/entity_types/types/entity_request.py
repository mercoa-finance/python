# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .account_type import AccountType
from .profile_request import ProfileRequest


class EntityRequest(pydantic_v1.BaseModel):
    """
    Examples
    --------
    from mercoa import (
        Address,
        BusinessProfileRequest,
        Ein,
        EntityRequest,
        PhoneNumber,
        ProfileRequest,
        TaxId,
    )

    EntityRequest(
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

    foreign_id: typing.Optional[str] = pydantic_v1.Field(alias="foreignId", default=None)
    """
    The ID used to identify this entity in your system. This ID must be unique across all entities in your system.
    """

    email_to: typing.Optional[str] = pydantic_v1.Field(alias="emailTo", default=None)
    """
    Sets the email address to which to send invoices to be added to the Invoice Inbox. Only provide the local-part/username of the email address, do not include the @domain.com
    """

    email_to_alias: typing.Optional[typing.List[str]] = pydantic_v1.Field(alias="emailToAlias", default=None)
    """
    Email inbox alias addresses. Used when forwarding emails to the emailTo address from an alias. Include the full email address.
    """

    is_customer: bool = pydantic_v1.Field(alias="isCustomer")
    """
    If this entity has a direct relationship with your organization (e.g your direct customer or client), set this to true. Otherwise, set to false (e.g your customer's vendors).
    """

    account_type: AccountType = pydantic_v1.Field(alias="accountType")
    profile: ProfileRequest
    is_payor: bool = pydantic_v1.Field(alias="isPayor")
    """
    If this entity will be paying invoices, set this to true.
    """

    is_payee: bool = pydantic_v1.Field(alias="isPayee")
    """
    If this entity will be receiving payments, set this to true.
    """

    is_network_payor: typing.Optional[bool] = pydantic_v1.Field(alias="isNetworkPayor", default=None)
    """
    Control if this entity should be available as a payor to any entity on your platform. If set to false, this entity will only be available as a payor to entities that have a direct relationship with this entity. Defaults to false.
    """

    is_network_payee: typing.Optional[bool] = pydantic_v1.Field(alias="isNetworkPayee", default=None)
    """
    Control if this entity should be available as a payee to any entity on your platform. If set to false, this entity will only be available as a payee to entities that have a direct relationship with this entity. Defaults to false.
    """

    logo: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Base64 encoded PNG image data for the entity logo. Max size 100KB.
    """

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
