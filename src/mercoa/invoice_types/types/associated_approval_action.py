# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import pydantic_v1
from ...entity_types.types.entity_user_id import EntityUserId
from .approver_action import ApproverAction


class AssociatedApprovalAction(pydantic_v1.BaseModel):
    """
    Examples
    --------
    from mercoa import AssociatedApprovalAction

    AssociatedApprovalAction(
        user_id="user_e24fc81c-c5ee-47e8-af42-4fe29d895506",
        action="APPROVE",
    )
    """

    user_id: EntityUserId = pydantic_v1.Field(alias="userId")
    action: ApproverAction

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
