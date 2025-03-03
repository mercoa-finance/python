# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import pydantic
import typing_extensions
from ...core.serialization import FieldMetadata
import typing
from .counterparty_response import CounterpartyResponse
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class FindCounterpartiesResponse(UniversalBaseModel):
    """
    Examples
    --------
    import datetime

    from mercoa.entity_types import (
        BusinessProfileResponse,
        CounterpartyResponse,
        FindCounterpartiesResponse,
        ProfileResponse,
    )
    from mercoa.payment_method_types import PaymentMethodResponse_BankAccount

    FindCounterpartiesResponse(
        count=1,
        has_more=False,
        data=[
            CounterpartyResponse(
                id="ent_21661ac1-a2a8-4465-a6c0-64474ba8181d",
                foreign_id="MY-DB-ID-90909",
                name="Big Box Store",
                email="vendor@bigboxstore.com",
                accepted_tos=False,
                status="unverified",
                is_customer=False,
                is_payor=False,
                is_payee=True,
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
                        email="vendor@bigboxstore.com",
                        legal_business_name="Big Box Store",
                        business_type="publicCorporation",
                        tax_id_provided=False,
                        owners_provided=False,
                    ),
                ),
                payment_methods=[
                    PaymentMethodResponse_BankAccount(
                        id="pm_7610541f-4619-4033-8620-cfccfb811293",
                        account_name="Vendor Checking Account",
                        bank_name="Chase",
                        routing_number="66554433",
                        account_number="55934059697648",
                        account_type="CHECKING",
                        status="NEW",
                        is_default_source=True,
                        is_default_destination=True,
                        supported_currencies=["USD"],
                        metadata={},
                        frozen=False,
                        created_at=datetime.datetime.fromisoformat(
                            "2021-01-01 00:00:00+00:00",
                        ),
                        updated_at=datetime.datetime.fromisoformat(
                            "2021-01-01 00:00:00+00:00",
                        ),
                    )
                ],
                counterparty_type=["ENTITY"],
            )
        ],
    )
    """

    count: int = pydantic.Field()
    """
    Total number of counterparties for the given filters. This value is not limited by the limit parameter. It is provided so that you can determine how many pages of results are available.
    """

    has_more: typing_extensions.Annotated[bool, FieldMetadata(alias="hasMore")] = pydantic.Field()
    """
    True if there are more counterparties available for the given filters.
    """

    data: typing.List[CounterpartyResponse]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
