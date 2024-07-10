# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from ...invoice_types.types.payment_destination_options import PaymentDestinationOptions
from ...payment_method_types.types.payment_method_id import PaymentMethodId


class CalculatePaymentTimingRequest(pydantic_v1.BaseModel):
    """
    Examples
    --------
    import datetime

    from mercoa import CalculatePaymentTimingRequest

    CalculatePaymentTimingRequest(
        estimated_deduction_date=datetime.datetime.fromisoformat(
            "2024-01-02 00:00:00+00:00",
        ),
        payment_source_id="pm_4794d597-70dc-4fec-b6ec-c5988e759769",
        payment_destination_id="pm_4794d597-70dc-4fec-b6ec-c5988e759769",
    )
    """

    estimated_deduction_date: typing.Optional[dt.datetime] = pydantic_v1.Field(
        alias="estimatedDeductionDate", default=None
    )
    """
    Date the payment is scheduled to be deducted from the payer's account. Use this field if the payment has not yet been deducted.
    """

    processed_at: typing.Optional[dt.datetime] = pydantic_v1.Field(alias="processedAt", default=None)
    """
    Date the payment was processed. Use this field if the payment has already been deducted.
    """

    payment_source_id: PaymentMethodId = pydantic_v1.Field(alias="paymentSourceId")
    """
    ID of payment source.
    """

    payment_destination_id: PaymentMethodId = pydantic_v1.Field(alias="paymentDestinationId")
    """
    ID of payment destination.
    """

    payment_destination_options: typing.Optional[PaymentDestinationOptions] = pydantic_v1.Field(
        alias="paymentDestinationOptions", default=None
    )
    """
    Options for the payment destination. Depending on the payment destination, this may include things such as check delivery method.
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
