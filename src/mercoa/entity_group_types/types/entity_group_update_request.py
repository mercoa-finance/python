# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class EntityGroupUpdateRequest(UniversalBaseModel):
    """
    Examples
    --------
    from mercoa.entity_group_types import EntityGroupUpdateRequest

    EntityGroupUpdateRequest(
        foreign_id="your-group-id",
        name="AcmeConglomerate",
        email_to_name="acmegroup",
    )
    """

    foreign_id: typing.Optional[str] = pydantic.Field(alias="foreignId", default=None)
    name: typing.Optional[str] = None
    email_to_name: typing.Optional[str] = pydantic.Field(alias="emailToName", default=None)
    metadata: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    Metadata key/value pairs to associate with this group. Will overwrite existing metadata.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow