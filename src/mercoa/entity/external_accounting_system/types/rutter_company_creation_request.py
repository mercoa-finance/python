# This file was auto-generated by Fern from our API Definition.

from ....core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ....core.serialization import FieldMetadata
import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2


class RutterCompanyCreationRequest(UniversalBaseModel):
    access_token: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="accessToken")] = (
        pydantic.Field(default=None)
    )
    """
    The access token for the existing Rutter connection. If the connection does not exist, leave this field blank and Rutter will create a new connection.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
