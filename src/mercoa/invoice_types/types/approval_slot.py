# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ...entity_types.types.approval_policy_id import ApprovalPolicyId
from ...core.serialization import FieldMetadata
import pydantic
from .approval_slot_id import ApprovalSlotId
from ...entity_types.types.entity_user_id import EntityUserId
from .approver_action import ApproverAction
import datetime as dt
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class ApprovalSlot(UniversalBaseModel):
    """
    Examples
    --------
    import datetime

    from mercoa.invoice_types import ApprovalSlot

    ApprovalSlot(
        approval_policy_id="apvl_5ce50275-1789-42ea-bc60-bb7e6d03635c",
        approval_slot_id="inap_9bb311c9-7c15-4c9e-8148-63814e0abec6",
        assigned_user_id="user_e24fc81c-c5ee-47e8-af42-4fe29d895506",
        action="APPROVE",
        eligible_user_ids=["user_e24fc81c-c5ee-47e8-af42-4fe29d895506"],
        eligible_roles=["admin"],
        date=datetime.datetime.fromisoformat(
            "2021-01-01 00:00:00+00:00",
        ),
    )
    """

    upstream_policy_id: typing_extensions.Annotated[
        typing.Optional[ApprovalPolicyId], FieldMetadata(alias="upstreamPolicyId")
    ] = pydantic.Field(default=None)
    """
    The identifier for the upstream policy this slot is associated with.
    """

    upstream_policies_approved: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="upstreamPoliciesApproved")
    ] = pydantic.Field(default=None)
    """
    Whether all upstream policies are approved.
    """

    approval_policy_id: typing_extensions.Annotated[ApprovalPolicyId, FieldMetadata(alias="approvalPolicyId")] = (
        pydantic.Field()
    )
    """
    The identifier for the approval policy this slot is associated with.
    """

    approval_slot_id: typing_extensions.Annotated[ApprovalSlotId, FieldMetadata(alias="approvalSlotId")] = (
        pydantic.Field()
    )
    """
    The identifier for this approval slot
    """

    assigned_user_id: typing_extensions.Annotated[
        typing.Optional[EntityUserId], FieldMetadata(alias="assignedUserId")
    ] = pydantic.Field(default=None)
    """
    The ID of the user who is assigned to the approval slot. If undefined, the approval slot is assigned to all eligible approvers.
    """

    action: ApproverAction
    eligible_roles: typing_extensions.Annotated[typing.List[str], FieldMetadata(alias="eligibleRoles")]
    eligible_user_ids: typing_extensions.Annotated[typing.List[EntityUserId], FieldMetadata(alias="eligibleUserIds")]
    date: dt.datetime = pydantic.Field()
    """
    Either the date the invoice was created, date the approver was assigned, or date of last action by approver, whichever is latest.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
