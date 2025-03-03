# This file was auto-generated by Fern from our API Definition.

from .invoice_request_base import InvoiceRequestBase
import typing_extensions
import typing
from .invoice_line_item_creation_request import InvoiceLineItemCreationRequest
from ...core.serialization import FieldMetadata
from ...entity_types.types.entity_id import EntityId
import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class InvoiceCreationWithEntityRequest(InvoiceRequestBase):
    """
    Examples
    --------
    import datetime

    from mercoa.invoice_types import (
        InvoiceCreationWithEntityRequest,
        InvoiceLineItemCreationRequest,
        PaymentDestinationOptions_Check,
    )

    InvoiceCreationWithEntityRequest(
        status="NEW",
        amount=100.0,
        currency="USD",
        invoice_date=datetime.datetime.fromisoformat(
            "2021-01-01 00:00:00+00:00",
        ),
        due_date=datetime.datetime.fromisoformat(
            "2021-01-31 00:00:00+00:00",
        ),
        invoice_number="INV-123",
        note_to_self="For the month of January",
        payer_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
        payment_source_id="pm_4794d597-70dc-4fec-b6ec-c5988e759769",
        vendor_id="ent_21661ac1-a2a8-4465-a6c0-64474ba8181d",
        payment_destination_id="pm_5fde2f4a-facc-48ef-8f0d-6b7d087c7b18",
        payment_destination_options=PaymentDestinationOptions_Check(
            delivery="MAIL",
            print_description=True,
        ),
        line_items=[
            InvoiceLineItemCreationRequest(
                amount=100.0,
                currency="USD",
                description="Product A",
                name="Product A",
                quantity=1.0,
                unit_price=100.0,
                category="EXPENSE",
                service_start_date=datetime.datetime.fromisoformat(
                    "2021-01-01 00:00:00+00:00",
                ),
                service_end_date=datetime.datetime.fromisoformat(
                    "2021-01-31 00:00:00+00:00",
                ),
                metadata={"key1": "value1", "key2": "value2"},
                gl_account_id="600394",
            )
        ],
        creator_entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
        creator_user_id="user_e24fc81c-c5ee-47e8-af42-4fe29d895506",
    )
    """

    line_items: typing_extensions.Annotated[
        typing.Optional[typing.List[InvoiceLineItemCreationRequest]], FieldMetadata(alias="lineItems")
    ] = None
    creator_entity_id: typing_extensions.Annotated[EntityId, FieldMetadata(alias="creatorEntityId")] = pydantic.Field()
    """
    ID of the entity who created this invoice.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
