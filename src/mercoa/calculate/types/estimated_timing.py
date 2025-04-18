# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
import datetime as dt
from ...core.serialization import FieldMetadata
import pydantic
from ...payment_method_types.types.payment_method_id import PaymentMethodId
from ...invoice_types.types.payment_destination_options import PaymentDestinationOptions
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class EstimatedTiming(UniversalBaseModel):
    """
    Examples
    --------
    import datetime

    from mercoa.calculate import EstimatedTiming

    EstimatedTiming(
        estimated_deduction_date=datetime.datetime.fromisoformat(
            "2024-01-02 00:00:00+00:00",
        ),
        payment_source_id="pm_4794d597-70dc-4fec-b6ec-c5988e759769",
        payment_destination_id="pm_4794d597-70dc-4fec-b6ec-c5988e759769",
    )
    """

    estimated_deduction_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="estimatedDeductionDate")
    ] = pydantic.Field(default=None)
    """
    Date the payment is scheduled to be deducted from the payer's account. Use this field if the payment has not yet been deducted.
    """

    processed_at: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="processedAt")] = (
        pydantic.Field(default=None)
    )
    """
    Date the payment was processed. Use this field if the payment has already been deducted.
    """

    payment_source_id: typing_extensions.Annotated[PaymentMethodId, FieldMetadata(alias="paymentSourceId")] = (
        pydantic.Field()
    )
    """
    ID of payment source.
    """

    payment_destination_id: typing_extensions.Annotated[
        PaymentMethodId, FieldMetadata(alias="paymentDestinationId")
    ] = pydantic.Field()
    """
    ID of payment destination.
    """

    payment_destination_options: typing_extensions.Annotated[
        typing.Optional[PaymentDestinationOptions],
        FieldMetadata(alias="paymentDestinationOptions"),
    ] = pydantic.Field(default=None)
    """
    Options for the payment destination. Depending on the payment destination, this may include things such as check delivery method.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
