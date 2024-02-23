# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .account_type import AccountType
from .profile_request import ProfileRequest

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class EntityUpdateRequest(pydantic.BaseModel):
    foreign_id: typing.Optional[str] = pydantic.Field(
        alias="foreignId",
        default=None,
        description="The ID used to identify this entity in your system. This ID must be unique across all entities in your system.",
    )
    email_to: typing.Optional[str] = pydantic.Field(
        alias="emailTo",
        default=None,
        description="Sets the email address to which to send invoices to be added to the Invoice Inbox. Only provide the local-part/username of the email address, do not include the @domain.com",
    )
    email_to_alias: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="emailToAlias",
        default=None,
        description="Email inbox alias addresses. Used when forwarding emails to the emailTo address from an alias. Include the full email address.",
    )
    is_customer: typing.Optional[bool] = pydantic.Field(
        alias="isCustomer",
        default=None,
        description="If this entity has a direct relationship with your organization (e.g your direct customer or client), set this to true. Otherwise, set to false (e.g your customer's vendors).",
    )
    account_type: typing.Optional[AccountType] = pydantic.Field(alias="accountType", default=None)
    profile: typing.Optional[ProfileRequest] = None
    is_payor: typing.Optional[bool] = pydantic.Field(
        alias="isPayor", default=None, description="If this entity will be paying invoices, set this to true."
    )
    is_payee: typing.Optional[bool] = pydantic.Field(
        alias="isPayee", default=None, description="If this entity will be receiving payments, set this to true."
    )
    logo: typing.Optional[str] = pydantic.Field(
        default=None, description="Base64 encoded PNG image data for the entity logo."
    )

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
