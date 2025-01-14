# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
from .invoice_status import InvoiceStatus
import typing
import pydantic
from ...payment_method_types.types.currency_code import CurrencyCode
import datetime as dt
from ...entity_types.types.entity_id import EntityId
from ...entity_types.types.counterparty_response import CounterpartyResponse
from ...payment_method_types.types.payment_method_response import PaymentMethodResponse
from ...payment_method_types.types.payment_method_id import PaymentMethodId
from .payment_destination_options import PaymentDestinationOptions
from .invoice_line_item_response import InvoiceLineItemResponse
from .approval_slot import ApprovalSlot
from ...entity_types.types.approval_policy_response import ApprovalPolicyResponse
from ...entity_types.types.entity_user_response import EntityUserResponse
from .comment_response import CommentResponse
from .invoice_fees_response import InvoiceFeesResponse
from .payment_schedule import PaymentSchedule
from ...ocr.types.ocr_job_id import OcrJobId
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class InvoiceResponseBase(UniversalBaseModel):
    status: InvoiceStatus
    amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    Total amount of invoice in major units
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
    Initial date when funds are scheduled to be deducted from payer's account. The actual deduction date may differ from this date, and will be reflected in the processedAt field.
    """

    next_deduction_date: typing.Optional[dt.datetime] = pydantic.Field(alias="nextDeductionDate", default=None)
    """
    For invoice templates, this is the date when the next recurring payment will be scheduled.
    """

    due_date: typing.Optional[dt.datetime] = pydantic.Field(alias="dueDate", default=None)
    """
    Due date of invoice.
    """

    invoice_number: typing.Optional[str] = pydantic.Field(alias="invoiceNumber", default=None)
    note_to_self: typing.Optional[str] = pydantic.Field(alias="noteToSelf", default=None)
    service_start_date: typing.Optional[dt.datetime] = pydantic.Field(alias="serviceStartDate", default=None)
    service_end_date: typing.Optional[dt.datetime] = pydantic.Field(alias="serviceEndDate", default=None)
    payer_id: typing.Optional[EntityId] = pydantic.Field(alias="payerId", default=None)
    payer: typing.Optional[CounterpartyResponse] = None
    payment_source: typing.Optional[PaymentMethodResponse] = pydantic.Field(alias="paymentSource", default=None)
    payment_source_id: typing.Optional[PaymentMethodId] = pydantic.Field(alias="paymentSourceId", default=None)
    vendor_id: typing.Optional[EntityId] = pydantic.Field(alias="vendorId", default=None)
    vendor: typing.Optional[CounterpartyResponse] = None
    payment_destination: typing.Optional[PaymentMethodResponse] = pydantic.Field(
        alias="paymentDestination", default=None
    )
    payment_destination_id: typing.Optional[PaymentMethodId] = pydantic.Field(
        alias="paymentDestinationId", default=None
    )
    payment_destination_options: typing.Optional[PaymentDestinationOptions] = pydantic.Field(
        alias="paymentDestinationOptions", default=None
    )
    payment_destination_confirmed: bool = pydantic.Field(alias="paymentDestinationConfirmed")
    """
    True if the payment destination has been confirmed by the vendor. False if the payment destination has been set (for example, a check to an address) but has not been confirmed by the vendor.
    """

    batch_payment: typing.Optional[bool] = pydantic.Field(alias="batchPayment", default=None)
    """
    If true, this invoice will be paid as a batch payment. Batches are automatically determined by Mercoa based on the payment source, destination, and scheduled payment date.
    """

    has_documents: bool = pydantic.Field(alias="hasDocuments")
    """
    True if the invoice has documents attached.
    """

    has_source_email: bool = pydantic.Field(alias="hasSourceEmail")
    """
    True if the invoice was created by an incoming email.
    """

    line_items: typing.Optional[typing.List[InvoiceLineItemResponse]] = pydantic.Field(alias="lineItems", default=None)
    tax_amount: typing.Optional[float] = pydantic.Field(alias="taxAmount", default=None)
    """
    Tax amount for this invoice.
    """

    shipping_amount: typing.Optional[float] = pydantic.Field(alias="shippingAmount", default=None)
    """
    Shipping amount for this invoice.
    """

    approvers: typing.List[ApprovalSlot]
    approval_policy: typing.List[ApprovalPolicyResponse] = pydantic.Field(alias="approvalPolicy")
    metadata: typing.Dict[str, str] = pydantic.Field()
    """
    Metadata associated with this invoice.
    """

    creator_entity_id: typing.Optional[EntityId] = pydantic.Field(alias="creatorEntityId", default=None)
    """
    The ID of the entity who created this invoice.
    """

    creator_user: typing.Optional[EntityUserResponse] = pydantic.Field(alias="creatorUser", default=None)
    """
    Entity user who created this invoice.
    """

    created_at: dt.datetime = pydantic.Field(alias="createdAt")
    updated_at: dt.datetime = pydantic.Field(alias="updatedAt")
    comments: typing.Optional[typing.List[CommentResponse]] = None
    fees: typing.Optional[InvoiceFeesResponse] = pydantic.Field(default=None)
    """
    Fees associated with this invoice.
    """

    payment_schedule: typing.Optional[PaymentSchedule] = pydantic.Field(alias="paymentSchedule", default=None)
    """
    If this is a recurring invoice, this will be the payment schedule for the invoice. If not provided, this will be a one-time invoice.
    """

    ocr_job_id: typing.Optional[OcrJobId] = pydantic.Field(alias="ocrJobId", default=None)
    """
    ID of the OCR job that processed this invoice.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
