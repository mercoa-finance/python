# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import pydantic
import typing_extensions
from ...core.serialization import FieldMetadata
import typing
from .vendor_credit_response import VendorCreditResponse
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class FindVendorCreditResponse(UniversalBaseModel):
    """
    Examples
    --------
    import datetime

    from mercoa.vendor_credit_types import (
        FindVendorCreditResponse,
        VendorCreditResponse,
    )

    FindVendorCreditResponse(
        count=1,
        has_more=False,
        data=[
            VendorCreditResponse(
                id="vcr_c3f4c87d-794d-4543-9562-575cdddfc0d7",
                total_amount=100.0,
                remaining_amount=100.0,
                currency="USD",
                vendor_id="ent_21661ac1-a2a8-4465-a6c0-64474ba8181d",
                payer_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
                creator_entity_id="ent_21661ac1-a2a8-4465-a6c0-64474ba8181d",
                note="This is a note",
                invoice_ids=["in_26e7b5d3-a739-4b23-9ad9-6aaa085f47a9"],
                created_at=datetime.datetime.fromisoformat(
                    "2021-01-01 00:00:00+00:00",
                ),
                updated_at=datetime.datetime.fromisoformat(
                    "2021-01-01 00:00:00+00:00",
                ),
            )
        ],
    )
    """

    count: int = pydantic.Field()
    """
    Total number of vendor credits for the given filters. This value is not limited by the limit parameter. It is provided so that you can determine how many pages of results are available.
    """

    has_more: typing_extensions.Annotated[bool, FieldMetadata(alias="hasMore")] = pydantic.Field()
    """
    True if there are more vendor credits available for the given filters.
    """

    data: typing.List[VendorCreditResponse]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
