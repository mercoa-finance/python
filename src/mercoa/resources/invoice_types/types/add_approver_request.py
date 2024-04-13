# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...entity_types.types.entity_user_id import EntityUserId
from .approval_slot_id import ApprovalSlotId

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class AddApproverRequest(pydantic.BaseModel):
    approval_slot_id: typing.Optional[ApprovalSlotId] = pydantic.Field(
        alias="approvalSlotId",
        default=None,
        description="The identifier for the approval slot this user is assigned to.",
    )
    user_id: EntityUserId = pydantic.Field(alias="userId")

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
        json_encoders = {dt.datetime: serialize_datetime}
