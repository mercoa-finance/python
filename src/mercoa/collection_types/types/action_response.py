# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ...core.pydantic_utilities import UniversalBaseModel
import typing
from .action_id import ActionId
import datetime as dt
import pydantic
from .action_status import ActionStatus
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class ActionResponse_Email(UniversalBaseModel):
    """
    Examples
    --------
    import datetime

    from mercoa.collection_types import ActionResponse_Email

    ActionResponse_Email(
        id="act_c3881909-c2f8-4a1e-878a-80a9b594483c",
        subject="Invoice Past Due - Please Review",
        body="Your invoice is now 3 days past due. Please make a payment at your earliest convenience.",
        scheduled_execution_time=datetime.datetime.fromisoformat(
            "2024-01-04 13:00:00+00:00",
        ),
        status="SUGGESTED",
    )
    """

    type: typing.Literal["email"] = "email"
    subject: str
    body: str
    id: ActionId
    scheduled_execution_time: dt.datetime = pydantic.Field(alias="scheduledExecutionTime")
    status: ActionStatus

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


"""
import datetime

from mercoa.collection_types import ActionResponse_Email

ActionResponse_Email(
    id="act_c3881909-c2f8-4a1e-878a-80a9b594483c",
    subject="Invoice Past Due - Please Review",
    body="Your invoice is now 3 days past due. Please make a payment at your earliest convenience.",
    scheduled_execution_time=datetime.datetime.fromisoformat(
        "2024-01-04 13:00:00+00:00",
    ),
    status="SUGGESTED",
)
"""
ActionResponse = ActionResponse_Email
