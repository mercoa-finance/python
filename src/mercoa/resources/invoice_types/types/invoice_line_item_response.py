# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...payment_method_types.types.currency_code import CurrencyCode

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class InvoiceLineItemResponse(pydantic.BaseModel):
    id: str
    amount: typing.Optional[float] = pydantic.Field(description="Total amount of line item in major units.")
    currency: CurrencyCode
    description: typing.Optional[str]
    name: typing.Optional[str]
    quantity: typing.Optional[int]
    unit_price: typing.Optional[float] = pydantic.Field(
        alias="unitPrice", description="Unit price of line item in major units."
    )
    service_start_date: typing.Optional[dt.datetime] = pydantic.Field(alias="serviceStartDate")
    service_end_date: typing.Optional[dt.datetime] = pydantic.Field(alias="serviceEndDate")
    metadata: typing.Optional[typing.Dict[str, str]]
    gl_account_id: typing.Optional[str] = pydantic.Field(
        alias="glAccountId", description="ID of general ledger account associated with this line item."
    )
    created_at: dt.datetime = pydantic.Field(alias="createdAt")
    updated_at: dt.datetime = pydantic.Field(alias="updatedAt")

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
        json_encoders = {dt.datetime: serialize_datetime}
