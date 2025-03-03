# This file was auto-generated by Fern from our API Definition.

from .payment_method_base_response import PaymentMethodBaseResponse
import typing_extensions
from .card_type import CardType
from ...core.serialization import FieldMetadata
from .card_brand import CardBrand
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import typing
import pydantic


class CardResponse(PaymentMethodBaseResponse):
    card_type: typing_extensions.Annotated[CardType, FieldMetadata(alias="cardType")]
    card_brand: typing_extensions.Annotated[CardBrand, FieldMetadata(alias="cardBrand")]
    last_four: typing_extensions.Annotated[str, FieldMetadata(alias="lastFour")]
    exp_month: typing_extensions.Annotated[str, FieldMetadata(alias="expMonth")]
    exp_year: typing_extensions.Annotated[str, FieldMetadata(alias="expYear")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
