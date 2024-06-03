# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1


class Address(pydantic_v1.BaseModel):
    """
    Examples
    --------
    from mercoa import Address

    Address(
        address_line_1="123 Main St",
        address_line_2="Unit 1",
        city="San Francisco",
        state_or_province="CA",
        postal_code="94105",
        country="US",
    )
    """

    address_line_1: str = pydantic_v1.Field(alias="addressLine1")
    address_line_2: typing.Optional[str] = pydantic_v1.Field(alias="addressLine2", default=None)
    city: str
    state_or_province: str = pydantic_v1.Field(alias="stateOrProvince")
    """
    State or province code. Must be in the format XX.
    """

    postal_code: str = pydantic_v1.Field(alias="postalCode")
    """
    Postal code. Must be in the format XXXXX or XXXXX-XXXX.
    """

    country: typing.Optional[str] = None

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
