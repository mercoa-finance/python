# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
from .validate_payment_gateway_card_acceptance import (
    ValidatePaymentGatewayCardAcceptance,
)
import pydantic
from .validate_payment_gateway_card_fee import ValidatePaymentGatewayCardFee
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class ValidatePaymentGatewayCardResponse(UniversalBaseModel):
    """
    Examples
    --------
    from mercoa.payment_gateway_types import (
        ValidatePaymentGatewayCardFee_Percentage,
        ValidatePaymentGatewayCardResponse,
    )

    ValidatePaymentGatewayCardResponse(
        eligibility="ACCEPTED",
        fee=ValidatePaymentGatewayCardFee_Percentage(
            value=2.5,
        ),
    )
    """

    eligibility: ValidatePaymentGatewayCardAcceptance = pydantic.Field()
    """
    Whether the payment gateway accepts card payments
    """

    fee: ValidatePaymentGatewayCardFee = pydantic.Field()
    """
    The fee that was extracted from the gateway
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
