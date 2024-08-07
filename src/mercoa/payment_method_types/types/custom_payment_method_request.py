# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .custom_payment_method_schema_id import CustomPaymentMethodSchemaId
from .payment_method_base_request import PaymentMethodBaseRequest


class CustomPaymentMethodRequest(PaymentMethodBaseRequest):
    """
    Examples
    --------
    from mercoa import CustomPaymentMethodRequest

    CustomPaymentMethodRequest(
        foreign_id="DB_FOREIGN_ID",
        account_name="Vendor Wire Account",
        account_number="123456789",
        schema_id="cpms_4794d597-70dc-4fec-b6ec-c5988e759769",
        data={
            "bankName": "Chase",
            "recipientName": "John Doe",
            "routingNumber": "123456789",
            "accountNumber": "99988767623",
        },
    )
    """

    foreign_id: typing.Optional[str] = pydantic_v1.Field(alias="foreignId", default=None)
    """
    ID for this payment method in your system
    """

    account_name: typing.Optional[str] = pydantic_v1.Field(alias="accountName", default=None)
    account_number: typing.Optional[str] = pydantic_v1.Field(alias="accountNumber", default=None)
    available_balance: typing.Optional[float] = pydantic_v1.Field(alias="availableBalance", default=None)
    """
    The available balance for this payment method.
    """

    schema_id: CustomPaymentMethodSchemaId = pydantic_v1.Field(alias="schemaId")
    """
    Payment method schema used for this payment method. Defines the fields that this payment method contains.
    """

    data: typing.Dict[str, str] = pydantic_v1.Field()
    """
    Object of key/value pairs that matches the keys in the linked payment method schema.
    """

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
