# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
import typing_extensions
import datetime as dt
from ...core.serialization import FieldMetadata
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class InvoiceLineItemIndividualUpdateRequest(UniversalBaseModel):
    """
    Examples
    --------
    import datetime

    from mercoa.invoice_types import InvoiceLineItemIndividualUpdateRequest

    InvoiceLineItemIndividualUpdateRequest(
        name="Product A",
        description="Product A",
        service_start_date=datetime.datetime.fromisoformat(
            "2021-01-01 00:00:00+00:00",
        ),
        service_end_date=datetime.datetime.fromisoformat(
            "2021-01-31 00:00:00+00:00",
        ),
        metadata={"key1": "value1", "key2": "value2"},
        gl_account_id="600394",
    )
    """

    name: typing.Optional[str] = None
    description: typing.Optional[str] = None
    category: typing.Optional[str] = pydantic.Field(default=None)
    """
    Category of the line item.
    """

    service_start_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="serviceStartDate")
    ] = None
    service_end_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="serviceEndDate")
    ] = None
    metadata: typing.Optional[typing.Dict[str, str]] = None
    gl_account_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="glAccountId")] = (
        pydantic.Field(default=None)
    )
    """
    ID of general ledger account associated with this line item.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
