# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .counterparty_customization_request import CounterpartyCustomizationRequest
from .entity_id import EntityId


class EntityAddPayorsRequest(pydantic_v1.BaseModel):
    """
    Examples
    --------
    from mercoa import CounterpartyCustomizationRequest, EntityAddPayorsRequest

    EntityAddPayorsRequest(
        payors=["ent_21661ac1-a2a8-4465-a6c0-64474ba8181d"],
        customizations=[
            CounterpartyCustomizationRequest(
                counterparty_id="ent_21661ac1-a2a8-4465-a6c0-64474ba8181d",
                account_id="85866843",
            )
        ],
    )
    """

    payors: typing.List[EntityId] = pydantic_v1.Field()
    """
    List of payor entity IDs to associate with the entity
    """

    customizations: typing.Optional[typing.List[CounterpartyCustomizationRequest]] = pydantic_v1.Field(default=None)
    """
    List of customizations to apply to the payors. If the payor is not currently a counterparty of the entity, the counterparty will be created with the provided customizations.
    """

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
