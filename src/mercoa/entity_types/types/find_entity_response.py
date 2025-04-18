# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import pydantic
import typing_extensions
from ...core.serialization import FieldMetadata
import typing
from .entity_with_payment_method_response import EntityWithPaymentMethodResponse
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class FindEntityResponse(UniversalBaseModel):
    """
    Examples
    --------
    import datetime

    from mercoa.commons import Address, PhoneNumber
    from mercoa.entity_types import (
        BusinessProfileResponse,
        Ein,
        EntityWithPaymentMethodResponse,
        FindEntityResponse,
        ProfileResponse,
        TaxId,
    )
    from mercoa.payment_method_types import PaymentMethodResponse_BankAccount

    FindEntityResponse(
        count=1,
        has_more=False,
        data=[
            EntityWithPaymentMethodResponse(
                id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
                foreign_id="MY-DB-ID-12345",
                name="Acme Inc.",
                email="customer@acme.com",
                accepted_tos=True,
                status="verified",
                is_customer=True,
                is_payor=True,
                is_payee=False,
                is_network_payor=False,
                is_network_payee=False,
                account_type="business",
                updated_at=datetime.datetime.fromisoformat(
                    "2024-01-02 00:00:00+00:00",
                ),
                created_at=datetime.datetime.fromisoformat(
                    "2024-01-01 00:00:00+00:00",
                ),
                profile=ProfileResponse(
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
                        tax_id=TaxId(
                            ein=Ein(
                                number="12-3456789",
                            ),
                        ),
                        owners_provided=True,
                    ),
                ),
                payment_methods=[
                    PaymentMethodResponse_BankAccount(
                        id="pm_4794d597-70dc-4fec-b6ec-c5988e759769",
                        account_name="My Checking Account",
                        bank_name="Chase",
                        routing_number="12345678",
                        account_number="99988767623",
                        account_type="CHECKING",
                        status="VERIFIED",
                        is_default_source=True,
                        is_default_destination=True,
                        supported_currencies=["USD"],
                        metadata={},
                        frozen=False,
                        confirmed_by_entity=True,
                        created_at=datetime.datetime.fromisoformat(
                            "2021-01-01 00:00:00+00:00",
                        ),
                        updated_at=datetime.datetime.fromisoformat(
                            "2021-01-01 00:00:00+00:00",
                        ),
                    )
                ],
            )
        ],
    )
    """

    count: int = pydantic.Field()
    """
    Total number of entities for the given filters. This value is not limited by the limit parameter. It is provided so that you can determine how many pages of results are available.
    """

    has_more: typing_extensions.Annotated[bool, FieldMetadata(alias="hasMore")] = pydantic.Field()
    """
    True if there are more entities available for the given filters.
    """

    data: typing.List[EntityWithPaymentMethodResponse]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
