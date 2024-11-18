# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from .payment_schedule_end_condition import PaymentScheduleEndCondition
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class PaymentScheduleBase(UniversalBaseModel):
    repeat_every: typing.Optional[int] = pydantic.Field(alias="repeatEvery", default=None)
    """
    How often to repeat the payments. Defaults to 1. Must be greater than 0. For example, if repeatEvery is set to 2 and this is a daily payment, the payment will be made every other day. If repeatEvery is set to 3 and this is a weekly payment, the payment will be made every third week.
    """

    ends: typing.Optional[PaymentScheduleEndCondition] = pydantic.Field(default=None)
    """
    When to end the payments, either a number of occurrences or a date. Defaults to never ending if not specified
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow