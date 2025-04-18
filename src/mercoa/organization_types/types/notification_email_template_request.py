# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ...core.serialization import FieldMetadata
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class NotificationEmailTemplateRequest(UniversalBaseModel):
    background_style: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="backgroundStyle")] = None
    header: typing.Optional[str] = None
    body: typing.Optional[str] = None
    signature: typing.Optional[str] = None
    footer: typing.Optional[str] = None
    button: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
