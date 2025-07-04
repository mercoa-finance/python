# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
from .approval_request_with_id import ApprovalRequestWithId
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class BulkInvoiceApprovalRequest(UniversalBaseModel):
    """
    Examples
    --------
    from mercoa.invoice_types import (
        ApprovalRequestWithId,
        BulkInvoiceApprovalRequest,
    )

    BulkInvoiceApprovalRequest(
        invoices=[
            ApprovalRequestWithId(
                invoice_id="in_26e7b5d3-a739-4b23-9ad9-6aaa085f47a9",
                text="This is a reason for my action",
                user_id="user_e24fc81c-c5ee-47e8-af42-4fe29d895506",
            )
        ],
    )
    """

    invoices: typing.List[ApprovalRequestWithId]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
