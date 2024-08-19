# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import datetime as dt
import pydantic
from ...payment_method_types.types.currency_code import CurrencyCode
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class InvoiceMetricsPerDateResponse(UniversalBaseModel):
    """
    Examples
    --------
    import datetime

    from mercoa.invoice_types import InvoiceMetricsPerDateResponse

    InvoiceMetricsPerDateResponse(
        date=datetime.datetime.fromisoformat(
            "2021-01-01 00:00:00+00:00",
        ),
        total_amount=100.0,
        total_count=1,
        average_amount=100.0,
        currency="USD",
    )
    """

    date: dt.datetime
    total_amount: float = pydantic.Field(alias="totalAmount")
    total_count: int = pydantic.Field(alias="totalCount")
    average_amount: float = pydantic.Field(alias="averageAmount")
    currency: CurrencyCode

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
