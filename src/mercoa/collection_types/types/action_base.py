# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
from .action_id import ActionId
import typing_extensions
import datetime as dt
from ...core.serialization import FieldMetadata
import pydantic
from .action_status import ActionStatus
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class ActionBase(UniversalBaseModel):
    id: ActionId
    scheduled_execution_time: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="scheduledExecutionTime")
    ] = pydantic.Field()
    """
    The UTC timestamp for when this action is scheduled for execution. Actual execution may be delayed by a few minutes due to processing time.
    """

    status: ActionStatus = pydantic.Field()
    """
    The current lifecycle state of the action. SUGGESTED actions are pending approval, APPROVED actions will be executed, and COMPLETED actions have been executed.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
