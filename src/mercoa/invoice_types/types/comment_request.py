# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ...entity_types.types.entity_user_id import EntityUserId
from ...core.serialization import FieldMetadata
import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class CommentRequest(UniversalBaseModel):
    """
    Examples
    --------
    from mercoa.invoice_types import CommentRequest

    CommentRequest(
        text="This is a comment",
        user_id="user_e24fc81c-c5ee-47e8-af42-4fe29d895506",
    )
    """

    text: str
    user_id: typing_extensions.Annotated[typing.Optional[EntityUserId], FieldMetadata(alias="userId")] = pydantic.Field(
        default=None
    )
    """
    The ID or the Foreign ID of the user who created the comment.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
