# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
from .payment_rail_response import PaymentRailResponse
import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class PaymentMethodsResponse(UniversalBaseModel):
    payer_payments: typing.List[PaymentRailResponse] = pydantic.Field(alias="payerPayments")
    """
    List of payment methods that can be used to pay invoices.
    """

    backup_disbursements: typing.List[PaymentRailResponse] = pydantic.Field(alias="backupDisbursements")
    """
    List of payment methods that can be created by a payor to send disbursements.
    """

    vendor_disbursements: typing.List[PaymentRailResponse] = pydantic.Field(alias="vendorDisbursements")
    """
    List of payment methods that can be created by a payee to receive disbursements.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
