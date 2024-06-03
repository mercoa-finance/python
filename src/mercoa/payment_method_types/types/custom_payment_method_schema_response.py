# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .currency_code import CurrencyCode
from .custom_payment_method_schema_field import CustomPaymentMethodSchemaField
from .custom_payment_method_schema_id import CustomPaymentMethodSchemaId


class CustomPaymentMethodSchemaResponse(pydantic_v1.BaseModel):
    """
    Examples
    --------
    import datetime

    from mercoa import (
        CustomPaymentMethodSchemaField,
        CustomPaymentMethodSchemaResponse,
    )

    CustomPaymentMethodSchemaResponse(
        id="cpms_4794d597-70dc-4fec-b6ec-c5988e759769",
        name="Wire",
        is_source=False,
        is_destination=True,
        supported_currencies=["USD", "EUR"],
        fields=[
            CustomPaymentMethodSchemaField(
                name="bankName",
                display_name="Bank Name",
                type="text",
                optional=False,
            ),
            CustomPaymentMethodSchemaField(
                name="recipientName",
                display_name="Recipient Name",
                type="text",
                optional=False,
            ),
            CustomPaymentMethodSchemaField(
                name="accountNumber",
                display_name="Account Number",
                type="number",
                optional=False,
                use_as_account_number=True,
            ),
            CustomPaymentMethodSchemaField(
                name="routingNumber",
                display_name="Routing Number",
                type="number",
                optional=False,
            ),
        ],
        created_at=datetime.datetime.fromisoformat(
            "2021-01-01 00:00:00+00:00",
        ),
        updated_at=datetime.datetime.fromisoformat(
            "2021-01-01 00:00:00+00:00",
        ),
    )
    """

    id: CustomPaymentMethodSchemaId
    name: str
    is_source: bool = pydantic_v1.Field(alias="isSource")
    """
    This payment method can be used as a payment source for an invoice
    """

    is_destination: bool = pydantic_v1.Field(alias="isDestination")
    """
    This payment method can be used as a payment destination for an invoice
    """

    supported_currencies: typing.List[CurrencyCode] = pydantic_v1.Field(alias="supportedCurrencies")
    """
    List of currencies that this payment method supports.
    """

    fields: typing.List[CustomPaymentMethodSchemaField]
    created_at: dt.datetime = pydantic_v1.Field(alias="createdAt")
    updated_at: dt.datetime = pydantic_v1.Field(alias="updatedAt")

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
