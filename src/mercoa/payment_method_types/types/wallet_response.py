# This file was auto-generated by Fern from our API Definition.

from .payment_method_base_response import PaymentMethodBaseResponse
import typing_extensions
from .wallet_balance import WalletBalance
from ...core.serialization import FieldMetadata
import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class WalletResponse(PaymentMethodBaseResponse):
    available_balance: typing_extensions.Annotated[WalletBalance, FieldMetadata(alias="availableBalance")] = (
        pydantic.Field()
    )
    """
    The balance available for use in this wallet.
    """

    pending_balance: typing_extensions.Annotated[WalletBalance, FieldMetadata(alias="pendingBalance")] = (
        pydantic.Field()
    )
    """
    The in-flight balance into/out of this wallet.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
