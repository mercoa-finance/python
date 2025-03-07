# This file was auto-generated by Fern from our API Definition.

from .payment_method_base_request import PaymentMethodBaseRequest
import typing_extensions
import typing
from ...core.serialization import FieldMetadata
import pydantic
from .custom_payment_method_schema_id import CustomPaymentMethodSchemaId
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class CustomPaymentMethodRequest(PaymentMethodBaseRequest):
    """
    Examples
    --------
    from mercoa.payment_method_types import CustomPaymentMethodRequest

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

    foreign_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="foreignId")] = pydantic.Field(
        default=None
    )
    """
    ID for this payment method in your system
    """

    account_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="accountName")] = None
    account_number: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="accountNumber")] = None
    available_balance: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="availableBalance")] = (
        pydantic.Field(default=None)
    )
    """
    The available balance for this payment method.
    """

    schema_id: typing_extensions.Annotated[CustomPaymentMethodSchemaId, FieldMetadata(alias="schemaId")] = (
        pydantic.Field()
    )
    """
    Payment method schema used for this payment method. Defines the fields that this payment method contains.
    """

    data: typing.Dict[str, str] = pydantic.Field()
    """
    Object of key/value pairs that matches the keys in the linked payment method schema.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
