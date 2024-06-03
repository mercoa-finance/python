# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .email_log import EmailLog


class EmailLogResponse(pydantic_v1.BaseModel):
    """
    Examples
    --------
    import datetime

    from mercoa import EmailLog, EmailLogResponse

    EmailLogResponse(
        count=1,
        has_more=False,
        data=[
            EmailLog(
                id="1234",
                subject="Invoice #1234",
                from_="John Doe <john.doe@example.com>",
                to="Jane Doe <jane.doe@example.com>",
                html_body="<html><body><p>Hi Jane,</p><p>Please find attached the invoice for your recent purchase.</p><p>Thanks,</p><p>John</p></body></html>",
                text_body="Hi Jane,\n\nPlease find attached the invoice for your recent purchase.\n\nThanks,\nJohn",
                created_at=datetime.datetime.fromisoformat(
                    "2021-01-01 00:00:00+00:00",
                ),
            )
        ],
    )
    """

    count: int = pydantic_v1.Field()
    """
    Total number of logs for the given filters. This value is not limited by the limit parameter. It is provided so that you can determine how many pages of results are available.
    """

    has_more: bool = pydantic_v1.Field(alias="hasMore")
    """
    True if there are more logs available for the given filters.
    """

    data: typing.List[EmailLog]

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
