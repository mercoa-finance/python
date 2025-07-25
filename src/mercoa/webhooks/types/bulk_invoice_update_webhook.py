# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing_extensions
from ...core.serialization import FieldMetadata
import pydantic
import typing
from ...invoice_types.types.bulk_invoice_update_from_object_response import (
    BulkInvoiceUpdateFromObjectResponse,
)
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class BulkInvoiceUpdateWebhook(UniversalBaseModel):
    """
    Examples
    --------
    from mercoa.invoice_types import BulkInvoiceUpdateFromObjectResponse
    from mercoa.webhooks import BulkInvoiceUpdateWebhook

    BulkInvoiceUpdateWebhook(
        event_type="invoice.bulk.updated",
        data=[
            BulkInvoiceUpdateFromObjectResponse(
                id="ent_21661ac1-a2a8-4465-a6c0-64474ba8181d",
                foreign_id="YOUR-INVOICE-ID",
            ),
            BulkInvoiceUpdateFromObjectResponse(
                error="Invoice update failed",
                foreign_id="YOUR-SECOND-INVOICE-ID",
            ),
        ],
    )
    """

    event_type: typing_extensions.Annotated[str, FieldMetadata(alias="eventType")] = pydantic.Field()
    """
    The type of the event.
    """

    data: typing.List[BulkInvoiceUpdateFromObjectResponse] = pydantic.Field()
    """
    A list of bulk invoice update responses.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
