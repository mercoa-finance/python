# This file was auto-generated by Fern from our API Definition.

from .payment_method_base_request import PaymentMethodBaseRequest
import typing_extensions
import typing
from ...core.serialization import FieldMetadata
import pydantic
from .bank_type import BankType
from .plaid_link_request import PlaidLinkRequest
from .bank_account_check_options import BankAccountCheckOptions
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class BankAccountRequest(PaymentMethodBaseRequest):
    account_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="accountName")] = (
        pydantic.Field(default=None)
    )
    """
    The name of the account. For example "My Checking Account" or "Property XYZ Checking"
    """

    bank_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="bankName")] = pydantic.Field(
        default=None
    )
    """
    The name of the bank. This is now automatically set when the bank account is linked.
    """

    routing_number: typing_extensions.Annotated[str, FieldMetadata(alias="routingNumber")]
    account_number: typing_extensions.Annotated[str, FieldMetadata(alias="accountNumber")]
    account_type: typing_extensions.Annotated[BankType, FieldMetadata(alias="accountType")]
    plaid: typing.Optional[PlaidLinkRequest] = pydantic.Field(default=None)
    """
    If provided, will link a bank account using Plaid Link
    """

    check_options: typing_extensions.Annotated[
        typing.Optional[BankAccountCheckOptions], FieldMetadata(alias="checkOptions")
    ] = pydantic.Field(default=None)
    """
    If this bank account supports check printing, use this to enable check printing and set the check options. Checks will be printed directly from the bank account.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
