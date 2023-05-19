# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from .account_type import AccountType
from .profile_request import ProfileRequest


class EntityUpdateRequest(pydantic.BaseModel):
    foreign_id: typing.Optional[str] = pydantic.Field(alias="foreignId")
    email_to: typing.Optional[str] = pydantic.Field(
        alias="emailTo", description=("Email inbox address. Do not include the @domain.com\n")
    )
    email_to_alias: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="emailToAlias",
        description=(
            "Email inbox alias addresses. Used when forwarding emails to the emailTo address from an alias. Include the full email address.\n"
        ),
    )
    owned_by_org: typing.Optional[bool] = pydantic.Field(
        alias="ownedByOrg",
        description=(
            "If this entity has a direct relationship with your organization, set this to true. Otherwise, set to false.\n"
        ),
    )
    account_type: typing.Optional[AccountType] = pydantic.Field(alias="accountType")
    profile: typing.Optional[ProfileRequest]
    is_payor: typing.Optional[bool] = pydantic.Field(
        alias="isPayor", description=("If this entity will be paying invoices, set this to true.\n")
    )
    is_payee: typing.Optional[bool] = pydantic.Field(
        alias="isPayee", description=("If this entity will be receiving payments, set this to true.\n")
    )

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
