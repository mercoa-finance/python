# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .custom_payment_method_fee_type import CustomPaymentMethodFeeType


class CustomPaymentMethodSchemaFee(pydantic_v1.BaseModel):
    type: CustomPaymentMethodFeeType
    amount: typing.Optional[float] = pydantic_v1.Field(default=None)
    """
    If type is 'flat', this is the flat amount that will be charged as a fee. For example, if the fee is $2.50, set this to 2.50. If type is 'percentage', this is the percentage of the payment amount that will be charged as a fee. For example, if the fee is 2.5%, set this to 2.5.
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
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
