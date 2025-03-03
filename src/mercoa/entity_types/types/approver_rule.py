# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing_extensions
from ...core.serialization import FieldMetadata
import pydantic
from .identifier_list import IdentifierList
import typing
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class ApproverRule(UniversalBaseModel):
    num_approvers: typing_extensions.Annotated[int, FieldMetadata(alias="numApprovers")] = pydantic.Field()
    """
    Number of approvals required to approve an invoice
    """

    identifier_list: typing_extensions.Annotated[IdentifierList, FieldMetadata(alias="identifierList")] = (
        pydantic.Field()
    )
    """
    List of users or roles that should be used to determine eligible approvers
    """

    auto_assign: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="autoAssign")] = pydantic.Field(
        default=None
    )
    """
    If true, the policy will automatically assign approvers to the invoice. If more than one approver is eligible, the policy will assign all eligible approvers to the invoice.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
