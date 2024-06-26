# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .business_profile_request import BusinessProfileRequest
from .individual_profile_request import IndividualProfileRequest


class ProfileRequest(pydantic_v1.BaseModel):
    """
    Examples
    --------
    from mercoa import (
        Address,
        BusinessProfileRequest,
        Ein,
        PhoneNumber,
        ProfileRequest,
        TaxId,
    )

    ProfileRequest(
        business=BusinessProfileRequest(
            email="customer@acme.com",
            legal_business_name="Acme Inc.",
            website="http://www.acme.com",
            business_type="llc",
            phone=PhoneNumber(
                country_code="1",
                number="4155551234",
            ),
            address=Address(
                address_line_1="123 Main St",
                address_line_2="Unit 1",
                city="San Francisco",
                state_or_province="CA",
                postal_code="94105",
                country="US",
            ),
            tax_id=TaxId(
                ein=Ein(
                    number="12-3456789",
                ),
            ),
        ),
    )
    """

    business: typing.Optional[BusinessProfileRequest] = pydantic_v1.Field(default=None)
    """
    If this entity is a business, set this field
    """

    individual: typing.Optional[IndividualProfileRequest] = pydantic_v1.Field(default=None)
    """
    If this entity is a individual, set this field
    """

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
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
