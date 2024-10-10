# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from .business_type import BusinessType
from ...commons.types.phone_number import PhoneNumber
from ...commons.types.address import Address
from .tax_id import TaxId
from .industry_codes import IndustryCodes
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class BusinessProfileResponse(UniversalBaseModel):
    """
    Examples
    --------
    from mercoa.commons import Address, PhoneNumber
    from mercoa.entity_types import BusinessProfileResponse, Ein, TaxId

    BusinessProfileResponse(
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
        tax_id=TaxId(
            ein=Ein(
                number="12-3456789",
            ),
        ),
        owners_provided=True,
    )
    """

    email: typing.Optional[str] = None
    legal_business_name: str = pydantic.Field(alias="legalBusinessName")
    business_type: typing.Optional[BusinessType] = pydantic.Field(alias="businessType", default=None)
    phone: typing.Optional[PhoneNumber] = None
    doing_business_as: typing.Optional[str] = pydantic.Field(alias="doingBusinessAs", default=None)
    website: typing.Optional[str] = None
    description: typing.Optional[str] = None
    address: typing.Optional[Address] = None
    owners_provided: typing.Optional[bool] = pydantic.Field(alias="ownersProvided", default=None)
    """
    True if all representatives have been provided for this business.
    """

    tax_id_provided: bool = pydantic.Field(alias="taxIDProvided")
    tax_id: typing.Optional[TaxId] = pydantic.Field(alias="taxId", default=None)
    industry_codes: typing.Optional[IndustryCodes] = pydantic.Field(alias="industryCodes", default=None)
    average_monthly_transaction_volume: typing.Optional[float] = pydantic.Field(
        alias="averageMonthlyTransactionVolume", default=None
    )
    average_transaction_size: typing.Optional[float] = pydantic.Field(alias="averageTransactionSize", default=None)
    max_transaction_size: typing.Optional[float] = pydantic.Field(alias="maxTransactionSize", default=None)

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
