# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing_extensions
from ...core.serialization import FieldMetadata
import typing
from .entity_group_response import EntityGroupResponse
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class EntityGroupFindResponse(UniversalBaseModel):
    """
    Examples
    --------
    import datetime

    from mercoa.commons import Address, PhoneNumber
    from mercoa.entity_group_types import (
        EntityGroupFindResponse,
        EntityGroupResponse,
    )
    from mercoa.entity_types import (
        BusinessProfileResponse,
        Ein,
        EntityResponse,
        ProfileResponse,
        TaxId,
    )

    EntityGroupFindResponse(
        count=3,
        has_more=False,
        data=[
            EntityGroupResponse(
                id="entg_a3582b70-fd04-4888-9185-a640ae9048be",
                foreign_id="your-group-id",
                name="AcmeConglomerate",
                email_to_name="acmegroup",
                metadata={"key1": "value1"},
                entities=[
                    EntityResponse(
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
                    EntityResponse(
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
                    ),
                ],
            )
        ],
    )
    """

    count: int
    has_more: typing_extensions.Annotated[bool, FieldMetadata(alias="hasMore")]
    data: typing.List[EntityGroupResponse]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
