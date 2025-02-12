# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from ...payment_method_types.types.payment_method_type import PaymentMethodType
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class MetadataShowConditions(UniversalBaseModel):
    always_hide: typing.Optional[bool] = pydantic.Field(alias="alwaysHide", default=None)
    """
    Always hide this field. Useful for getting data from OCR and AI predictions that you don't want to show in the UI.
    """

    has_options: typing.Optional[bool] = pydantic.Field(alias="hasOptions", default=None)
    """
    Show this field only if the entity has values set for the metadata key.
    """

    has_document: typing.Optional[bool] = pydantic.Field(alias="hasDocument", default=None)
    """
    Show this field only if a document has been attached.
    """

    has_no_line_items: typing.Optional[bool] = pydantic.Field(alias="hasNoLineItems", default=None)
    """
    Show this field only if the invoice has no line items. Useful for showing a field that applies to the entire invoice but overridden by line items if present.
    """

    payment_source_types: typing.Optional[typing.List[PaymentMethodType]] = pydantic.Field(
        alias="paymentSourceTypes", default=None
    )
    """
    Show this field only if the payment source type is in this list.
    """

    payment_source_custom_schema_ids: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="paymentSourceCustomSchemaIds", default=None
    )
    """
    Show this field only if the payment source schema ID is in this list of payment source schema IDs. This is only applicable if paymentSourceTypes contains CUSTOM.
    """

    payment_destination_types: typing.Optional[typing.List[PaymentMethodType]] = pydantic.Field(
        alias="paymentDestinationTypes", default=None
    )
    """
    Show this field only if the payment destination type is in this list.
    """

    payment_destination_custom_schema_ids: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="paymentDestinationCustomSchemaIds", default=None
    )
    """
    Show this field only if the payment destination schema ID is in this list of payment destination schema IDs. This is only applicable if paymentDestinationTypes contains CUSTOM.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
