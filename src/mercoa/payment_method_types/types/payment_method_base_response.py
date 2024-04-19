# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import pydantic_v1
from .currency_code import CurrencyCode
from .payment_method_id import PaymentMethodId


class PaymentMethodBaseResponse(pydantic_v1.BaseModel):
    id: PaymentMethodId
    is_default_source: bool = pydantic_v1.Field(alias="isDefaultSource")
    """
    Indicates whether this payment method is the default source for the entity
    """

    is_default_destination: bool = pydantic_v1.Field(alias="isDefaultDestination")
    """
    Indicates whether this payment method is the default destination for the entity
    """

    supported_currencies: typing.List[CurrencyCode] = pydantic_v1.Field(alias="supportedCurrencies")
    created_at: dt.datetime = pydantic_v1.Field(alias="createdAt")
    updated_at: dt.datetime = pydantic_v1.Field(alias="updatedAt")

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
        populate_by_name = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
