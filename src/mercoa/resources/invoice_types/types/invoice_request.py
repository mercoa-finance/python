# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...entity_types.types.entity_id import EntityId
from ...entity_types.types.entity_user_id import EntityUserId
from ...payment_method_types.types.currency_code import CurrencyCode
from ...payment_method_types.types.payment_method_id import PaymentMethodId
from .approval_slot_assignment import ApprovalSlotAssignment
from .invoice_line_item_request import InvoiceLineItemRequest
from .invoice_status import InvoiceStatus
from .payment_destination_options import PaymentDestinationOptions

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class InvoiceRequest(pydantic.BaseModel):
    status: typing.Optional[InvoiceStatus] = None
    amount: typing.Optional[float] = pydantic.Field(
        default=None,
        description="Total amount of invoice in major units. If the entered amount has more decimal places than the currency supports, trailing decimals will be truncated.",
    )
    currency: typing.Optional[CurrencyCode] = pydantic.Field(
        default=None, description="Currency code for the amount. Defaults to USD."
    )
    invoice_date: typing.Optional[dt.datetime] = pydantic.Field(
        alias="invoiceDate", default=None, description="Date the invoice was issued."
    )
    deduction_date: typing.Optional[dt.datetime] = pydantic.Field(
        alias="deductionDate", default=None, description="Date when funds will be deducted from payer's account."
    )
    settlement_date: typing.Optional[dt.datetime] = pydantic.Field(
        alias="settlementDate", default=None, description="Date of funds settlement."
    )
    due_date: typing.Optional[dt.datetime] = pydantic.Field(
        alias="dueDate", default=None, description="Due date of invoice."
    )
    invoice_number: typing.Optional[str] = pydantic.Field(alias="invoiceNumber", default=None)
    note_to_self: typing.Optional[str] = pydantic.Field(
        alias="noteToSelf", default=None, description="Note to self or memo on invoice."
    )
    service_start_date: typing.Optional[dt.datetime] = pydantic.Field(alias="serviceStartDate", default=None)
    service_end_date: typing.Optional[dt.datetime] = pydantic.Field(alias="serviceEndDate", default=None)
    payer_id: typing.Optional[EntityId] = pydantic.Field(alias="payerId", default=None)
    payment_source_id: typing.Optional[PaymentMethodId] = pydantic.Field(
        alias="paymentSourceId",
        default=None,
        description="ID of payment source for this invoice. If not provided, will attempt to use the default payment source for the payer when creating an invoice if a default payment source exists for the payer.",
    )
    vendor_id: typing.Optional[EntityId] = pydantic.Field(alias="vendorId", default=None)
    payment_destination_id: typing.Optional[PaymentMethodId] = pydantic.Field(
        alias="paymentDestinationId",
        default=None,
        description="ID of payment destination for this invoice. If not provided, will attempt to use the default payment destination for the vendor when creating an invoice if a default payment destination exists for the vendor.",
    )
    payment_destination_options: typing.Optional[PaymentDestinationOptions] = pydantic.Field(
        alias="paymentDestinationOptions",
        default=None,
        description="Options for the payment destination. Depending on the payment destination, this may include things such as check delivery method.",
    )
    approvers: typing.Optional[typing.List[ApprovalSlotAssignment]] = pydantic.Field(
        default=None, description="Set approvers for this invoice."
    )
    line_items: typing.Optional[typing.List[InvoiceLineItemRequest]] = pydantic.Field(alias="lineItems", default=None)
    metadata: typing.Optional[typing.Dict[str, str]] = pydantic.Field(
        default=None,
        description="Metadata associated with this invoice. You can specify up to 10 keys, with key names up to 40 characters long and values up to 200 characters long.",
    )
    foreign_id: typing.Optional[str] = pydantic.Field(
        alias="foreignId",
        default=None,
        description="The ID used to identify this invoice in your system. This ID must be unique within each creatorEntity in your system, e.g. two invoices with the same creatorEntity may not have the same foreign ID.",
    )
    document: typing.Optional[str] = pydantic.Field(
        default=None,
        description="Base64 encoded image or PDF of invoice document. PNG, JPG, and PDF are supported. 10MB max. If the invoice already has a document, this will add a new document to the invoice.",
    )
    uploaded_image: typing.Optional[str] = pydantic.Field(
        alias="uploadedImage", default=None, description="DEPRECATED. Use document field instead."
    )
    creator_entity_id: typing.Optional[EntityId] = pydantic.Field(
        alias="creatorEntityId", default=None, description="ID of entity who created this invoice."
    )
    creator_user_id: typing.Optional[EntityUserId] = pydantic.Field(
        alias="creatorUserId", default=None, description="ID of entity user who created this invoice."
    )

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
