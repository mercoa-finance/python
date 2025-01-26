# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import pydantic
from ...entity_types.types.entity_id import EntityId
import typing
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class EntityMetadataUpdatedWebhook(UniversalBaseModel):
    """
    Examples
    --------
    from mercoa.webhooks import EntityMetadataUpdatedWebhook

    EntityMetadataUpdatedWebhook(
        event_type="entity.metadata.updated",
        entity_id="ent_21661ac1-a2a8-4465-a6c0-64474ba8181d",
        foreign_id="your_id_1234567890",
        key="my_custom_field",
        value=["my_value", "my_second_value"],
    )
    """

    event_type: str = pydantic.Field(alias="eventType")
    entity_id: EntityId = pydantic.Field(alias="entityId")
    foreign_id: typing.Optional[str] = pydantic.Field(alias="foreignId", default=None)
    key: str
    value: typing.List[str]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
