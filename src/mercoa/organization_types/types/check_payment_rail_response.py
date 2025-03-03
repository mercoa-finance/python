# This file was auto-generated by Fern from our API Definition.

from .generic_payment_rail_response import GenericPaymentRailResponse
import typing_extensions
import typing
from ...invoice_types.types.check_delivery_method import CheckDeliveryMethod
from ...core.serialization import FieldMetadata
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class CheckPaymentRailResponse(GenericPaymentRailResponse):
    available_delivery_methods: typing_extensions.Annotated[
        typing.List[CheckDeliveryMethod], FieldMetadata(alias="availableDeliveryMethods")
    ]
    default_delivery_method: typing_extensions.Annotated[
        CheckDeliveryMethod, FieldMetadata(alias="defaultDeliveryMethod")
    ]
    print_description: typing_extensions.Annotated[bool, FieldMetadata(alias="printDescription")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
