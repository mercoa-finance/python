# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class EmailMessageResponse(UniversalBaseModel):
    """
    Examples
    --------
    from mercoa.collection_types import EmailMessageResponse

    EmailMessageResponse(
        subject="Invoice Past Due - Please Review",
        body="Your invoice is now 3 days overdue. Please arrange payment as soon as possible to avoid further follow-ups.",
    )
    """

    subject: str = pydantic.Field()
    """
    The subject of the email
    """

    body: str = pydantic.Field()
    """
    The body of the email in plaintext
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
