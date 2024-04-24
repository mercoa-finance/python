# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import pydantic_v1
from ...payment_method_types.types.payment_method_type import PaymentMethodType


class MetadataShowConditions(pydantic_v1.BaseModel):
    has_options: typing.Optional[bool] = pydantic_v1.Field(alias="hasOptions", default=None)
    """
    Show this field only if the entity has values set for the metadata key.
    """

    has_document: typing.Optional[bool] = pydantic_v1.Field(alias="hasDocument", default=None)
    """
    Show this field only if a document has been attached.
    """

    has_no_line_items: typing.Optional[bool] = pydantic_v1.Field(alias="hasNoLineItems", default=None)
    """
    Show this field only if the invoice has no line items. Useful for showing a field that applies to the entire invoice but overridden by line items if present.
    """

    payment_source_types: typing.Optional[typing.List[PaymentMethodType]] = pydantic_v1.Field(
        alias="paymentSourceTypes", default=None
    )
    """
    Show this field only if the payment source type is in this list.
    """

    payment_source_custom_schema_ids: typing.Optional[typing.List[str]] = pydantic_v1.Field(
        alias="paymentSourceCustomSchemaIds", default=None
    )
    """
    Show this field only if the payment source schema ID is in this list of payment source schema IDs. This is only applicable if paymentSourceTypes contains CUSTOM.
    """

    payment_destination_types: typing.Optional[typing.List[PaymentMethodType]] = pydantic_v1.Field(
        alias="paymentDestinationTypes", default=None
    )
    """
    Show this field only if the payment destination type is in this list.
    """

    payment_destination_custom_schema_ids: typing.Optional[typing.List[str]] = pydantic_v1.Field(
        alias="paymentDestinationCustomSchemaIds", default=None
    )
    """
    Show this field only if the payment destination schema ID is in this list of payment destination schema IDs. This is only applicable if paymentDestinationTypes contains CUSTOM.
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