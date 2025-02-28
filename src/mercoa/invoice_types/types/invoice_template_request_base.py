# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
from .invoice_status import InvoiceStatus
import pydantic
from ...payment_method_types.types.currency_code import CurrencyCode
import datetime as dt
from ...entity_types.types.entity_id import EntityId
from ...payment_method_types.types.payment_method_id import PaymentMethodId
from .payment_destination_options import PaymentDestinationOptions
from .approval_slot_assignment import ApprovalSlotAssignment
from ...entity_types.types.entity_user_id import EntityUserId
from .invoice_fees_request import InvoiceFeesRequest
from .payment_schedule import PaymentSchedule
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class InvoiceTemplateRequestBase(UniversalBaseModel):
    status: typing.Optional[InvoiceStatus] = None
    amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    Total amount of invoice in major units. If the entered amount has more decimal places than the currency supports, trailing decimals will be truncated.
    """

    currency: typing.Optional[CurrencyCode] = pydantic.Field(default=None)
    """
    Currency code for the amount. Defaults to USD.
    """

    invoice_date: typing.Optional[dt.datetime] = pydantic.Field(alias="invoiceDate", default=None)
    """
    Date the invoice was issued.
    """

    deduction_date: typing.Optional[dt.datetime] = pydantic.Field(alias="deductionDate", default=None)
    """
    Initial date when funds are scheduled to be deducted from payer's account.
    """

    due_date: typing.Optional[dt.datetime] = pydantic.Field(alias="dueDate", default=None)
    """
    Due date of invoice.
    """

    invoice_number: typing.Optional[str] = pydantic.Field(alias="invoiceNumber", default=None)
    note_to_self: typing.Optional[str] = pydantic.Field(alias="noteToSelf", default=None)
    """
    Note to self or memo on invoice.
    """

    service_start_date: typing.Optional[dt.datetime] = pydantic.Field(alias="serviceStartDate", default=None)
    service_end_date: typing.Optional[dt.datetime] = pydantic.Field(alias="serviceEndDate", default=None)
    payer_id: typing.Optional[EntityId] = pydantic.Field(alias="payerId", default=None)
    """
    ID or foreign ID of the payer of this invoice.
    """

    payment_source_id: typing.Optional[PaymentMethodId] = pydantic.Field(alias="paymentSourceId", default=None)
    """
    ID of payment source for this invoice. If not provided, will attempt to use the default payment source for the payer when creating an invoice if a default payment source exists for the payer.
    """

    vendor_id: typing.Optional[EntityId] = pydantic.Field(alias="vendorId", default=None)
    """
    ID or foreign ID of the vendor of this invoice.
    """

    payment_destination_id: typing.Optional[PaymentMethodId] = pydantic.Field(
        alias="paymentDestinationId", default=None
    )
    """
    ID of payment destination for this invoice. If not provided, will attempt to use the default payment destination for the vendor when creating an invoice if a default payment destination exists for the vendor.
    """

    payment_destination_options: typing.Optional[PaymentDestinationOptions] = pydantic.Field(
        alias="paymentDestinationOptions", default=None
    )
    """
    Options for the payment destination. Depending on the payment destination, this may include things such as check delivery method.
    """

    approvers: typing.Optional[typing.List[ApprovalSlotAssignment]] = pydantic.Field(default=None)
    """
    Set approvers for this invoice.
    """

    metadata: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    Metadata associated with this invoice.
    """

    document: typing.Optional[str] = pydantic.Field(default=None)
    """
    Base64-encoded string. Supported file types include PNG, JPG, WEBP, PDF, and all Microsoft Office formats (automatically converted to PDF). Max file size 10MB.
    """

    creator_user_id: typing.Optional[EntityUserId] = pydantic.Field(alias="creatorUserId", default=None)
    """
    User ID or Foreign ID of entity user who created this invoice.
    """

    fees: typing.Optional[InvoiceFeesRequest] = pydantic.Field(default=None)
    """
    If using a custom payment method, you can override the default fees for this invoice. If not provided, the default fees for the custom payment method will be used.
    """

    batch_payment: typing.Optional[bool] = pydantic.Field(alias="batchPayment", default=None)
    """
    If true, this invoice will be paid as a batch payment. Batches are automatically determined by Mercoa based on the payment source, destination, and scheduled payment date.
    """

    payment_schedule: typing.Optional[PaymentSchedule] = pydantic.Field(alias="paymentSchedule", default=None)
    """
    If this is a recurring invoice, this will be the payment schedule for the invoice. If not provided, this will be a one-time invoice.
    """

    tax_amount: typing.Optional[float] = pydantic.Field(alias="taxAmount", default=None)
    """
    Tax amount for this invoice.
    """

    shipping_amount: typing.Optional[float] = pydantic.Field(alias="shippingAmount", default=None)
    """
    Shipping amount for this invoice.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
