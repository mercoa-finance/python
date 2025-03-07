# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
from ...payment_method_types.types.currency_code import CurrencyCode
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import typing
import pydantic


class AccelerationFundsBalanceResponse(UniversalBaseModel):
    """
    Examples
    --------
    from mercoa.entity_types import AccelerationFundsBalanceResponse

    AccelerationFundsBalanceResponse(
        amount=100.0,
        currency="USD",
    )
    """

    amount: float
    currency: CurrencyCode

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
