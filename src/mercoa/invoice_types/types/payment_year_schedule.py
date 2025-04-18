# This file was auto-generated by Fern from our API Definition.

from .payment_schedule_base import PaymentScheduleBase
import typing_extensions
from ...core.serialization import FieldMetadata
import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class PaymentYearSchedule(PaymentScheduleBase):
    """
    Examples
    --------
    import datetime

    from mercoa.invoice_types import PaymentYearSchedule

    PaymentYearSchedule(
        repeat_on_day=10,
        repeat_on_month=1,
        ends=datetime.datetime.fromisoformat(
            "2021-01-01 00:00:00+00:00",
        ),
    )
    """

    repeat_on_day: typing_extensions.Annotated[int, FieldMetadata(alias="repeatOnDay")] = pydantic.Field()
    """
    Day of the month to repeat on. Positive values (1-31): Represent the day of the month counting from the start (e.g., 10 is the 10th day of the month). Negative values (-1 to -31): Represent the day of the month counting backward from the end (e.g., -1 is the last day of the month, -2 is the second-to-last day).
    """

    repeat_on_month: typing_extensions.Annotated[int, FieldMetadata(alias="repeatOnMonth")] = pydantic.Field()
    """
    Month to repeat on (1-12).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
