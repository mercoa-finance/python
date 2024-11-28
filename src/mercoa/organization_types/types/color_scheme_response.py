# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class ColorSchemeResponse(UniversalBaseModel):
    primary_color: typing.Optional[str] = pydantic.Field(alias="primaryColor", default=None)
    secondary_color: typing.Optional[str] = pydantic.Field(alias="secondaryColor", default=None)
    logo_background_color: typing.Optional[str] = pydantic.Field(alias="logoBackgroundColor", default=None)
    rounded_corners: typing.Optional[int] = pydantic.Field(alias="roundedCorners", default=None)
    font_family: typing.Optional[str] = pydantic.Field(alias="fontFamily", default=None)
    font_size: typing.Optional[str] = pydantic.Field(alias="fontSize", default=None)

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
