# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import pydantic_v1
from ...payment_method_types.types.payment_method_type import PaymentMethodType
from .payment_rail_markup import PaymentRailMarkup


class PaymentRailRequest(pydantic_v1.BaseModel):
    type: PaymentMethodType
    name: str = pydantic_v1.Field()
    """
    Name of the payment method. For custom payment methods, this is the ID of the schema.
    """

    markup: typing.Optional[PaymentRailMarkup] = None
    description: typing.Optional[str] = None
    active: bool

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}