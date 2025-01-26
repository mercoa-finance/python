# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
from .metadata_customization_request import MetadataCustomizationRequest
from .payment_method_customization_request import PaymentMethodCustomizationRequest
import pydantic
from .ocr_customization_request import OcrCustomizationRequest
from .notification_customization_request import NotificationCustomizationRequest
from .workflow_customization_request import WorkflowCustomizationRequest
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class EntityCustomizationRequest(UniversalBaseModel):
    """
    Examples
    --------
    from mercoa.entity_types import (
        EntityCustomizationRequest,
        MetadataCustomizationRequest,
        NotificationCustomizationRequest,
        OcrCustomizationRequest,
        PaymentMethodCustomizationRequest_BankAccount,
        PaymentMethodCustomizationRequest_Check,
        PaymentMethodCustomizationRequest_Custom,
        WorkflowCustomizationRequest,
    )

    EntityCustomizationRequest(
        metadata=[
            MetadataCustomizationRequest(
                key="my_custom_field",
                disabled=True,
            ),
            MetadataCustomizationRequest(
                key="my_other_field",
                disabled=False,
            ),
        ],
        payment_source=[
            PaymentMethodCustomizationRequest_BankAccount(
                disabled=True,
            ),
            PaymentMethodCustomizationRequest_Custom(
                schema_id="cpms_7df2974a-4069-454c-912f-7e58ebe030fb",
                disabled=True,
            ),
        ],
        backup_disbursement=[
            PaymentMethodCustomizationRequest_Check(
                disabled=True,
            )
        ],
        payment_destination=[
            PaymentMethodCustomizationRequest_BankAccount(
                disabled=True,
            ),
            PaymentMethodCustomizationRequest_Check(
                disabled=True,
            ),
        ],
        ocr=OcrCustomizationRequest(
            line_items=True,
            collapse_line_items=True,
            invoice_metadata=True,
            line_item_metadata=True,
            line_item_gl_account_id=True,
            predict_metadata=True,
            tax_and_shipping_as_line_items=True,
        ),
        notifications=NotificationCustomizationRequest(
            assume_role="admin",
        ),
        workflow=WorkflowCustomizationRequest(
            auto_advance_invoice_status=True,
        ),
    )
    """

    metadata: typing.Optional[typing.List[MetadataCustomizationRequest]] = None
    payment_source: typing.Optional[typing.List[PaymentMethodCustomizationRequest]] = pydantic.Field(
        alias="paymentSource", default=None
    )
    backup_disbursement: typing.Optional[typing.List[PaymentMethodCustomizationRequest]] = pydantic.Field(
        alias="backupDisbursement", default=None
    )
    payment_destination: typing.Optional[typing.List[PaymentMethodCustomizationRequest]] = pydantic.Field(
        alias="paymentDestination", default=None
    )
    ocr: typing.Optional[OcrCustomizationRequest] = None
    notifications: typing.Optional[NotificationCustomizationRequest] = None
    workflow: typing.Optional[WorkflowCustomizationRequest] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
