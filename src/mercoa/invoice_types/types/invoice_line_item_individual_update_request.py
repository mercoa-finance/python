# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1


class InvoiceLineItemIndividualUpdateRequest(pydantic_v1.BaseModel):
    """
    Examples
    --------
    import datetime

    from mercoa import InvoiceLineItemIndividualUpdateRequest

    InvoiceLineItemIndividualUpdateRequest(
        name="Product A",
        description="Product A",
        service_start_date=datetime.datetime.fromisoformat(
            "2021-01-01 00:00:00+00:00",
        ),
        service_end_date=datetime.datetime.fromisoformat(
            "2021-01-31 00:00:00+00:00",
        ),
        metadata={"key1": "value1", "key2": "value2"},
        gl_account_id="600394",
    )
    """

    name: typing.Optional[str] = None
    description: typing.Optional[str] = None
    service_start_date: typing.Optional[dt.datetime] = pydantic_v1.Field(alias="serviceStartDate", default=None)
    service_end_date: typing.Optional[dt.datetime] = pydantic_v1.Field(alias="serviceEndDate", default=None)
    metadata: typing.Optional[typing.Dict[str, str]] = None
    gl_account_id: typing.Optional[str] = pydantic_v1.Field(alias="glAccountId", default=None)
    """
    ID of general ledger account associated with this line item.
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
