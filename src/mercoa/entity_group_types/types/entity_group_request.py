# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
from ...entity_types.types.entity_id import EntityId
import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class EntityGroupRequest(UniversalBaseModel):
    """
    Examples
    --------
    from mercoa.entity_group_types import EntityGroupRequest

    EntityGroupRequest(
        foreign_id="your-group-id",
        name="AcmeConglomerate",
        email_to_name="acmegroup",
        entity_ids=[
            "ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
            "ent_21661ac1-a2a8-4465-a6c0-64474ba8181d",
        ],
    )
    """

    entity_ids: typing.List[EntityId] = pydantic.Field(alias="entityIds")
    foreign_id: typing.Optional[str] = pydantic.Field(alias="foreignId", default=None)
    name: typing.Optional[str] = None
    email_to_name: typing.Optional[str] = pydantic.Field(alias="emailToName", default=None)

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
