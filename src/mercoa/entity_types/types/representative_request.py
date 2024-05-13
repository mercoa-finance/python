# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...commons.types.address import Address
from ...commons.types.birth_date import BirthDate
from ...commons.types.full_name import FullName
from ...commons.types.individual_government_id import IndividualGovernmentId
from ...commons.types.phone_number import PhoneNumber
from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import pydantic_v1
from .responsibilities import Responsibilities


class RepresentativeRequest(pydantic_v1.BaseModel):
    """
    Examples
    --------
    from mercoa import (
        Address,
        BirthDate,
        FullName,
        IndividualGovernmentId,
        PhoneNumber,
        RepresentativeRequest,
        Responsibilities,
    )

    RepresentativeRequest(
        name=FullName(
            first_name="John",
            middle_name="Quincy",
            last_name="Adams",
            suffix="Jr.",
        ),
        phone=PhoneNumber(
            country_code="1",
            number="4155551234",
        ),
        email="john.doe@acme.com",
        address=Address(
            address_line_1="123 Main St",
            address_line_2="Unit 1",
            city="San Francisco",
            state_or_province="CA",
            postal_code="94105",
            country="US",
        ),
        birth_date=BirthDate(
            day="1",
            month="1",
            year="1980",
        ),
        government_id=IndividualGovernmentId(
            ssn="123-45-6789",
        ),
        responsibilities=Responsibilities(
            is_owner=True,
            ownership_percentage=40,
            is_controller=True,
        ),
    )
    """

    name: FullName
    phone: PhoneNumber
    email: str
    address: Address
    birth_date: BirthDate = pydantic_v1.Field(alias="birthDate")
    government_id: IndividualGovernmentId = pydantic_v1.Field(alias="governmentID")
    responsibilities: Responsibilities

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
        populate_by_name = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
