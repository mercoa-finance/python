# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from .payment_method_fee import PaymentMethodFee
from ...core.serialization import FieldMetadata
import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class FeeCustomizationRailRequest(UniversalBaseModel):
    """
    Examples
    --------
    from mercoa.customization_types import (
        FeeCustomizationRailRequest,
        PaymentMethodFee_Flat,
        PaymentMethodFee_Percentage,
    )

    FeeCustomizationRailRequest(
        ach_standard=PaymentMethodFee_Flat(
            amount=2.5,
        ),
        ach_same_day=PaymentMethodFee_Percentage(
            amount=2.5,
        ),
        check_print=PaymentMethodFee_Flat(
            amount=2.5,
        ),
        check_mail=PaymentMethodFee_Flat(
            amount=2.5,
        ),
        check_mail_priority=PaymentMethodFee_Flat(
            amount=2.5,
        ),
        check_mail_ups_next_day=PaymentMethodFee_Flat(
            amount=2.5,
        ),
    )
    """

    ach_standard: typing_extensions.Annotated[
        typing.Optional[PaymentMethodFee], FieldMetadata(alias="ACH_STANDARD")
    ] = pydantic.Field(default=None)
    """
    The fee for the ACH standard rail.
    """

    ach_same_day: typing_extensions.Annotated[
        typing.Optional[PaymentMethodFee], FieldMetadata(alias="ACH_SAME_DAY")
    ] = pydantic.Field(default=None)
    """
    The fee for the ACH same day rail.
    """

    check_print: typing_extensions.Annotated[typing.Optional[PaymentMethodFee], FieldMetadata(alias="CHECK_PRINT")] = (
        pydantic.Field(default=None)
    )
    """
    The fee for the check print rail.
    """

    check_mail: typing_extensions.Annotated[typing.Optional[PaymentMethodFee], FieldMetadata(alias="CHECK_MAIL")] = (
        pydantic.Field(default=None)
    )
    """
    The fee for the check mail rail.
    """

    check_mail_priority: typing_extensions.Annotated[
        typing.Optional[PaymentMethodFee], FieldMetadata(alias="CHECK_MAIL_PRIORITY")
    ] = pydantic.Field(default=None)
    """
    The fee for the check mail priority rail.
    """

    check_mail_ups_next_day: typing_extensions.Annotated[
        typing.Optional[PaymentMethodFee],
        FieldMetadata(alias="CHECK_MAIL_UPS_NEXT_DAY"),
    ] = pydantic.Field(default=None)
    """
    The fee for the check mail UPS next day rail.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
