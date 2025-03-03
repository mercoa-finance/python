# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing_extensions
from ...core.serialization import FieldMetadata
import pydantic
import typing
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class CounterpartyCustomizationAccount(UniversalBaseModel):
    """
    Examples
    --------
    from mercoa.entity_types import CounterpartyCustomizationAccount

    CounterpartyCustomizationAccount(
        account_id="85866843",
        postal_code="94105",
        name_on_account="John Doe",
    )
    """

    account_id: typing_extensions.Annotated[str, FieldMetadata(alias="accountId")] = pydantic.Field()
    """
    The ID the counterparty has assigned to this account.
    """

    postal_code: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="postalCode")] = pydantic.Field(
        default=None
    )
    """
    The postal code the counterparty has assigned to this account.
    """

    name_on_account: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="nameOnAccount")] = (
        pydantic.Field(default=None)
    )
    """
    The name on the account the counterparty has assigned to this account.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
