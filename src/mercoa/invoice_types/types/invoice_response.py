# This file was auto-generated by Fern from our API Definition.

from .invoice_response_base import InvoiceResponseBase
from .invoice_id import InvoiceId
import typing
import datetime as dt
import pydantic
from .invoice_failure_type import InvoiceFailureType
from ...transaction.types.transaction_response_without_invoices import TransactionResponseWithoutInvoices
from ...vendor_credit_types.types.vendor_credit_id import VendorCreditId
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class InvoiceResponse(InvoiceResponseBase):
    """
    Examples
    --------
    import datetime

    from mercoa.commons import Address, PhoneNumber
    from mercoa.entity_types import (
        ApprovalPolicyResponse,
        BusinessProfileResponse,
        CounterpartyCustomizationAccount,
        CounterpartyResponse,
        Ein,
        EntityUserResponse,
        IdentifierList_RolesList,
        ProfileResponse,
        Rule_Approver,
        TaxId,
        Trigger_Amount,
    )
    from mercoa.invoice_types import (
        ApprovalSlot,
        AssociatedApprovalAction,
        CommentResponse,
        InvoiceLineItemResponse,
        InvoiceResponse,
        PaymentDestinationOptions_Check,
    )
    from mercoa.payment_method_types import (
        PaymentMethodResponse_BankAccount,
        PaymentMethodResponse_Check,
    )

    InvoiceResponse(
        id="in_26e7b5d3-a739-4b23-9ad9-6aaa085f47a9",
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
        payer=CounterpartyResponse(
            id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
            foreign_id="MY-DB-ID-12345",
            name="Acme Inc.",
            email="customer@acme.com",
            accepted_tos=True,
            status="verified",
            is_customer=True,
            is_payor=True,
            is_payee=False,
            is_network_payor=False,
            is_network_payee=False,
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
                    tax_id=TaxId(
                        ein=Ein(
                            number="12-3456789",
                        ),
                    ),
                    owners_provided=True,
                ),
            ),
            accounts=[
                CounterpartyCustomizationAccount(
                    account_id="85866843",
                    postal_code="94105",
                    name_on_account="John Doe",
                )
            ],
            payment_methods=[
                PaymentMethodResponse_BankAccount(
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
                    metadata={},
                    frozen=False,
                    created_at=datetime.datetime.fromisoformat(
                        "2021-01-01 00:00:00+00:00",
                    ),
                    updated_at=datetime.datetime.fromisoformat(
                        "2021-01-01 00:00:00+00:00",
                    ),
                )
            ],
            counterparty_type=["ENTITY"],
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
            metadata={},
            frozen=False,
            created_at=datetime.datetime.fromisoformat(
                "2021-01-01 00:00:00+00:00",
            ),
            updated_at=datetime.datetime.fromisoformat(
                "2021-01-01 00:00:00+00:00",
            ),
        ),
        payment_source_id="pm_4794d597-70dc-4fec-b6ec-c5988e759769",
        vendor_id="ent_21661ac1-a2a8-4465-a6c0-64474ba8181d",
        vendor=CounterpartyResponse(
            id="ent_21661ac1-a2a8-4465-a6c0-64474ba8181d",
            foreign_id="MY-DB-ID-90909",
            name="Big Box Store",
            email="vendor@bigboxstore.com",
            accepted_tos=False,
            status="unverified",
            is_customer=False,
            is_payor=False,
            is_payee=True,
            is_network_payor=False,
            is_network_payee=False,
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
            payment_methods=[
                PaymentMethodResponse_BankAccount(
                    id="pm_7610541f-4619-4033-8620-cfccfb811293",
                    account_name="Vendor Checking Account",
                    bank_name="Chase",
                    routing_number="66554433",
                    account_number="55934059697648",
                    account_type="CHECKING",
                    status="NEW",
                    is_default_source=True,
                    is_default_destination=True,
                    supported_currencies=["USD"],
                    metadata={},
                    frozen=False,
                    created_at=datetime.datetime.fromisoformat(
                        "2021-01-01 00:00:00+00:00",
                    ),
                    updated_at=datetime.datetime.fromisoformat(
                        "2021-01-01 00:00:00+00:00",
                    ),
                )
            ],
            counterparty_type=["ENTITY"],
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
            metadata={},
            frozen=False,
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
                text="This is an approval comment",
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
                quantity=1.0,
                unit_price=100.0,
                category="EXPENSE",
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
                trigger=[
                    Trigger_Amount(
                        amount=100.0,
                        currency="USD",
                    )
                ],
                rule=Rule_Approver(
                    num_approvers=2,
                    identifier_list=IdentifierList_RolesList(
                        value=["Admin", "Controller"]
                    ),
                ),
                upstream_policy_id="root",
                updated_at=datetime.datetime.fromisoformat(
                    "2024-01-02 00:00:00+00:00",
                ),
                created_at=datetime.datetime.fromisoformat(
                    "2024-01-01 00:00:00+00:00",
                ),
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
    processed_at: typing.Optional[dt.datetime] = pydantic.Field(alias="processedAt", default=None)
    """
    Date when the invoice payment was processed.
    """

    settlement_date: typing.Optional[dt.datetime] = pydantic.Field(alias="settlementDate", default=None)
    """
    Date of funds settlement.
    """

    foreign_id: typing.Optional[str] = pydantic.Field(alias="foreignId", default=None)
    """
    The ID used to identify this invoice in your system. This ID must be unique within each creatorEntity in your system, e.g. two invoices with the same creatorEntity may not have the same foreign ID.
    """

    failure_type: typing.Optional[InvoiceFailureType] = pydantic.Field(alias="failureType", default=None)
    """
    If the invoice failed to be paid, this field will be populated with the type of failure.
    """

    transactions: typing.Optional[typing.List[TransactionResponseWithoutInvoices]] = pydantic.Field(default=None)
    """
    Transactions associated with this invoice.
    """

    vendor_credit_ids: typing.Optional[typing.List[VendorCreditId]] = pydantic.Field(
        alias="vendorCreditIds", default=None
    )
    """
    The IDs of the vendor credits that are currently applied to this invoice.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
