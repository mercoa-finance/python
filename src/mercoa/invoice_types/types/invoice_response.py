# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import pydantic_v1
from ...entity_types.types.approval_policy_response import ApprovalPolicyResponse
from ...entity_types.types.entity_id import EntityId
from ...entity_types.types.entity_response import EntityResponse
from ...entity_types.types.entity_user_response import EntityUserResponse
from ...payment_method_types.types.currency_code import CurrencyCode
from ...payment_method_types.types.payment_method_id import PaymentMethodId
from ...payment_method_types.types.payment_method_response import PaymentMethodResponse
from .approval_slot import ApprovalSlot
from .comment_response import CommentResponse
from .invoice_failure_type import InvoiceFailureType
from .invoice_fees_response import InvoiceFeesResponse
from .invoice_id import InvoiceId
from .invoice_line_item_response import InvoiceLineItemResponse
from .invoice_status import InvoiceStatus
from .payment_destination_options import PaymentDestinationOptions


class InvoiceResponse(pydantic_v1.BaseModel):
    """
    Examples
    --------
    import datetime

    from mercoa import (
        Address,
        ApprovalPolicyResponse,
        ApprovalSlot,
        AssociatedApprovalAction,
        BusinessProfileResponse,
        CommentResponse,
        EntityResponse,
        EntityUserResponse,
        IdentifierList_RolesList,
        InvoiceLineItemResponse,
        InvoiceResponse,
        PaymentDestinationOptions_Check,
        PaymentMethodResponse_BankAccount,
        PaymentMethodResponse_Check,
        PhoneNumber,
        ProfileResponse,
        Rule_Approver,
    )

    InvoiceResponse(
        id="inv_26e7b5d3-a739-4b23-9ad9-6aaa085f47a9",
        status="PAID",
        amount=100.0,
        currency="USD",
        invoice_date=datetime.datetime.fromisoformat(
            "2021-01-01 00:00:00+00:00",
        ),
        deduction_date=datetime.datetime.fromisoformat(
            "2021-01-01 00:00:00+00:00",
        ),
        settlement_date=datetime.datetime.fromisoformat(
            "2021-01-03 00:00:00+00:00",
        ),
        due_date=datetime.datetime.fromisoformat(
            "2021-01-31 00:00:00+00:00",
        ),
        invoice_number="INV-123",
        note_to_self="For the month of January",
        service_start_date=datetime.datetime.fromisoformat(
            "2021-01-01 00:00:00+00:00",
        ),
        service_end_date=datetime.datetime.fromisoformat(
            "2021-01-31 00:00:00+00:00",
        ),
        payer_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
        payer=EntityResponse(
            id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
            foreign_id="MY-DB-ID-12345",
            name="Acme Inc.",
            email="customer@acme.com",
            accepted_tos=True,
            status="verified",
            is_customer=True,
            is_payor=True,
            is_payee=False,
            account_type="business",
            updated_at=datetime.datetime.fromisoformat(
                "2024-01-02 00:00:00+00:00",
            ),
            created_at=datetime.datetime.fromisoformat(
                "2024-01-01 00:00:00+00:00",
            ),
            profile=ProfileResponse(
                business=BusinessProfileResponse(
                    email="customer@acme.com",
                    legal_business_name="Acme Inc.",
                    business_type="llc",
                    phone=PhoneNumber(
                        country_code="1",
                        number="4155551234",
                    ),
                    address=Address(
                        address_line_1="123 Main St",
                        address_line_2="Unit 1",
                        city="San Francisco",
                        state_or_province="CA",
                        postal_code="94105",
                        country="US",
                    ),
                    tax_id_provided=True,
                    owners_provided=True,
                ),
            ),
        ),
        payment_source=PaymentMethodResponse_BankAccount(
            id="pm_4794d597-70dc-4fec-b6ec-c5988e759769",
            account_name="My Checking Account",
            bank_name="Chase",
            routing_number="12345678",
            account_number="99988767623",
            account_type="CHECKING",
            status="VERIFIED",
            is_default_source=True,
            is_default_destination=True,
            supported_currencies=["USD"],
            created_at=datetime.datetime.fromisoformat(
                "2021-01-01 00:00:00+00:00",
            ),
            updated_at=datetime.datetime.fromisoformat(
                "2021-01-01 00:00:00+00:00",
            ),
        ),
        payment_source_id="pm_4794d597-70dc-4fec-b6ec-c5988e759769",
        vendor_id="ent_21661ac1-a2a8-4465-a6c0-64474ba8181d",
        vendor=EntityResponse(
            id="ent_21661ac1-a2a8-4465-a6c0-64474ba8181d",
            foreign_id="MY-DB-ID-90909",
            name="Big Box Store",
            email="vendor@bigboxstore.com",
            accepted_tos=False,
            status="unverified",
            is_customer=False,
            is_payor=False,
            is_payee=True,
            account_type="business",
            updated_at=datetime.datetime.fromisoformat(
                "2024-01-02 00:00:00+00:00",
            ),
            created_at=datetime.datetime.fromisoformat(
                "2024-01-01 00:00:00+00:00",
            ),
            profile=ProfileResponse(
                business=BusinessProfileResponse(
                    email="vendor@bigboxstore.com",
                    legal_business_name="Big Box Store",
                    business_type="publicCorporation",
                    tax_id_provided=False,
                    owners_provided=False,
                ),
            ),
        ),
        payment_destination=PaymentMethodResponse_Check(
            id="pm_5fde2f4a-facc-48ef-8f0d-6b7d087c7b18",
            pay_to_the_order_of="John Doe",
            address_line_1="123 Main St",
            address_line_2="Apt 1",
            city="New York",
            state_or_province="NY",
            postal_code="10001",
            country="US",
            is_default_source=False,
            is_default_destination=True,
            supported_currencies=["USD"],
            created_at=datetime.datetime.fromisoformat(
                "2021-01-01 00:00:00+00:00",
            ),
            updated_at=datetime.datetime.fromisoformat(
                "2021-01-01 00:00:00+00:00",
            ),
        ),
        payment_destination_id="pm_5fde2f4a-facc-48ef-8f0d-6b7d087c7b18",
        payment_destination_options=PaymentDestinationOptions_Check(
            delivery="MAIL",
        ),
        payment_destination_confirmed=True,
        has_documents=True,
        has_source_email=True,
        comments=[
            CommentResponse(
                id="ic_b3525b66-da94-4525-9f31-426bcf657128",
                text="This is a comment",
                user=EntityUserResponse(
                    id="user_ec3aafc8-ea86-408a-a6c1-545497badbbb",
                    foreign_id="MY-DB-ID-12345",
                    email="john.doe@acme.com",
                    name="John Doe",
                    roles=["admin", "approver"],
                    created_at=datetime.datetime.fromisoformat(
                        "2024-01-01 00:00:00+00:00",
                    ),
                    updated_at=datetime.datetime.fromisoformat(
                        "2024-01-01 00:00:00+00:00",
                    ),
                ),
                associated_approval_action=AssociatedApprovalAction(
                    user_id="user_e24fc81c-c5ee-47e8-af42-4fe29d895506",
                    action="APPROVE",
                ),
                created_at=datetime.datetime.fromisoformat(
                    "2021-01-01 00:00:00+00:00",
                ),
                updated_at=datetime.datetime.fromisoformat(
                    "2021-01-01 00:00:00+00:00",
                ),
            )
        ],
        line_items=[
            InvoiceLineItemResponse(
                id="inli_26672f38-eb9a-48f1-a7a0-f1b855e38cd7",
                amount=100.0,
                currency="USD",
                description="Product A",
                name="Product A",
                quantity=1,
                unit_price=100.0,
                service_start_date=datetime.datetime.fromisoformat(
                    "2021-01-01 00:00:00+00:00",
                ),
                service_end_date=datetime.datetime.fromisoformat(
                    "2021-01-31 00:00:00+00:00",
                ),
                metadata={"key1": "value1", "key2": "value2"},
                gl_account_id="600394",
                created_at=datetime.datetime.fromisoformat(
                    "2021-01-01 00:00:00+00:00",
                ),
                updated_at=datetime.datetime.fromisoformat(
                    "2021-01-01 00:00:00+00:00",
                ),
            )
        ],
        approvers=[
            ApprovalSlot(
                approval_policy_id="apvl_5ce50275-1789-42ea-bc60-bb7e6d03635c",
                approval_slot_id="inap_9bb311c9-7c15-4c9e-8148-63814e0abec6",
                assigned_user_id="user_e24fc81c-c5ee-47e8-af42-4fe29d895506",
                action="APPROVE",
                eligible_user_ids=["user_e24fc81c-c5ee-47e8-af42-4fe29d895506"],
                eligible_roles=["admin"],
                date=datetime.datetime.fromisoformat(
                    "2021-01-01 00:00:00+00:00",
                ),
            )
        ],
        approval_policy=[
            ApprovalPolicyResponse(
                id="apvl_8545a84e-a45f-41bf-bdf1-33b42a55812c",
                trigger=[],
                rule=Rule_Approver(
                    num_approvers=1,
                    identifier_list=IdentifierList_RolesList(value=["admin"]),
                ),
                upstream_policy_id="root",
            )
        ],
        metadata={"key1": "value1", "key2": "value2"},
        foreign_id="YOUR-DATABASE-ID",
        creator_user=EntityUserResponse(
            id="user_ec3aafc8-ea86-408a-a6c1-545497badbbb",
            foreign_id="MY-DB-ID-12345",
            email="john.doe@acme.com",
            name="John Doe",
            roles=["admin", "approver"],
            created_at=datetime.datetime.fromisoformat(
                "2024-01-01 00:00:00+00:00",
            ),
            updated_at=datetime.datetime.fromisoformat(
                "2024-01-01 00:00:00+00:00",
            ),
        ),
        processed_at=datetime.datetime.fromisoformat(
            "2021-01-01 00:00:00+00:00",
        ),
        created_at=datetime.datetime.fromisoformat(
            "2021-01-01 00:00:00+00:00",
        ),
        updated_at=datetime.datetime.fromisoformat(
            "2021-01-01 00:00:00+00:00",
        ),
    )
    """

    id: InvoiceId
    status: InvoiceStatus
    amount: typing.Optional[float] = pydantic_v1.Field(default=None)
    """
    Total amount of invoice in major units
    """

    currency: typing.Optional[CurrencyCode] = pydantic_v1.Field(default=None)
    """
    Currency code for the amount. Defaults to USD.
    """

    invoice_date: typing.Optional[dt.datetime] = pydantic_v1.Field(alias="invoiceDate", default=None)
    """
    Date the invoice was issued.
    """

    deduction_date: typing.Optional[dt.datetime] = pydantic_v1.Field(alias="deductionDate", default=None)
    """
    Date when funds will be deducted from payer's account.
    """

    settlement_date: typing.Optional[dt.datetime] = pydantic_v1.Field(alias="settlementDate", default=None)
    """
    Date of funds settlement.
    """

    due_date: typing.Optional[dt.datetime] = pydantic_v1.Field(alias="dueDate", default=None)
    """
    Due date of invoice.
    """

    invoice_number: typing.Optional[str] = pydantic_v1.Field(alias="invoiceNumber", default=None)
    note_to_self: typing.Optional[str] = pydantic_v1.Field(alias="noteToSelf", default=None)
    service_start_date: typing.Optional[dt.datetime] = pydantic_v1.Field(alias="serviceStartDate", default=None)
    service_end_date: typing.Optional[dt.datetime] = pydantic_v1.Field(alias="serviceEndDate", default=None)
    payer_id: typing.Optional[EntityId] = pydantic_v1.Field(alias="payerId", default=None)
    payer: typing.Optional[EntityResponse] = None
    payment_source: typing.Optional[PaymentMethodResponse] = pydantic_v1.Field(alias="paymentSource", default=None)
    payment_source_id: typing.Optional[PaymentMethodId] = pydantic_v1.Field(alias="paymentSourceId", default=None)
    vendor_id: typing.Optional[EntityId] = pydantic_v1.Field(alias="vendorId", default=None)
    vendor: typing.Optional[EntityResponse] = None
    payment_destination: typing.Optional[PaymentMethodResponse] = pydantic_v1.Field(
        alias="paymentDestination", default=None
    )
    payment_destination_id: typing.Optional[PaymentMethodId] = pydantic_v1.Field(
        alias="paymentDestinationId", default=None
    )
    payment_destination_options: typing.Optional[PaymentDestinationOptions] = pydantic_v1.Field(
        alias="paymentDestinationOptions", default=None
    )
    payment_destination_confirmed: bool = pydantic_v1.Field(alias="paymentDestinationConfirmed")
    """
    True if the payment destination has been confirmed by the vendor. False if the payment destination has been set (for example, a check to an address) but has not been confirmed by the vendor.
    """

    has_documents: bool = pydantic_v1.Field(alias="hasDocuments")
    """
    True if the invoice has documents attached.
    """

    has_source_email: bool = pydantic_v1.Field(alias="hasSourceEmail")
    """
    True if the invoice was created by an incoming email.
    """

    comments: typing.Optional[typing.List[CommentResponse]] = None
    line_items: typing.Optional[typing.List[InvoiceLineItemResponse]] = pydantic_v1.Field(
        alias="lineItems", default=None
    )
    approvers: typing.List[ApprovalSlot]
    approval_policy: typing.List[ApprovalPolicyResponse] = pydantic_v1.Field(alias="approvalPolicy")
    metadata: typing.Dict[str, str] = pydantic_v1.Field()
    """
    Metadata associated with this invoice.
    """

    foreign_id: typing.Optional[str] = pydantic_v1.Field(alias="foreignId", default=None)
    """
    The ID used to identify this invoice in your system. This ID must be unique within each creatorEntity in your system, e.g. two invoices with the same creatorEntity may not have the same foreign ID.
    """

    creator_user: typing.Optional[EntityUserResponse] = pydantic_v1.Field(alias="creatorUser", default=None)
    """
    Entity user who created this invoice.
    """

    failure_type: typing.Optional[InvoiceFailureType] = pydantic_v1.Field(alias="failureType", default=None)
    """
    If the invoice failed to be paid, this field will be populated with the type of failure.
    """

    processed_at: typing.Optional[dt.datetime] = pydantic_v1.Field(alias="processedAt", default=None)
    created_at: dt.datetime = pydantic_v1.Field(alias="createdAt")
    updated_at: dt.datetime = pydantic_v1.Field(alias="updatedAt")
    fees: typing.Optional[InvoiceFeesResponse] = pydantic_v1.Field(default=None)
    """
    Fees associated with this invoice.
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
