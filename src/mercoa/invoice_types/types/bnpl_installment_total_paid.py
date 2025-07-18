# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing_extensions
from ...core.serialization import FieldMetadata
import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class BnplInstallmentTotalPaid(UniversalBaseModel):
    """
    Examples
    --------
    from mercoa.invoice_types import BnplInstallmentTotalPaid

    BnplInstallmentTotalPaid(
        principal_balance=0,
        due_interest=0,
        total_late_fees=0,
        fee_amount=0,
    )
    """

    principal_balance: typing_extensions.Annotated[int, FieldMetadata(alias="principalBalance")] = pydantic.Field()
    """
    Total principal paid in cents
    """

    due_interest: typing_extensions.Annotated[int, FieldMetadata(alias="dueInterest")] = pydantic.Field()
    """
    Total interest paid in cents
    """

    total_late_fees: typing_extensions.Annotated[int, FieldMetadata(alias="totalLateFees")] = pydantic.Field()
    """
    Total late fees paid in cents
    """

    fee_amount: typing_extensions.Annotated[int, FieldMetadata(alias="feeAmount")] = pydantic.Field()
    """
    Total fees paid in cents
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
