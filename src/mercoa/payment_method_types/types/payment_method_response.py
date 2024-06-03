# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .bank_account_check_options import BankAccountCheckOptions
from .bank_status import BankStatus
from .bank_type import BankType
from .card_brand import CardBrand
from .card_type import CardType
from .currency_code import CurrencyCode
from .custom_payment_method_schema_id import CustomPaymentMethodSchemaId
from .custom_payment_method_schema_response import CustomPaymentMethodSchemaResponse
from .payment_method_id import PaymentMethodId


class PaymentMethodResponse_BankAccount(pydantic_v1.BaseModel):
    """
    Examples
    --------
    import datetime

    from mercoa import PaymentMethodResponse_BankAccount

    PaymentMethodResponse_BankAccount(
        id="pm_4794d597-70dc-4fec-b6ec-c5988e759769",
        account_name="My Checking Account",
        bank_name="Chase",
        routing_number="12345678",
        account_number="99988767623",
        account_type="CHECKING",
        status="VERIFIED",
        is_default_source=True,
        is_default_destination=True,
        supported_currencies=["USD"],
        created_at=datetime.datetime.fromisoformat(
            "2021-01-01 00:00:00+00:00",
        ),
        updated_at=datetime.datetime.fromisoformat(
            "2021-01-01 00:00:00+00:00",
        ),
    )
    """

    account_name: str = pydantic_v1.Field(alias="accountName")
    bank_name: str = pydantic_v1.Field(alias="bankName")
    routing_number: str = pydantic_v1.Field(alias="routingNumber")
    account_number: str = pydantic_v1.Field(alias="accountNumber")
    account_type: BankType = pydantic_v1.Field(alias="accountType")
    status: BankStatus
    check_options: typing.Optional[BankAccountCheckOptions] = pydantic_v1.Field(alias="checkOptions", default=None)
    id: PaymentMethodId
    is_default_source: bool = pydantic_v1.Field(alias="isDefaultSource")
    is_default_destination: bool = pydantic_v1.Field(alias="isDefaultDestination")
    supported_currencies: typing.List[CurrencyCode] = pydantic_v1.Field(alias="supportedCurrencies")
    created_at: dt.datetime = pydantic_v1.Field(alias="createdAt")
    updated_at: dt.datetime = pydantic_v1.Field(alias="updatedAt")
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


class PaymentMethodResponse_Card(pydantic_v1.BaseModel):
    """
    Examples
    --------
    import datetime

    from mercoa import PaymentMethodResponse_BankAccount

    PaymentMethodResponse_BankAccount(
        id="pm_4794d597-70dc-4fec-b6ec-c5988e759769",
        account_name="My Checking Account",
        bank_name="Chase",
        routing_number="12345678",
        account_number="99988767623",
        account_type="CHECKING",
        status="VERIFIED",
        is_default_source=True,
        is_default_destination=True,
        supported_currencies=["USD"],
        created_at=datetime.datetime.fromisoformat(
            "2021-01-01 00:00:00+00:00",
        ),
        updated_at=datetime.datetime.fromisoformat(
            "2021-01-01 00:00:00+00:00",
        ),
    )
    """

    card_type: CardType = pydantic_v1.Field(alias="cardType")
    card_brand: CardBrand = pydantic_v1.Field(alias="cardBrand")
    last_four: str = pydantic_v1.Field(alias="lastFour")
    exp_month: str = pydantic_v1.Field(alias="expMonth")
    exp_year: str = pydantic_v1.Field(alias="expYear")
    id: PaymentMethodId
    is_default_source: bool = pydantic_v1.Field(alias="isDefaultSource")
    is_default_destination: bool = pydantic_v1.Field(alias="isDefaultDestination")
    supported_currencies: typing.List[CurrencyCode] = pydantic_v1.Field(alias="supportedCurrencies")
    created_at: dt.datetime = pydantic_v1.Field(alias="createdAt")
    updated_at: dt.datetime = pydantic_v1.Field(alias="updatedAt")
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


class PaymentMethodResponse_Check(pydantic_v1.BaseModel):
    """
    Examples
    --------
    import datetime

    from mercoa import PaymentMethodResponse_BankAccount

    PaymentMethodResponse_BankAccount(
        id="pm_4794d597-70dc-4fec-b6ec-c5988e759769",
        account_name="My Checking Account",
        bank_name="Chase",
        routing_number="12345678",
        account_number="99988767623",
        account_type="CHECKING",
        status="VERIFIED",
        is_default_source=True,
        is_default_destination=True,
        supported_currencies=["USD"],
        created_at=datetime.datetime.fromisoformat(
            "2021-01-01 00:00:00+00:00",
        ),
        updated_at=datetime.datetime.fromisoformat(
            "2021-01-01 00:00:00+00:00",
        ),
    )
    """

    pay_to_the_order_of: str = pydantic_v1.Field(alias="payToTheOrderOf")
    address_line_1: str = pydantic_v1.Field(alias="addressLine1")
    address_line_2: typing.Optional[str] = pydantic_v1.Field(alias="addressLine2", default=None)
    city: str
    state_or_province: str = pydantic_v1.Field(alias="stateOrProvince")
    postal_code: str = pydantic_v1.Field(alias="postalCode")
    country: str
    id: PaymentMethodId
    is_default_source: bool = pydantic_v1.Field(alias="isDefaultSource")
    is_default_destination: bool = pydantic_v1.Field(alias="isDefaultDestination")
    supported_currencies: typing.List[CurrencyCode] = pydantic_v1.Field(alias="supportedCurrencies")
    created_at: dt.datetime = pydantic_v1.Field(alias="createdAt")
    updated_at: dt.datetime = pydantic_v1.Field(alias="updatedAt")
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


class PaymentMethodResponse_Custom(pydantic_v1.BaseModel):
    """
    Examples
    --------
    import datetime

    from mercoa import PaymentMethodResponse_BankAccount

    PaymentMethodResponse_BankAccount(
        id="pm_4794d597-70dc-4fec-b6ec-c5988e759769",
        account_name="My Checking Account",
        bank_name="Chase",
        routing_number="12345678",
        account_number="99988767623",
        account_type="CHECKING",
        status="VERIFIED",
        is_default_source=True,
        is_default_destination=True,
        supported_currencies=["USD"],
        created_at=datetime.datetime.fromisoformat(
            "2021-01-01 00:00:00+00:00",
        ),
        updated_at=datetime.datetime.fromisoformat(
            "2021-01-01 00:00:00+00:00",
        ),
    )
    """

    foreign_id: str = pydantic_v1.Field(alias="foreignId")
    account_name: typing.Optional[str] = pydantic_v1.Field(alias="accountName", default=None)
    account_number: typing.Optional[str] = pydantic_v1.Field(alias="accountNumber", default=None)
    schema_id: CustomPaymentMethodSchemaId = pydantic_v1.Field(alias="schemaId")
    schema_: CustomPaymentMethodSchemaResponse = pydantic_v1.Field(alias="schema")
    data: typing.Dict[str, str]
    id: PaymentMethodId
    is_default_source: bool = pydantic_v1.Field(alias="isDefaultSource")
    is_default_destination: bool = pydantic_v1.Field(alias="isDefaultDestination")
    supported_currencies: typing.List[CurrencyCode] = pydantic_v1.Field(alias="supportedCurrencies")
    created_at: dt.datetime = pydantic_v1.Field(alias="createdAt")
    updated_at: dt.datetime = pydantic_v1.Field(alias="updatedAt")
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


class PaymentMethodResponse_OffPlatform(pydantic_v1.BaseModel):
    """
    Examples
    --------
    import datetime

    from mercoa import PaymentMethodResponse_BankAccount

    PaymentMethodResponse_BankAccount(
        id="pm_4794d597-70dc-4fec-b6ec-c5988e759769",
        account_name="My Checking Account",
        bank_name="Chase",
        routing_number="12345678",
        account_number="99988767623",
        account_type="CHECKING",
        status="VERIFIED",
        is_default_source=True,
        is_default_destination=True,
        supported_currencies=["USD"],
        created_at=datetime.datetime.fromisoformat(
            "2021-01-01 00:00:00+00:00",
        ),
        updated_at=datetime.datetime.fromisoformat(
            "2021-01-01 00:00:00+00:00",
        ),
    )
    """

    id: PaymentMethodId
    is_default_source: bool = pydantic_v1.Field(alias="isDefaultSource")
    is_default_destination: bool = pydantic_v1.Field(alias="isDefaultDestination")
    supported_currencies: typing.List[CurrencyCode] = pydantic_v1.Field(alias="supportedCurrencies")
    created_at: dt.datetime = pydantic_v1.Field(alias="createdAt")
    updated_at: dt.datetime = pydantic_v1.Field(alias="updatedAt")
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
import datetime

from mercoa import PaymentMethodResponse_BankAccount

PaymentMethodResponse_BankAccount(
    id="pm_4794d597-70dc-4fec-b6ec-c5988e759769",
    account_name="My Checking Account",
    bank_name="Chase",
    routing_number="12345678",
    account_number="99988767623",
    account_type="CHECKING",
    status="VERIFIED",
    is_default_source=True,
    is_default_destination=True,
    supported_currencies=["USD"],
    created_at=datetime.datetime.fromisoformat(
        "2021-01-01 00:00:00+00:00",
    ),
    updated_at=datetime.datetime.fromisoformat(
        "2021-01-01 00:00:00+00:00",
    ),
)
"""
PaymentMethodResponse = typing.Union[
    PaymentMethodResponse_BankAccount,
    PaymentMethodResponse_Card,
    PaymentMethodResponse_Check,
    PaymentMethodResponse_Custom,
    PaymentMethodResponse_OffPlatform,
]
