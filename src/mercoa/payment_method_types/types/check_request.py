# This file was auto-generated by Fern from our API Definition.

from .payment_method_base_request import PaymentMethodBaseRequest
import pydantic
import typing
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class CheckRequest(PaymentMethodBaseRequest):
    pay_to_the_order_of: str = pydantic.Field(alias="payToTheOrderOf")
    address_line_1: str = pydantic.Field(alias="addressLine1")
    address_line_2: typing.Optional[str] = pydantic.Field(alias="addressLine2", default=None)
    city: str
    state_or_province: str = pydantic.Field(alias="stateOrProvince")
    postal_code: str = pydantic.Field(alias="postalCode")
    country: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
