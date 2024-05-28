# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import pydantic_v1
from .bank_account_check_options import BankAccountCheckOptions
from .bank_status import BankStatus
from .bank_type import BankType
from .payment_method_base_response import PaymentMethodBaseResponse


class BankAccountResponse(PaymentMethodBaseResponse):
    """
    Examples
    --------
    import datetime

    from mercoa import BankAccountResponse

    BankAccountResponse(
        id="pm_4794d597-70dc-4fec-b6ec-c5988e759769",
        account_name="My Checking Account",
        bank_name="Chase",
        routing_number="12345678",
        account_number="99988767623",
        account_type="CHECKING",
        status="VERIFIED",
        is_default_source=True,
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

    account_name: str = pydantic_v1.Field(alias="accountName")
    bank_name: str = pydantic_v1.Field(alias="bankName")
    routing_number: str = pydantic_v1.Field(alias="routingNumber")
    account_number: str = pydantic_v1.Field(alias="accountNumber")
    account_type: BankType = pydantic_v1.Field(alias="accountType")
    status: BankStatus
    check_options: typing.Optional[BankAccountCheckOptions] = pydantic_v1.Field(alias="checkOptions", default=None)
    """
    If check printing is enabled for the account, will return the check options for this bank account
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
