# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...commons.types.address import Address
from ...commons.types.phone_number import PhoneNumber
from .business_type import BusinessType
from .tax_id import TaxId

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class BusinessProfileRequest(pydantic.BaseModel):
    """
    from mercoa import (
        Address,
        BusinessProfileRequest,
        BusinessType,
        Ein,
        PhoneNumber,
        TaxId,
    )

    BusinessProfileRequest(
        email="customer@acme.com",
        legal_business_name="Acme Inc.",
        website="http://www.acme.com",
        business_type=BusinessType.LLC,
        phone=PhoneNumber(
            country_code="1",
            number="4155551234",
        ),
        address=Address(
            address_line_1="123 Main St",
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
    )
    """

    email: typing.Optional[str] = pydantic.Field(
        default=None, description="Email address for the business. Required for KYB."
    )
    legal_business_name: str = pydantic.Field(alias="legalBusinessName")
    business_type: typing.Optional[BusinessType] = pydantic.Field(alias="businessType", default=None)
    phone: typing.Optional[PhoneNumber] = pydantic.Field(
        default=None, description="Phone number for the business. Required for KYB."
    )
    doing_business_as: typing.Optional[str] = pydantic.Field(alias="doingBusinessAs", default=None)
    website: typing.Optional[str] = pydantic.Field(
        default=None,
        description="Website URL for the business. Must be in the format http://www.example.com. Required for KYB if description is not provided.",
    )
    description: typing.Optional[str] = pydantic.Field(
        default=None, description="Description of the business. Required for KYB if website is not provided."
    )
    address: typing.Optional[Address] = pydantic.Field(
        default=None, description="Address for the business. Required for KYB."
    )
    tax_id: typing.Optional[TaxId] = pydantic.Field(
        alias="taxId",
        default=None,
        description="Tax ID for the business. Currently only EIN is supported. Required for KYB.",
    )
    formation_date: typing.Optional[dt.datetime] = pydantic.Field(
        alias="formationDate", default=None, description="Date of business formation"
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
