# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
from .bulk_invoice_creation_from_object_response import (
    BulkInvoiceCreationFromObjectResponse,
)
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class BulkInvoiceCreationResponse(UniversalBaseModel):
    """
    Examples
    --------
    from mercoa.invoice_types import (
        BulkInvoiceCreationFromObjectResponse,
        BulkInvoiceCreationResponse,
    )

    BulkInvoiceCreationResponse(
        data=[
            BulkInvoiceCreationFromObjectResponse(
                id="ent_21661ac1-a2a8-4465-a6c0-64474ba8181d",
                foreign_id="YOUR-INVOICE-ID",
            ),
            BulkInvoiceCreationFromObjectResponse(
                error="Invoice creation failed",
                foreign_id="YOUR-SECOND-INVOICE-ID",
            ),
        ],
    )
    """

    data: typing.List[BulkInvoiceCreationFromObjectResponse]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
