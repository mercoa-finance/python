# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import pydantic
import typing
from .currency_code import CurrencyCode
from .custom_payment_method_schema_field import CustomPaymentMethodSchemaField
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class CustomPaymentMethodSchemaRequest(UniversalBaseModel):
    """
    Examples
    --------
    from mercoa.payment_method_types import (
        CustomPaymentMethodSchemaField,
        CustomPaymentMethodSchemaRequest,
    )

    CustomPaymentMethodSchemaRequest(
        name="Wire",
        is_source=False,
        is_destination=True,
        supported_currencies=["USD", "EUR"],
        fields=[
            CustomPaymentMethodSchemaField(
                name="bankName",
                display_name="Bank Name",
                type="text",
                optional=False,
            ),
            CustomPaymentMethodSchemaField(
                name="recipientName",
                display_name="Recipient Name",
                type="text",
                optional=False,
            ),
            CustomPaymentMethodSchemaField(
                name="accountNumber",
                display_name="Account Number",
                type="usBankAccountNumber",
                optional=False,
                use_as_account_number=True,
            ),
            CustomPaymentMethodSchemaField(
                name="routingNumber",
                display_name="Routing Number",
                type="usBankRoutingNumber",
                optional=False,
            ),
        ],
        estimated_processing_time=0,
        max_amount=100000.0,
        min_amount=1.0,
    )
    """

    name: str
    is_source: bool = pydantic.Field(alias="isSource")
    """
    This payment method can be used as a payment source for an invoice
    """

    is_destination: bool = pydantic.Field(alias="isDestination")
    """
    This payment method can be used as a payment destination for an invoice
    """

    supported_currencies: typing.Optional[typing.List[CurrencyCode]] = pydantic.Field(
        alias="supportedCurrencies", default=None
    )
    """
    List of currencies that this payment method supports. If not provided, the payment method will support only USD.
    """

    fields: typing.List[CustomPaymentMethodSchemaField]
    estimated_processing_time: typing.Optional[int] = pydantic.Field(alias="estimatedProcessingTime", default=None)
    """
    Estimated time in days for this payment method to process a payments. Set as 0 for same-day payment methods, -1 for unknown processing time.
    """

    max_amount: typing.Optional[float] = pydantic.Field(alias="maxAmount", default=None)
    """
    The maximum amount that can be transferred from this payment method in a single transaction.
    """

    min_amount: typing.Optional[float] = pydantic.Field(alias="minAmount", default=None)
    """
    The minimum amount that can be transferred from this payment method in a single transaction. Default is 1.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
