# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ...core.pydantic_utilities import UniversalBaseModel
import typing
from .check_delivery_method import CheckDeliveryMethod
import typing_extensions
from ...core.serialization import FieldMetadata
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic
from .bank_delivery_method import BankDeliveryMethod


class PaymentDestinationOptions_Check(UniversalBaseModel):
    """
    Examples
    --------
    from mercoa.invoice_types import PaymentDestinationOptions_Check

    PaymentDestinationOptions_Check(
        delivery="MAIL",
        print_description=True,
    )
    """

    type: typing.Literal["check"] = "check"
    delivery: typing.Optional[CheckDeliveryMethod] = None
    print_description: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="printDescription")] = (
        None
    )

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PaymentDestinationOptions_BankAccount(UniversalBaseModel):
    """
    Examples
    --------
    from mercoa.invoice_types import PaymentDestinationOptions_Check

    PaymentDestinationOptions_Check(
        delivery="MAIL",
        print_description=True,
    )
    """

    type: typing.Literal["bankAccount"] = "bankAccount"
    delivery: typing.Optional[BankDeliveryMethod] = None
    description: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PaymentDestinationOptions_Utility(UniversalBaseModel):
    """
    Examples
    --------
    from mercoa.invoice_types import PaymentDestinationOptions_Check

    PaymentDestinationOptions_Check(
        delivery="MAIL",
        print_description=True,
    )
    """

    type: typing.Literal["utility"] = "utility"
    account_id: typing_extensions.Annotated[str, FieldMetadata(alias="accountId")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


"""
from mercoa.invoice_types import PaymentDestinationOptions_Check

PaymentDestinationOptions_Check(
    delivery="MAIL",
    print_description=True,
)
"""
PaymentDestinationOptions = typing.Union[
    PaymentDestinationOptions_Check, PaymentDestinationOptions_BankAccount, PaymentDestinationOptions_Utility
]
