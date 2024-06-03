# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .bank_address import BankAddress


class BankLookupResponse(pydantic_v1.BaseModel):
    """
    Examples
    --------
    from mercoa import BankAddress, BankLookupResponse

    BankLookupResponse(
        bank_name="Bank of America",
        bank_address=BankAddress(
            address="123 Main St",
            city="Anytown",
            state="CA",
            postal_code="12345",
            postal_code_extension="6789",
        ),
    )
    """

    bank_name: str = pydantic_v1.Field(alias="bankName")
    bank_address: BankAddress = pydantic_v1.Field(alias="bankAddress")

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
