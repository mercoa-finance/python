# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
from .business_profile_response import BusinessProfileResponse
import pydantic
from .individual_profile_response import IndividualProfileResponse
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class ProfileResponse(UniversalBaseModel):
    """
    Examples
    --------
    from mercoa.commons import Address, PhoneNumber
    from mercoa.entity_types import BusinessProfileResponse, ProfileResponse

    ProfileResponse(
        business=BusinessProfileResponse(
            email="customer@acme.com",
            legal_business_name="Acme Inc.",
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
            tax_id_provided=True,
            owners_provided=True,
        ),
    )
    """

    business: typing.Optional[BusinessProfileResponse] = pydantic.Field(default=None)
    """
    Will be set if the entity is a business
    """

    individual: typing.Optional[IndividualProfileResponse] = pydantic.Field(default=None)
    """
    Will be set if the entity is a individual
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
