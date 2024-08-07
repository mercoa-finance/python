# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .counterparty_response import CounterpartyResponse


class FindCounterpartiesResponse(pydantic_v1.BaseModel):
    """
    Examples
    --------
    import datetime

    from mercoa import (
        BusinessProfileResponse,
        CounterpartyResponse,
        FindCounterpartiesResponse,
        PaymentMethodResponse_BankAccount,
        ProfileResponse,
    )

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

    count: int = pydantic_v1.Field()
    """
    Total number of counterparties for the given filters. This value is not limited by the limit parameter. It is provided so that you can determine how many pages of results are available.
    """

    has_more: bool = pydantic_v1.Field(alias="hasMore")
    """
    True if there are more counterparties available for the given filters.
    """

    data: typing.List[CounterpartyResponse]

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
