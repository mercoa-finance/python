# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing_extensions
from .ocr_job_id import OcrJobId
from ...core.serialization import FieldMetadata
from ...invoice_types.types.invoice_response import InvoiceResponse
from ...entity_types.types.counterparty_response import CounterpartyResponse
import typing
from ...payment_method_types.types.check_response import CheckResponse
from ...payment_method_types.types.bank_account_response import BankAccountResponse
from ...entity_types.types.entity_response import EntityResponse
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class OcrResponse(UniversalBaseModel):
    """
    Examples
    --------
    import datetime

    from mercoa.commons import Address, PhoneNumber
    from mercoa.entity_types import (
        BusinessProfileResponse,
        CounterpartyCustomizationAccount,
        CounterpartyResponse,
        Ein,
        EntityResponse,
        ProfileResponse,
        TaxId,
    )
    from mercoa.invoice_types import InvoiceLineItemResponse, InvoiceResponse
    from mercoa.ocr import OcrResponse
    from mercoa.payment_method_types import (
        BankAccountResponse,
        CheckResponse,
        PaymentMethodResponse_BankAccount,
    )

    OcrResponse(
        job_id="ocr_8f86116b-3b4d-4ded-99ef-3bc929d8c33c",
        invoice=InvoiceResponse(
            id="in_26e7b5d3-a739-4b23-9ad9-6aaa085f47a9",
            status="DRAFT",
            amount=100.0,
            currency="USD",
            invoice_date=datetime.datetime.fromisoformat(
                "2021-01-01 00:00:00+00:00",
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
                        confirmed_by_entity=True,
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
                        confirmed_by_entity=False,
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
            payment_destination_confirmed=False,
            has_documents=True,
            has_source_email=True,
            comments=[],
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
            approvers=[],
            approval_policy=[],
            metadata={},
            created_at=datetime.datetime.fromisoformat(
                "2021-01-01 00:00:00+00:00",
            ),
            updated_at=datetime.datetime.fromisoformat(
                "2021-01-01 00:00:00+00:00",
            ),
        ),
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
                    confirmed_by_entity=False,
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
        check=CheckResponse(
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
            confirmed_by_entity=True,
            created_at=datetime.datetime.fromisoformat(
                "2021-01-01 00:00:00+00:00",
            ),
            updated_at=datetime.datetime.fromisoformat(
                "2021-01-01 00:00:00+00:00",
            ),
        ),
        bank_account=BankAccountResponse(
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
            confirmed_by_entity=False,
            created_at=datetime.datetime.fromisoformat(
                "2021-01-01 00:00:00+00:00",
            ),
            updated_at=datetime.datetime.fromisoformat(
                "2021-01-01 00:00:00+00:00",
            ),
        ),
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
        ),
    )
    """

    job_id: typing_extensions.Annotated[OcrJobId, FieldMetadata(alias="jobId")]
    invoice: InvoiceResponse
    vendor: CounterpartyResponse
    check: typing.Optional[CheckResponse] = None
    bank_account: typing_extensions.Annotated[
        typing.Optional[BankAccountResponse], FieldMetadata(alias="bankAccount")
    ] = None
    payer: typing.Optional[EntityResponse] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
