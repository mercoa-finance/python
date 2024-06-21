# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .approval_policy_id import ApprovalPolicyId
from .rule import Rule
from .trigger import Trigger


class ApprovalPolicyResponse(pydantic_v1.BaseModel):
    """
    Examples
    --------
    import datetime

    from mercoa import (
        ApprovalPolicyResponse,
        IdentifierList_RolesList,
        Rule_Approver,
        Trigger_Amount,
    )

    ApprovalPolicyResponse(
        id="apvl_8545a84e-a45f-41bf-bdf1-33b42a55812c",
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
        updated_at=datetime.datetime.fromisoformat(
            "2024-01-02 00:00:00+00:00",
        ),
        created_at=datetime.datetime.fromisoformat(
            "2024-01-01 00:00:00+00:00",
        ),
    )
    """

    id: ApprovalPolicyId
    trigger: typing.List[Trigger]
    rule: Rule
    upstream_policy_id: ApprovalPolicyId = pydantic_v1.Field(alias="upstreamPolicyId")
    created_at: dt.datetime = pydantic_v1.Field(alias="createdAt")
    updated_at: dt.datetime = pydantic_v1.Field(alias="updatedAt")

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
