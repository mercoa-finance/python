# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import pydantic_v1
from .approval_policy_id import ApprovalPolicyId
from .rule import Rule
from .trigger import Trigger


class ApprovalPolicyRequest(pydantic_v1.BaseModel):
    """
    Examples
    --------
    from mercoa import (
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

    trigger: typing.List[Trigger] = pydantic_v1.Field()
    """
    List of triggers that will cause this policy to be evaluated. If no triggers are provided, the policy will be evaluated for all invoices.
    """

    rule: Rule
    upstream_policy_id: ApprovalPolicyId = pydantic_v1.Field(alias="upstreamPolicyId")
    """
    The policy ID of the previous approval policy in the chain of policies. Use 'root' if no upstreamPolicyId is intended to be set.
    """

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
