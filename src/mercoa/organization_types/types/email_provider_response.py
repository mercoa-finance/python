# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
from .email_sender_response import EmailSenderResponse
import pydantic
import typing
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class EmailProviderResponse(UniversalBaseModel):
    sender: EmailSenderResponse
    inbox_domain: str = pydantic.Field(alias="inboxDomain")
    alternative_inbox_domains: typing.List[str] = pydantic.Field(alias="alternativeInboxDomains")

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
