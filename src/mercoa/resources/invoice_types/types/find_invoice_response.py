# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from .invoice_response import InvoiceResponse


class FindInvoiceResponse(pydantic.BaseModel):
    count: int = pydantic.Field(
        description=(
            "Total number of notifications for the given start and end date filters. This value is not limited by the limit parameter. It is provided so that you can determine how many pages of results are available.\n"
        )
    )
    has_more: bool = pydantic.Field(
        alias="hasMore",
        description=("True if there are more notifications available for the given start and end date filters.\n"),
    )
    data: typing.List[InvoiceResponse]

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