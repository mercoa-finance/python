# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class UserNotificationPolicyRequest(UniversalBaseModel):
    """
    Examples
    --------
    from mercoa.entity_types import UserNotificationPolicyRequest

    UserNotificationPolicyRequest(
        disabled=True,
    )
    """

    disabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Set to true if the selected notification type should be disabled for this user
    """

    digest: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Set to true if the selected notification type should be sent as a digest. Default is false.
    """

    immediate: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Set to true if the selected notification type should be sent immediately. Default is true.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
