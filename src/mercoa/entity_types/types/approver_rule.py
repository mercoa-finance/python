# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import pydantic
from .identifier_list import IdentifierList
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class ApproverRule(UniversalBaseModel):
    num_approvers: int = pydantic.Field(alias="numApprovers")
    identifier_list: IdentifierList = pydantic.Field(alias="identifierList")

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
