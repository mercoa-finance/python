# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .currency_code import CurrencyCode
from .custom_payment_method_schema_field import CustomPaymentMethodSchemaField


class CustomPaymentMethodSchemaRequest(pydantic_v1.BaseModel):
    """
    Examples
    --------
    from mercoa import (
        CustomPaymentMethodSchemaField,
        CustomPaymentMethodSchemaRequest,
    )

    CustomPaymentMethodSchemaRequest(
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
        estimated_processing_time=0,
    )
    """

    name: str
    is_source: bool = pydantic_v1.Field(alias="isSource")
    """
    This payment method can be used as a payment source for an invoice
    """

    is_destination: bool = pydantic_v1.Field(alias="isDestination")
    """
    This payment method can be used as a payment destination for an invoice
    """

    estimated_processing_time: typing.Optional[int] = pydantic_v1.Field(alias="estimatedProcessingTime", default=None)
    """
    Estimated time in days for this payment method to process a payments. Set as 0 for same-day payment methods, -1 for unknown processing time.
    """

    supported_currencies: typing.Optional[typing.List[CurrencyCode]] = pydantic_v1.Field(
        alias="supportedCurrencies", default=None
    )
    """
    List of currencies that this payment method supports. If not provided, the payment method will support only USD.
    """

    fields: typing.List[CustomPaymentMethodSchemaField]

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
