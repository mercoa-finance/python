# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class BankAccountCheckOptions(pydantic.BaseModel):
    enabled: typing.Optional[bool] = pydantic.Field(
        default=None, description="If true, will allow the user to print checks from this bank account"
    )
    initial_check_number: typing.Optional[int] = pydantic.Field(
        alias="initialCheckNumber",
        default=None,
        description="If provided, will start the check number sequence at the provided number. If not provided, will start at 5000.",
    )
    routing_number_override: typing.Optional[str] = pydantic.Field(
        alias="routingNumberOverride",
        default=None,
        description="If provided, will print a check with the provided routing number instead of the one from the bank account",
    )
    account_number_override: typing.Optional[str] = pydantic.Field(
        alias="accountNumberOverride",
        default=None,
        description="If provided, will print a check with the provided account number instead of the one from the bank account",
    )
    signatory_name: str = pydantic.Field(
        alias="signatoryName", description="Name of the person who's signature will be printed on the check."
    )
    signature_image: typing.Optional[str] = pydantic.Field(
        alias="signatureImage",
        default=None,
        description="Base64 encoded image of the signature. If not provided, will use the signatoryName to generate a signature. Mercoa will automatically grayscale, resize, and convert the image to a PNG the image to fit on the check.",
    )
    use_signature_image: typing.Optional[bool] = pydantic.Field(
        alias="useSignatureImage",
        default=None,
        description="If true, will print checks with the provided signatureImage. If false, will print checks with a generated signature from the signatoryName. If this parameter is not set the default behavior is to use the signatureImage if provided.",
    )

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
        json_encoders = {dt.datetime: serialize_datetime}
