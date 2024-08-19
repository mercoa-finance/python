# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class TokenGenerationPagesOptions(UniversalBaseModel):
    payment_methods: typing.Optional[bool] = pydantic.Field(alias="paymentMethods", default=None)
    representatives: typing.Optional[bool] = None
    notifications: typing.Optional[bool] = None
    counterparties: typing.Optional[bool] = None
    approvals: typing.Optional[bool] = None
    email_log: typing.Optional[bool] = pydantic.Field(alias="emailLog", default=None)

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
