# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from ...invoice_types.types.invoice_status import InvoiceStatus


class CounterpartyInvoiceMetricsStatusResponse(pydantic_v1.BaseModel):
    """
    Examples
    --------
    from mercoa import CounterpartyInvoiceMetricsStatusResponse

    CounterpartyInvoiceMetricsStatusResponse(
        status="PAID",
        total_count=10,
        total_amount=1000.0,
    )
    """

    status: InvoiceStatus
    total_count: int = pydantic_v1.Field(alias="totalCount")
    total_amount: float = pydantic_v1.Field(alias="totalAmount")

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
