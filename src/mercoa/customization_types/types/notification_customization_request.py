# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ...core.serialization import FieldMetadata
import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class NotificationCustomizationRequest(UniversalBaseModel):
    """
    Examples
    --------
    from mercoa.customization_types import NotificationCustomizationRequest

    NotificationCustomizationRequest(
        assume_role="admin",
    )
    """

    assume_role: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="assumeRole")] = pydantic.Field(
        default=None
    )
    """
    If set, notifications to this role will be sent to the email address of the entity. Set as empty string to disable.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
