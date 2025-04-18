# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing_extensions
from ...core.serialization import FieldMetadata
import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class InvoiceFeesResponse(UniversalBaseModel):
    """
    Examples
    --------
    from mercoa.invoice_types import InvoiceFeesResponse

    InvoiceFeesResponse(
        source_payment_method_fee=0.1,
        source_platform_markup_fee=0.2,
        destination_payment_method_fee=1.0,
        destination_platform_markup_fee=1.5,
    )
    """

    source_payment_method_fee: typing_extensions.Annotated[float, FieldMetadata(alias="sourcePaymentMethodFee")] = (
        pydantic.Field()
    )
    """
    Fee charged to the platform (C1) for processing the source payment method. For example, credit card interchange and acquiring fees.
    """

    source_platform_markup_fee: typing_extensions.Annotated[float, FieldMetadata(alias="sourcePlatformMarkupFee")] = (
        pydantic.Field()
    )
    """
    Fee charged to the payer (C2).
    """

    destination_payment_method_fee: typing_extensions.Annotated[
        float, FieldMetadata(alias="destinationPaymentMethodFee")
    ] = pydantic.Field()
    """
    Fee charged to the platform (C1) for processing the destination payment method. For example, postage for a check payment.
    """

    destination_platform_markup_fee: typing_extensions.Annotated[
        float, FieldMetadata(alias="destinationPlatformMarkupFee")
    ] = pydantic.Field()
    """
    Fee charged to the payee (C3).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
