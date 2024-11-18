# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import pydantic
from ...entity_types.types.entity_id import EntityId
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class CounterpartyEventWebhook(UniversalBaseModel):
    """
    Examples
    --------
    from mercoa.webhooks import CounterpartyEventWebhook

    CounterpartyEventWebhook(
        event_type="counterparty.onboarding.completed",
        entity_id="ent_21661ac1-a2a8-4465-a6c0-64474ba8181d",
        counterparty_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    )
    """

    event_type: str = pydantic.Field(alias="eventType")
    entity_id: EntityId = pydantic.Field(alias="entityId")
    """
    The ID of the entity that owns the counterparty relationship
    """

    counterparty_id: EntityId = pydantic.Field(alias="counterpartyId")
    """
    The ID of the counterparty
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow