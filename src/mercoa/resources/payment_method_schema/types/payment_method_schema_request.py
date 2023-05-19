# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from ...invoice.types.currency_code import CurrencyCode
from .payment_method_schema_field import PaymentMethodSchemaField


class PaymentMethodSchemaRequest(pydantic.BaseModel):
    name: str
    is_source: bool = pydantic.Field(
        alias="isSource", description=("This payment method can be used as a payment source for an invoice\n")
    )
    is_destination: bool = pydantic.Field(
        alias="isDestination", description=("This payment method can be used as a payment destination for an invoice\n")
    )
    supported_currencies: typing.Optional[typing.List[CurrencyCode]] = pydantic.Field(
        alias="supportedCurrencies",
        description=(
            "List of currencies that this payment method supports. If not provided, the payment method will support only USD.\n"
        ),
    )
    fields: typing.List[PaymentMethodSchemaField]

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
