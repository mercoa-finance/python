# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from ...entity.types.entity_response import EntityResponse
from ...invoice.types.invoice_id import InvoiceId
from ...payment_method.types.payment_method_response import PaymentMethodResponse
from .transaction_response import TransactionResponse


class TransactionResponseExpanded(TransactionResponse):
    invoice_id: InvoiceId = pydantic.Field(alias="invoiceId")
    deduction_date: typing.Optional[dt.datetime] = pydantic.Field(alias="deductionDate")
    due_date: typing.Optional[dt.datetime] = pydantic.Field(alias="dueDate")
    payer: typing.Optional[EntityResponse]
    vendor: typing.Optional[EntityResponse]
    payment_source: typing.Optional[PaymentMethodResponse] = pydantic.Field(alias="paymentSource")
    payment_destination: typing.Optional[PaymentMethodResponse] = pydantic.Field(alias="paymentDestination")

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
