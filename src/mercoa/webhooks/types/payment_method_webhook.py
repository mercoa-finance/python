# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import pydantic
from ...entity_types.types.entity_id import EntityId
from ...payment_method_types.types.payment_method_response import PaymentMethodResponse
from ...entity_types.types.entity_response import EntityResponse
import typing
from ...entity_types.types.entity_user_response import EntityUserResponse
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class PaymentMethodWebhook(UniversalBaseModel):
    """
    Examples
    --------
    import datetime

    from mercoa.commons import Address, PhoneNumber
    from mercoa.entity_types import (
        BusinessProfileResponse,
        EntityResponse,
        EntityUserResponse,
        ProfileResponse,
    )
    from mercoa.payment_method_types import PaymentMethodResponse_BankAccount
    from mercoa.webhooks import PaymentMethodWebhook

    PaymentMethodWebhook(
        event_type="paymentMethod.created",
        entity_id="ent_21661ac1-a2a8-4465-a6c0-64474ba8181d",
        payment_method=PaymentMethodResponse_BankAccount(
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
        ),
        entity=EntityResponse(
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
        ),
        user=EntityUserResponse(
            id="user_ec3aafc8-ea86-408a-a6c1-545497badbbb",
            foreign_id="MY-DB-ID-12345",
            email="john.doe@acme.com",
            name="John Doe",
            roles=["admin", "approver"],
            created_at=datetime.datetime.fromisoformat(
                "2024-01-01 00:00:00+00:00",
            ),
            updated_at=datetime.datetime.fromisoformat(
                "2024-01-01 00:00:00+00:00",
            ),
        ),
    )
    """

    event_type: str = pydantic.Field(alias="eventType")
    entity_id: EntityId = pydantic.Field(alias="entityId")
    payment_method: PaymentMethodResponse = pydantic.Field(alias="paymentMethod")
    entity: EntityResponse
    user: typing.Optional[EntityUserResponse] = pydantic.Field(default=None)
    """
    User who initiated the change.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
