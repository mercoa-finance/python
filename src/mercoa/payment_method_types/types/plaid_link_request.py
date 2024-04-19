# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import pydantic_v1


class PlaidLinkRequest(pydantic_v1.BaseModel):
    account_id: str = pydantic_v1.Field(alias="accountId")
    """
    Plaid account ID
    """

    public_token: typing.Optional[str] = pydantic_v1.Field(alias="publicToken", default=None)
    """
    Public token received from Plaid Link. Use this if linking the account using the Plaid Link frontend component.
    """

    access_token: typing.Optional[str] = pydantic_v1.Field(alias="accessToken", default=None)
    """
    Plaid access token for the account. If you already have an access token for the account (for example, you have linked the account to your app already), use this instead of publicToken.
    """

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
