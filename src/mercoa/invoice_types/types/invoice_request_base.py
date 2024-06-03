# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from ...entity_types.types.entity_id import EntityId
from ...entity_types.types.entity_user_id import EntityUserId
from ...payment_method_types.types.currency_code import CurrencyCode
from ...payment_method_types.types.payment_method_id import PaymentMethodId
from .approval_slot_assignment import ApprovalSlotAssignment
from .invoice_line_item_request import InvoiceLineItemRequest
from .invoice_status import InvoiceStatus
from .payment_destination_options import PaymentDestinationOptions


class InvoiceRequestBase(pydantic_v1.BaseModel):
    status: typing.Optional[InvoiceStatus] = None
    amount: typing.Optional[float] = pydantic_v1.Field(default=None)
    """
    Total amount of invoice in major units. If the entered amount has more decimal places than the currency supports, trailing decimals will be truncated.
    """

    currency: typing.Optional[CurrencyCode] = pydantic_v1.Field(default=None)
    """
    Currency code for the amount. Defaults to USD.
    """

    invoice_date: typing.Optional[dt.datetime] = pydantic_v1.Field(alias="invoiceDate", default=None)
    """
    Date the invoice was issued.
    """

    deduction_date: typing.Optional[dt.datetime] = pydantic_v1.Field(alias="deductionDate", default=None)
    """
    Date when funds will be deducted from payer's account.
    """

    settlement_date: typing.Optional[dt.datetime] = pydantic_v1.Field(alias="settlementDate", default=None)
    """
    Date of funds settlement.
    """

    due_date: typing.Optional[dt.datetime] = pydantic_v1.Field(alias="dueDate", default=None)
    """
    Due date of invoice.
    """

    invoice_number: typing.Optional[str] = pydantic_v1.Field(alias="invoiceNumber", default=None)
    note_to_self: typing.Optional[str] = pydantic_v1.Field(alias="noteToSelf", default=None)
    """
    Note to self or memo on invoice.
    """

    service_start_date: typing.Optional[dt.datetime] = pydantic_v1.Field(alias="serviceStartDate", default=None)
    service_end_date: typing.Optional[dt.datetime] = pydantic_v1.Field(alias="serviceEndDate", default=None)
    payer_id: typing.Optional[EntityId] = pydantic_v1.Field(alias="payerId", default=None)
    payment_source_id: typing.Optional[PaymentMethodId] = pydantic_v1.Field(alias="paymentSourceId", default=None)
    """
    ID of payment source for this invoice. If not provided, will attempt to use the default payment source for the payer when creating an invoice if a default payment source exists for the payer.
    """

    vendor_id: typing.Optional[EntityId] = pydantic_v1.Field(alias="vendorId", default=None)
    payment_destination_id: typing.Optional[PaymentMethodId] = pydantic_v1.Field(
        alias="paymentDestinationId", default=None
    )
    """
    ID of payment destination for this invoice. If not provided, will attempt to use the default payment destination for the vendor when creating an invoice if a default payment destination exists for the vendor.
    """

    payment_destination_options: typing.Optional[PaymentDestinationOptions] = pydantic_v1.Field(
        alias="paymentDestinationOptions", default=None
    )
    """
    Options for the payment destination. Depending on the payment destination, this may include things such as check delivery method.
    """

    approvers: typing.Optional[typing.List[ApprovalSlotAssignment]] = pydantic_v1.Field(default=None)
    """
    Set approvers for this invoice.
    """

    line_items: typing.Optional[typing.List[InvoiceLineItemRequest]] = pydantic_v1.Field(
        alias="lineItems", default=None
    )
    metadata: typing.Optional[typing.Dict[str, str]] = pydantic_v1.Field(default=None)
    """
    Metadata associated with this invoice. You can specify up to 10 keys, with key names up to 40 characters long and values up to 200 characters long.
    """

    foreign_id: typing.Optional[str] = pydantic_v1.Field(alias="foreignId", default=None)
    """
    The ID used to identify this invoice in your system. This ID must be unique within each creatorEntity in your system, e.g. two invoices with the same creatorEntity may not have the same foreign ID.
    """

    document: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Base64 encoded image or PDF of invoice document. PNG, JPG, and PDF are supported. 10MB max. If the invoice already has a document, this will add a new document to the invoice.
    """

    uploaded_image: typing.Optional[str] = pydantic_v1.Field(alias="uploadedImage", default=None)
    """
    DEPRECATED. Use document field instead.
    """

    creator_user_id: typing.Optional[EntityUserId] = pydantic_v1.Field(alias="creatorUserId", default=None)
    """
    ID of entity user who created this invoice.
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
        allow_population_by_field_name = True
        populate_by_name = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
