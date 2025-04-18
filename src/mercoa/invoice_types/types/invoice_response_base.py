# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
from .invoice_status import InvoiceStatus
import typing
import pydantic
from ...payment_method_types.types.currency_code import CurrencyCode
import typing_extensions
import datetime as dt
from ...core.serialization import FieldMetadata
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

    invoice_date: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="invoiceDate")] = (
        pydantic.Field(default=None)
    )
    """
    Date the invoice was issued.
    """

    deduction_date: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="deductionDate")] = (
        pydantic.Field(default=None)
    )
    """
    Initial date when funds are scheduled to be deducted from payer's account. The actual deduction date may differ from this date, and will be reflected in the processedAt field.
    """

    next_deduction_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="nextDeductionDate")
    ] = pydantic.Field(default=None)
    """
    For invoice templates, this is the date when the next recurring payment will be scheduled.
    """

    due_date: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="dueDate")] = (
        pydantic.Field(default=None)
    )
    """
    Due date of invoice.
    """

    invoice_number: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="invoiceNumber")] = None
    note_to_self: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="noteToSelf")] = None
    service_start_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="serviceStartDate")
    ] = None
    service_end_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="serviceEndDate")
    ] = None
    net_terms: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="netTerms")] = pydantic.Field(
        default=None
    )
    """
    Net terms in days. Must be a positive number.
    """

    payer_id: typing_extensions.Annotated[typing.Optional[EntityId], FieldMetadata(alias="payerId")] = None
    payer: typing.Optional[CounterpartyResponse] = None
    payment_source: typing_extensions.Annotated[
        typing.Optional[PaymentMethodResponse], FieldMetadata(alias="paymentSource")
    ] = None
    payment_source_id: typing_extensions.Annotated[
        typing.Optional[PaymentMethodId], FieldMetadata(alias="paymentSourceId")
    ] = None
    vendor_id: typing_extensions.Annotated[typing.Optional[EntityId], FieldMetadata(alias="vendorId")] = None
    vendor: typing.Optional[CounterpartyResponse] = None
    payment_destination: typing_extensions.Annotated[
        typing.Optional[PaymentMethodResponse],
        FieldMetadata(alias="paymentDestination"),
    ] = None
    payment_destination_id: typing_extensions.Annotated[
        typing.Optional[PaymentMethodId], FieldMetadata(alias="paymentDestinationId")
    ] = None
    payment_destination_options: typing_extensions.Annotated[
        typing.Optional[PaymentDestinationOptions],
        FieldMetadata(alias="paymentDestinationOptions"),
    ] = None
    payment_destination_confirmed: typing_extensions.Annotated[
        bool, FieldMetadata(alias="paymentDestinationConfirmed")
    ] = pydantic.Field()
    """
    True if the payment destination has been confirmed by the vendor. False if the payment destination has been set (for example, a check to an address) but has not been confirmed by the vendor.
    """

    batch_payment: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="batchPayment")] = (
        pydantic.Field(default=None)
    )
    """
    If true, this invoice will be paid as a batch payment. Batches are automatically determined by Mercoa based on the payment source, destination, and scheduled payment date.
    """

    has_documents: typing_extensions.Annotated[bool, FieldMetadata(alias="hasDocuments")] = pydantic.Field()
    """
    True if the invoice has documents attached.
    """

    has_source_email: typing_extensions.Annotated[bool, FieldMetadata(alias="hasSourceEmail")] = pydantic.Field()
    """
    True if the invoice was created by an incoming email.
    """

    line_items: typing_extensions.Annotated[
        typing.Optional[typing.List[InvoiceLineItemResponse]],
        FieldMetadata(alias="lineItems"),
    ] = None
    tax_amount: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="taxAmount")] = pydantic.Field(
        default=None
    )
    """
    Tax amount for this invoice.
    """

    shipping_amount: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="shippingAmount")] = (
        pydantic.Field(default=None)
    )
    """
    Shipping amount for this invoice.
    """

    approvers: typing.List[ApprovalSlot]
    approval_policy: typing_extensions.Annotated[
        typing.List[ApprovalPolicyResponse], FieldMetadata(alias="approvalPolicy")
    ]
    metadata: typing.Dict[str, str] = pydantic.Field()
    """
    Metadata associated with this invoice.
    """

    creator_entity_id: typing_extensions.Annotated[
        typing.Optional[EntityId], FieldMetadata(alias="creatorEntityId")
    ] = pydantic.Field(default=None)
    """
    The ID of the entity who created this invoice.
    """

    creator_user: typing_extensions.Annotated[
        typing.Optional[EntityUserResponse], FieldMetadata(alias="creatorUser")
    ] = pydantic.Field(default=None)
    """
    Entity user who created this invoice.
    """

    created_at: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="createdAt")]
    updated_at: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="updatedAt")]
    comments: typing.Optional[typing.List[CommentResponse]] = None
    fees: typing.Optional[InvoiceFeesResponse] = pydantic.Field(default=None)
    """
    Fees associated with this invoice.
    """

    payment_schedule: typing_extensions.Annotated[
        typing.Optional[PaymentSchedule], FieldMetadata(alias="paymentSchedule")
    ] = pydantic.Field(default=None)
    """
    If this is a recurring invoice, this will be the payment schedule for the invoice. If not provided, this will be a one-time invoice.
    """

    ocr_job_id: typing_extensions.Annotated[typing.Optional[OcrJobId], FieldMetadata(alias="ocrJobId")] = (
        pydantic.Field(default=None)
    )
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
