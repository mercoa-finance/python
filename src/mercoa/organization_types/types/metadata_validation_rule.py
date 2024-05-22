# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

from ...core.pydantic_utilities import pydantic_v1


class MetadataValidationRule_Regex(pydantic_v1.BaseModel):
    type: typing.Literal["regex"] = "regex"
    regex: str
    error_message: str = pydantic_v1.Field(alias="errorMessage")

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


MetadataValidationRule = typing.Union[MetadataValidationRule_Regex]
