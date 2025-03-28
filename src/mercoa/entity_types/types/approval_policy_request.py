# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
from .trigger import Trigger
import pydantic
from .rule import Rule
import typing_extensions
from .approval_policy_id import ApprovalPolicyId
from ...core.serialization import FieldMetadata
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class ApprovalPolicyRequest(UniversalBaseModel):
    """
    Examples
    --------
    from mercoa.entity_types import (
        ApprovalPolicyRequest,
        IdentifierList_RolesList,
        Rule_Approver,
        Trigger_Amount,
    )

    ApprovalPolicyRequest(
        trigger=[
            Trigger_Amount(
                amount=100.0,
                currency="USD",
            )
        ],
        rule=Rule_Approver(
            num_approvers=2,
            identifier_list=IdentifierList_RolesList(value=["Admin", "Controller"]),
        ),
        upstream_policy_id="root",
    )
    """

    trigger: typing.List[Trigger] = pydantic.Field()
    """
    List of triggers that will cause this policy to be evaluated. If no triggers are provided, the policy will be evaluated for all invoices.
    """

    rule: Rule
    upstream_policy_id: typing_extensions.Annotated[ApprovalPolicyId, FieldMetadata(alias="upstreamPolicyId")] = (
        pydantic.Field()
    )
    """
    The policy ID of the previous approval policy in the chain of policies. Use 'root' if no upstreamPolicyId is intended to be set.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
