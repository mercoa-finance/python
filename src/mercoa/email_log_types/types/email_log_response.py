# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import pydantic
import typing_extensions
from ...core.serialization import FieldMetadata
import typing
from .email_log import EmailLog
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class EmailLogResponse(UniversalBaseModel):
    """
    Examples
    --------
    import datetime

    from mercoa.email_log_types import EmailLog, EmailLogResponse

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

    count: int = pydantic.Field()
    """
    Total number of logs for the given filters. This value is not limited by the limit parameter. It is provided so that you can determine how many pages of results are available.
    """

    has_more: typing_extensions.Annotated[bool, FieldMetadata(alias="hasMore")] = pydantic.Field()
    """
    True if there are more logs available for the given filters.
    """

    data: typing.List[EmailLog]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
