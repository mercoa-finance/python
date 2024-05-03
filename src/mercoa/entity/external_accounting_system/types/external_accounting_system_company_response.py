# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

from ....core.pydantic_utilities import pydantic_v1


class ExternalAccountingSystemCompanyResponse_Codat(pydantic_v1.BaseModel):
    type: typing.Literal["codat"] = "codat"
    company_id: str = pydantic_v1.Field(alias="companyId")

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


ExternalAccountingSystemCompanyResponse = typing.Union[ExternalAccountingSystemCompanyResponse_Codat]
