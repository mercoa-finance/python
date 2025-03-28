# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ...core.pydantic_utilities import UniversalBaseModel
import typing
import typing_extensions
from ...core.serialization import FieldMetadata
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class ExternalAccountingSystemProviderRequest_None(UniversalBaseModel):
    type: typing.Literal["none"] = "none"
    api_key: typing_extensions.Annotated[str, FieldMetadata(alias="apiKey")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ExternalAccountingSystemProviderRequest_Codat(UniversalBaseModel):
    type: typing.Literal["codat"] = "codat"
    api_key: typing_extensions.Annotated[str, FieldMetadata(alias="apiKey")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ExternalAccountingSystemProviderRequest_Rutter(UniversalBaseModel):
    type: typing.Literal["rutter"] = "rutter"
    client_id: typing_extensions.Annotated[str, FieldMetadata(alias="clientId")]
    client_secret: typing_extensions.Annotated[str, FieldMetadata(alias="clientSecret")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ExternalAccountingSystemProviderRequest = typing.Union[
    ExternalAccountingSystemProviderRequest_None,
    ExternalAccountingSystemProviderRequest_Codat,
    ExternalAccountingSystemProviderRequest_Rutter,
]
