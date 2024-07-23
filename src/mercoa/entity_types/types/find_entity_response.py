# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .entity_with_payment_method_response import EntityWithPaymentMethodResponse


class FindEntityResponse(pydantic_v1.BaseModel):
    """
    Examples
    --------
    import datetime

    from mercoa import (
        Address,
        BusinessProfileResponse,
        EntityWithPaymentMethodResponse,
        FindEntityResponse,
        PaymentMethodResponse_BankAccount,
        PhoneNumber,
        ProfileResponse,
    )

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

    count: int = pydantic_v1.Field()
    """
    Total number of entities for the given filters. This value is not limited by the limit parameter. It is provided so that you can determine how many pages of results are available.
    """

    has_more: bool = pydantic_v1.Field(alias="hasMore")
    """
    True if there are more entities available for the given filters.
    """

    data: typing.List[EntityWithPaymentMethodResponse]

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
