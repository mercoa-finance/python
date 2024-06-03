# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .notification_response import NotificationResponse


class FindNotificationResponse(pydantic_v1.BaseModel):
    """
    Examples
    --------
    import datetime

    from mercoa import FindNotificationResponse, NotificationResponse

    FindNotificationResponse(
        count=2,
        has_more=False,
        data=[
            NotificationResponse(
                id="notif_7df2974a-4069-454c-912f-7e58ebe030fb",
                invoice_id="inv_26e7b5d3-a739-4b23-9ad9-6aaa085f47a9",
                type="INVOICE_APPROVAL_NEEDED",
                created_at=datetime.datetime.fromisoformat(
                    "2024-01-01 00:00:00+00:00",
                ),
            ),
            NotificationResponse(
                id="notif_958c4ffb-dc06-494c-a0e0-1b4946c6bb0f",
                invoice_id="inv_26e7b5d3-a739-4b23-9ad9-6aaa085f47a9",
                type="INVOICE_APPROVED",
                created_at=datetime.datetime.fromisoformat(
                    "2024-01-01 00:00:00+00:00",
                ),
            ),
        ],
    )
    """

    count: int = pydantic_v1.Field()
    """
    Total number of notifications for the given start and end date filters. This value is not limited by the limit parameter. It is provided so that you can determine how many pages of results are available.
    """

    has_more: bool = pydantic_v1.Field(alias="hasMore")
    """
    True if there are more notifications available for the given start and end date filters.
    """

    data: typing.List[NotificationResponse]

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
