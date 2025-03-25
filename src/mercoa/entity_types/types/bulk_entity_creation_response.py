# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
from .bulk_entity_creation_from_object_response import (
    BulkEntityCreationFromObjectResponse,
)
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class BulkEntityCreationResponse(UniversalBaseModel):
    """
    Examples
    --------
    from mercoa.entity_types import (
        BulkEntityCreationFromObjectResponse,
        BulkEntityCreationResponse,
    )

    BulkEntityCreationResponse(
        data=[
            BulkEntityCreationFromObjectResponse(
                id="ent_21661ac1-a2a8-4465-a6c0-64474ba8181d",
                foreign_id="YOUR-ENTITY-ID",
            ),
            BulkEntityCreationFromObjectResponse(
                error="Entity creation failed",
                foreign_id="YOUR-SECOND-ENTITY-ID",
            ),
        ],
    )
    """

    data: typing.List[BulkEntityCreationFromObjectResponse]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
