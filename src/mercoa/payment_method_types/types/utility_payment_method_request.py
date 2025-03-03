# This file was auto-generated by Fern from our API Definition.

from .payment_method_base_request import PaymentMethodBaseRequest
import typing_extensions
from ...core.serialization import FieldMetadata
import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class UtilityPaymentMethodRequest(PaymentMethodBaseRequest):
    utility_id: typing_extensions.Annotated[str, FieldMetadata(alias="utilityId")] = pydantic.Field()
    """
    The ID of the utility that this payment method is linked to.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
