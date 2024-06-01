# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import pydantic_v1
from .bank_delivery_method import BankDeliveryMethod


class BankAccountPaymentDestinationOptions(pydantic_v1.BaseModel):
    """
    Examples
    --------
    from mercoa import BankAccountPaymentDestinationOptions

    BankAccountPaymentDestinationOptions(
        delivery="ACH_SAME_DAY",
    )
    """

    delivery: typing.Optional[BankDeliveryMethod] = pydantic_v1.Field(default=None)
    """
    Delivery method for ACH payments. Defaults to ACH_SAME_DAY.
    """

    description: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    ACH Statement Description. By default, this will be 'AP' followed by the first 8 characters of the invoice ID. Must be at least 4 characters and no more than 10 characters, and follow this regex pattern ^[a-zA-Z0-9\-#.$&*]{4,10}$
    """

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
