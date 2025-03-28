# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import pydantic
import typing_extensions
from ...core.serialization import FieldMetadata
import typing
from .entity_user_response import EntityUserResponse
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class FindEntityUserResponse(UniversalBaseModel):
    """
    Examples
    --------
    import datetime

    from mercoa.entity_types import EntityUserResponse, FindEntityUserResponse

    FindEntityUserResponse(
        count=1,
        has_more=False,
        data=[
            EntityUserResponse(
                id="user_ec3aafc8-ea86-408a-a6c1-545497badbbb",
                foreign_id="MY-DB-ID-12345",
                email="john.doe@acme.com",
                name="John Doe",
                roles=["admin", "approver"],
                created_at=datetime.datetime.fromisoformat(
                    "2024-01-01 00:00:00+00:00",
                ),
                updated_at=datetime.datetime.fromisoformat(
                    "2024-01-01 00:00:00+00:00",
                ),
            )
        ],
    )
    """

    count: int = pydantic.Field()
    """
    Total number of users for the given filters. This value is not limited by the limit parameter. It is provided so that you can determine how many pages of results are available.
    """

    has_more: typing_extensions.Annotated[bool, FieldMetadata(alias="hasMore")] = pydantic.Field()
    """
    True if there are more users available for the given filters.
    """

    data: typing.List[EntityUserResponse]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
