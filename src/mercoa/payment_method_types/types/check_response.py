# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import pydantic_v1
from .payment_method_base_response import PaymentMethodBaseResponse


class CheckResponse(PaymentMethodBaseResponse):
    """
    Examples
    --------
    import datetime

    from mercoa import CheckResponse

    CheckResponse(
        id="pm_5fde2f4a-facc-48ef-8f0d-6b7d087c7b18",
        pay_to_the_order_of="John Doe",
        address_line_1="123 Main St",
        address_line_2="Apt 1",
        city="New York",
        state_or_province="NY",
        postal_code="10001",
        country="US",
        is_default_source=False,
        is_default_destination=True,
        supported_currencies=["USD"],
        created_at=datetime.datetime.fromisoformat(
            "2021-01-01 00:00:00+00:00",
        ),
        updated_at=datetime.datetime.fromisoformat(
            "2021-01-01 00:00:00+00:00",
        ),
    )
    """

    pay_to_the_order_of: str = pydantic_v1.Field(alias="payToTheOrderOf")
    address_line_1: str = pydantic_v1.Field(alias="addressLine1")
    address_line_2: typing.Optional[str] = pydantic_v1.Field(alias="addressLine2", default=None)
    city: str
    state_or_province: str = pydantic_v1.Field(alias="stateOrProvince")
    postal_code: str = pydantic_v1.Field(alias="postalCode")
    country: str

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
