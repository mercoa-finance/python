# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .account_type import AccountType
from .entity_id import EntityId
from .entity_status import EntityStatus
from .profile_response import ProfileResponse


class EntityResponse(pydantic_v1.BaseModel):
    """
    Examples
    --------
    import datetime

    from mercoa import (
        Address,
        BusinessProfileResponse,
        EntityResponse,
        PhoneNumber,
        ProfileResponse,
    )

    EntityResponse(
        id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
        foreign_id="MY-DB-ID-12345",
        name="Acme Inc.",
        email="customer@acme.com",
        accepted_tos=True,
        status="verified",
        is_customer=True,
        is_payor=True,
        is_payee=False,
        is_network_payor=False,
        is_network_payee=False,
        account_type="business",
        updated_at=datetime.datetime.fromisoformat(
            "2024-01-02 00:00:00+00:00",
        ),
        created_at=datetime.datetime.fromisoformat(
            "2024-01-01 00:00:00+00:00",
        ),
        profile=ProfileResponse(
            business=BusinessProfileResponse(
                email="customer@acme.com",
                legal_business_name="Acme Inc.",
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
                tax_id_provided=True,
                owners_provided=True,
            ),
        ),
    )
    """

    id: EntityId
    name: str
    email: str
    foreign_id: typing.Optional[str] = pydantic_v1.Field(alias="foreignId", default=None)
    """
    The ID used to identify this entity in your system
    """

    email_to: typing.Optional[str] = pydantic_v1.Field(alias="emailTo", default=None)
    """
    Local-part/username of the email address to which to send invoices to be added to the Invoice Inbox.
    """

    email_to_alias: typing.Optional[typing.List[str]] = pydantic_v1.Field(alias="emailToAlias", default=None)
    """
    Email inbox alias addresses. Used when forwarding emails to the emailTo address from an alias.
    """

    is_customer: bool = pydantic_v1.Field(alias="isCustomer")
    """
    True if this entity has a direct relationship with your organization.
    """

    account_type: AccountType = pydantic_v1.Field(alias="accountType")
    profile: ProfileResponse
    status: EntityStatus
    accepted_tos: bool = pydantic_v1.Field(alias="acceptedTos")
    """
    True if this entity has accepted the terms of service.
    """

    is_payor: bool = pydantic_v1.Field(alias="isPayor")
    """
    True if this entity can pay invoices.
    """

    is_payee: bool = pydantic_v1.Field(alias="isPayee")
    """
    True if this entity can receive payments.
    """

    is_network_payor: bool = pydantic_v1.Field(alias="isNetworkPayor")
    """
    True if this entity is available as a payor to any entity on your platform. Otherwise this entity will only be available as a payor to entities that have a direct relationship with this entity.
    """

    is_network_payee: bool = pydantic_v1.Field(alias="isNetworkPayee")
    """
    True if this entity is available as a payee to any entity on your platform. Otherwise this entity will only be available as a payee to entities that have a direct relationship with this entity.
    """

    created_at: dt.datetime = pydantic_v1.Field(alias="createdAt")
    updated_at: dt.datetime = pydantic_v1.Field(alias="updatedAt")

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
