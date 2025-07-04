# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class ValidatePaymentGatewayCardFeePercentage(UniversalBaseModel):
    """
    Examples
    --------
    from mercoa.payment_gateway_types import ValidatePaymentGatewayCardFeePercentage

    ValidatePaymentGatewayCardFeePercentage(
        value=250.0,
    )
    """

    value: float = pydantic.Field()
    """
    The fee percentage in bps. For example, if the fee is 2.5% and the payment amount is $100, set this to 250.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
