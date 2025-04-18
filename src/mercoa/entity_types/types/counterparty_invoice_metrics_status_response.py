# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
from ...invoice_types.types.invoice_status import InvoiceStatus
import typing_extensions
from ...core.serialization import FieldMetadata
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import typing
import pydantic


class CounterpartyInvoiceMetricsStatusResponse(UniversalBaseModel):
    """
    Examples
    --------
    from mercoa.entity_types import CounterpartyInvoiceMetricsStatusResponse

    CounterpartyInvoiceMetricsStatusResponse(
        status="PAID",
        total_count=10,
        total_amount=1000.0,
    )
    """

    status: InvoiceStatus
    total_count: typing_extensions.Annotated[int, FieldMetadata(alias="totalCount")]
    total_amount: typing_extensions.Annotated[float, FieldMetadata(alias="totalAmount")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
