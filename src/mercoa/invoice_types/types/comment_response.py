# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from ...entity_types.types.entity_user_response import EntityUserResponse
from .associated_approval_action import AssociatedApprovalAction


class CommentResponse(pydantic_v1.BaseModel):
    """
    Examples
    --------
    import datetime

    from mercoa import CommentResponse, EntityUserResponse

    CommentResponse(
        id="ic_b3525b66-da94-4525-9f31-426bcf657128",
        text="This is a comment",
        user=EntityUserResponse(
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
        ),
        created_at=datetime.datetime.fromisoformat(
            "2021-01-01 00:00:00+00:00",
        ),
        updated_at=datetime.datetime.fromisoformat(
            "2021-01-01 00:00:00+00:00",
        ),
    )
    """

    id: str
    text: str
    user: typing.Optional[EntityUserResponse] = None
    associated_approval_action: typing.Optional[AssociatedApprovalAction] = pydantic_v1.Field(
        alias="associatedApprovalAction", default=None
    )
    """
    If an approval action has triggered the generation of this comment, returns the associated approval action and actor
    """

    created_at: dt.datetime = pydantic_v1.Field(alias="createdAt")
    updated_at: dt.datetime = pydantic_v1.Field(alias="updatedAt")

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
        allow_population_by_field_name = True
        populate_by_name = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
