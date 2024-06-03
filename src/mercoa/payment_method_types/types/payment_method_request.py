# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .bank_account_check_options import BankAccountCheckOptions
from .bank_type import BankType
from .card_brand import CardBrand
from .card_type import CardType
from .custom_payment_method_schema_id import CustomPaymentMethodSchemaId
from .plaid_link_request import PlaidLinkRequest


class PaymentMethodRequest_BankAccount(pydantic_v1.BaseModel):
    """
    Examples
    --------
    from mercoa import PaymentMethodRequest_BankAccount

    PaymentMethodRequest_BankAccount(
        routing_number="12345678",
        account_number="99988767623",
        account_type="CHECKING",
    )
    """

    account_name: typing.Optional[str] = pydantic_v1.Field(alias="accountName", default=None)
    bank_name: typing.Optional[str] = pydantic_v1.Field(alias="bankName", default=None)
    routing_number: str = pydantic_v1.Field(alias="routingNumber")
    account_number: str = pydantic_v1.Field(alias="accountNumber")
    account_type: BankType = pydantic_v1.Field(alias="accountType")
    plaid: typing.Optional[PlaidLinkRequest] = None
    check_options: typing.Optional[BankAccountCheckOptions] = pydantic_v1.Field(alias="checkOptions", default=None)
    default_source: typing.Optional[bool] = pydantic_v1.Field(alias="defaultSource", default=None)
    default_destination: typing.Optional[bool] = pydantic_v1.Field(alias="defaultDestination", default=None)
    type: typing.Literal["bankAccount"] = "bankAccount"

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


class PaymentMethodRequest_Card(pydantic_v1.BaseModel):
    """
    Examples
    --------
    from mercoa import PaymentMethodRequest_BankAccount

    PaymentMethodRequest_BankAccount(
        routing_number="12345678",
        account_number="99988767623",
        account_type="CHECKING",
    )
    """

    card_type: CardType = pydantic_v1.Field(alias="cardType")
    card_brand: CardBrand = pydantic_v1.Field(alias="cardBrand")
    last_four: str = pydantic_v1.Field(alias="lastFour")
    exp_month: str = pydantic_v1.Field(alias="expMonth")
    exp_year: str = pydantic_v1.Field(alias="expYear")
    token: str
    default_source: typing.Optional[bool] = pydantic_v1.Field(alias="defaultSource", default=None)
    default_destination: typing.Optional[bool] = pydantic_v1.Field(alias="defaultDestination", default=None)
    type: typing.Literal["card"] = "card"

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


class PaymentMethodRequest_Check(pydantic_v1.BaseModel):
    """
    Examples
    --------
    from mercoa import PaymentMethodRequest_BankAccount

    PaymentMethodRequest_BankAccount(
        routing_number="12345678",
        account_number="99988767623",
        account_type="CHECKING",
    )
    """

    pay_to_the_order_of: str = pydantic_v1.Field(alias="payToTheOrderOf")
    address_line_1: str = pydantic_v1.Field(alias="addressLine1")
    address_line_2: typing.Optional[str] = pydantic_v1.Field(alias="addressLine2", default=None)
    city: str
    state_or_province: str = pydantic_v1.Field(alias="stateOrProvince")
    postal_code: str = pydantic_v1.Field(alias="postalCode")
    country: str
    default_source: typing.Optional[bool] = pydantic_v1.Field(alias="defaultSource", default=None)
    default_destination: typing.Optional[bool] = pydantic_v1.Field(alias="defaultDestination", default=None)
    type: typing.Literal["check"] = "check"

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


class PaymentMethodRequest_Custom(pydantic_v1.BaseModel):
    """
    Examples
    --------
    from mercoa import PaymentMethodRequest_BankAccount

    PaymentMethodRequest_BankAccount(
        routing_number="12345678",
        account_number="99988767623",
        account_type="CHECKING",
    )
    """

    foreign_id: str = pydantic_v1.Field(alias="foreignId")
    account_name: typing.Optional[str] = pydantic_v1.Field(alias="accountName", default=None)
    account_number: typing.Optional[str] = pydantic_v1.Field(alias="accountNumber", default=None)
    schema_id: CustomPaymentMethodSchemaId = pydantic_v1.Field(alias="schemaId")
    data: typing.Dict[str, str]
    default_source: typing.Optional[bool] = pydantic_v1.Field(alias="defaultSource", default=None)
    default_destination: typing.Optional[bool] = pydantic_v1.Field(alias="defaultDestination", default=None)
    type: typing.Literal["custom"] = "custom"

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


class PaymentMethodRequest_OffPlatform(pydantic_v1.BaseModel):
    """
    Examples
    --------
    from mercoa import PaymentMethodRequest_BankAccount

    PaymentMethodRequest_BankAccount(
        routing_number="12345678",
        account_number="99988767623",
        account_type="CHECKING",
    )
    """

    default_source: typing.Optional[bool] = pydantic_v1.Field(alias="defaultSource", default=None)
    default_destination: typing.Optional[bool] = pydantic_v1.Field(alias="defaultDestination", default=None)
    type: typing.Literal["offPlatform"] = "offPlatform"

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


"""
from mercoa import PaymentMethodRequest_BankAccount

PaymentMethodRequest_BankAccount(
    routing_number="12345678",
    account_number="99988767623",
    account_type="CHECKING",
)
"""
PaymentMethodRequest = typing.Union[
    PaymentMethodRequest_BankAccount,
    PaymentMethodRequest_Card,
    PaymentMethodRequest_Check,
    PaymentMethodRequest_Custom,
    PaymentMethodRequest_OffPlatform,
]
