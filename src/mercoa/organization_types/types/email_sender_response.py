# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
from .email_sender_provider import EmailSenderProvider
import typing_extensions
from ...core.serialization import FieldMetadata
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import typing
import pydantic


class EmailSenderResponse(UniversalBaseModel):
    provider: EmailSenderProvider
    from_email: typing_extensions.Annotated[str, FieldMetadata(alias="fromEmail")]
    from_name: typing_extensions.Annotated[str, FieldMetadata(alias="fromName")]
    has_api_key: typing_extensions.Annotated[bool, FieldMetadata(alias="hasApiKey")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
