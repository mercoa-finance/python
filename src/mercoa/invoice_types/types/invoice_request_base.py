# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
from .invoice_status import InvoiceStatus
import pydantic
from ...payment_method_types.types.currency_code import CurrencyCode
import typing_extensions
import datetime as dt
from ...core.serialization import FieldMetadata
from ...entity_types.types.entity_id import EntityId
from ...payment_method_types.types.payment_method_id import PaymentMethodId
from .payment_destination_options import PaymentDestinationOptions
from .approval_slot_assignment import ApprovalSlotAssignment
from ...entity_types.types.entity_user_id import EntityUserId
from .invoice_failure_type import InvoiceFailureType
from .invoice_fees_request import InvoiceFeesRequest
from .payment_schedule import PaymentSchedule
from ...vendor_credit_types.types.vendor_credit_id import VendorCreditId
from ...ocr.types.ocr_job_id import OcrJobId
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class InvoiceRequestBase(UniversalBaseModel):
    status: typing.Optional[InvoiceStatus] = None
    amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    Total amount of invoice in major units. If the entered amount has more decimal places than the currency supports, trailing decimals will be truncated.
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
    Initial date when funds are scheduled to be deducted from payer's account.
    """

    settlement_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="settlementDate")
    ] = pydantic.Field(default=None)
    """
    Date of funds settlement.
    """

    due_date: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="dueDate")] = (
        pydantic.Field(default=None)
    )
    """
    Due date of invoice.
    """

    invoice_number: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="invoiceNumber")] = None
    note_to_self: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="noteToSelf")] = pydantic.Field(
        default=None
    )
    """
    Note to self or memo on invoice.
    """

    service_start_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="serviceStartDate")
    ] = None
    service_end_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="serviceEndDate")
    ] = None
    payer_id: typing_extensions.Annotated[typing.Optional[EntityId], FieldMetadata(alias="payerId")] = pydantic.Field(
        default=None
    )
    """
    ID or foreign ID of the payer of this invoice.
    """

    payment_source_id: typing_extensions.Annotated[
        typing.Optional[PaymentMethodId], FieldMetadata(alias="paymentSourceId")
    ] = pydantic.Field(default=None)
    """
    ID of payment source for this invoice. If not provided, will attempt to use the default payment source for the payer when creating an invoice if a default payment source exists for the payer.
    """

    vendor_id: typing_extensions.Annotated[typing.Optional[EntityId], FieldMetadata(alias="vendorId")] = pydantic.Field(
        default=None
    )
    """
    ID or foreign ID of the vendor of this invoice.
    """

    payment_destination_id: typing_extensions.Annotated[
        typing.Optional[PaymentMethodId], FieldMetadata(alias="paymentDestinationId")
    ] = pydantic.Field(default=None)
    """
    ID of payment destination for this invoice. If not provided, will attempt to use the default payment destination for the vendor when creating an invoice if a default payment destination exists for the vendor.
    """

    payment_destination_options: typing_extensions.Annotated[
        typing.Optional[PaymentDestinationOptions],
        FieldMetadata(alias="paymentDestinationOptions"),
    ] = pydantic.Field(default=None)
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

    foreign_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="foreignId")] = pydantic.Field(
        default=None
    )
    """
    The ID used to identify this invoice in your system. This ID must be unique within each creatorEntity in your system, e.g. two invoices with the same creatorEntity may not have the same foreign ID.
    """

    document: typing.Optional[str] = pydantic.Field(default=None)
    """
    Base64-encoded string. Supported file types include PNG, JPG, WEBP, PDF, and all Microsoft Office formats (automatically converted to PDF). Max file size 10MB. If the invoice already has a document, this will add a new document to the invoice.
    """

    uploaded_image: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="uploadedImage")] = (
        pydantic.Field(default=None)
    )
    """
    DEPRECATED. Use document field instead.
    """

    creator_user_id: typing_extensions.Annotated[
        typing.Optional[EntityUserId], FieldMetadata(alias="creatorUserId")
    ] = pydantic.Field(default=None)
    """
    User ID or Foreign ID of entity user who created this invoice.
    """

    failure_type: typing_extensions.Annotated[
        typing.Optional[InvoiceFailureType], FieldMetadata(alias="failureType")
    ] = pydantic.Field(default=None)
    """
    If the invoice failed to be paid, indicate the failure reason. Only applicable for invoices with custom payment methods.
    """

    fees: typing.Optional[InvoiceFeesRequest] = pydantic.Field(default=None)
    """
    If using a custom payment method, you can override the default fees for this invoice. If not provided, the default fees for the custom payment method will be used.
    """

    batch_payment: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="batchPayment")] = (
        pydantic.Field(default=None)
    )
    """
    If true, this invoice will be paid as a batch payment. Batches are automatically determined by Mercoa based on the payment source, destination, and scheduled payment date.
    """

    payment_schedule: typing_extensions.Annotated[
        typing.Optional[PaymentSchedule], FieldMetadata(alias="paymentSchedule")
    ] = pydantic.Field(default=None)
    """
    If this is a recurring invoice, this will be the payment schedule for the invoice. If not provided, this will be a one-time invoice.
    """

    vendor_credit_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[VendorCreditId]],
        FieldMetadata(alias="vendorCreditIds"),
    ] = pydantic.Field(default=None)
    """
    The IDs of the vendor credits to be applied to this invoice. Passing this field will un-apply any previously applied vendor credits.
    """

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
