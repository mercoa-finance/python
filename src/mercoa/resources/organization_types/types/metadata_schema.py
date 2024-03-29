# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .metadata_show_conditions import MetadataShowConditions
from .metadata_type import MetadataType

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class MetadataSchema(pydantic.BaseModel):
    key: str
    display_name: str = pydantic.Field(alias="displayName")
    description: typing.Optional[str] = None
    line_item: typing.Optional[bool] = pydantic.Field(
        alias="lineItem",
        default=None,
        description="Whether or not this field should be shown on line items. If true, this field will be shown on each line item. If false, the field will be shown on the invoice level. Defaults to false.",
    )
    type: MetadataType
    allow_multiple: typing.Optional[bool] = pydantic.Field(
        alias="allowMultiple",
        default=None,
        description="Whether or not multiple values are allowed for this field. Defaults to false. If true, the value will be a list of the specified type.",
    )
    show_conditions: typing.Optional[MetadataShowConditions] = pydantic.Field(
        alias="showConditions",
        default=None,
        description="A list of conditional rules that determine whether or not this field should be shown. The field will only be shown if all of the conditions are met. If no conditions are specified, the field will always be shown.",
    )

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
