# This file was auto-generated by Fern from our API Definition.

from .process_payment_gateway_card_details_base import (
    ProcessPaymentGatewayCardDetailsBase,
)
import typing_extensions
from ...core.serialization import FieldMetadata
import pydantic
import typing
from .ephemeral_key_endpoint import EphemeralKeyEndpoint
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class ProcessPaymentGatewayCardDetailsStripeIssuing(ProcessPaymentGatewayCardDetailsBase):
    """
    Examples
    --------
    from mercoa.payment_gateway_types import (
        EphemeralKeyEndpoint,
        ProcessPaymentGatewayCardDetailsStripeIssuing,
    )

    ProcessPaymentGatewayCardDetailsStripeIssuing(
        first_name="John",
        last_name="Doe",
        postal_code="12345",
        country="US",
        stripe_card_id="ic_1234567890abcdef",
        stripe_publishable_key="pk_test_1234567890abcdef",
        ephemeral_key_endpoint=EphemeralKeyEndpoint(
            url="https://api.example.com/ephemeral-keys",
            method="POST",
            headers={
                "Authorization": "Bearer YOUR_AUTH_SCHEME",
                "Content-Type": "application/json",
            },
            post_body='{"card_id": "{{cardId}}", "nonce": "{{nonce}}", "account_id": "{{accountId}}"}',
        ),
    )
    """

    stripe_card_id: typing_extensions.Annotated[str, FieldMetadata(alias="stripeCardId")] = pydantic.Field()
    """
    The Stripe Issuing card ID
    """

    stripe_publishable_key: typing_extensions.Annotated[str, FieldMetadata(alias="stripePublishableKey")] = (
        pydantic.Field()
    )
    """
    The Stripe publishable key for the Issuing Elements
    """

    stripe_account_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="stripeAccountId")] = (
        pydantic.Field(default=None)
    )
    """
    The Stripe account ID (optional, used for connected accounts)
    """

    ephemeral_key_endpoint: typing_extensions.Annotated[
        EphemeralKeyEndpoint, FieldMetadata(alias="ephemeralKeyEndpoint")
    ] = pydantic.Field()
    """
    The endpoint configuration for generating ephemeral keys. Expects a JSON response with a `ephemeralKeySecret` field.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
