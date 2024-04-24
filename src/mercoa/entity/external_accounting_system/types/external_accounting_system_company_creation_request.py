# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

from .codat_company_creation_request import CodatCompanyCreationRequest


class ExternalAccountingSystemCompanyCreationRequest_Codat(CodatCompanyCreationRequest):
    type: typing.Literal["codat"] = "codat"

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


ExternalAccountingSystemCompanyCreationRequest = typing.Union[ExternalAccountingSystemCompanyCreationRequest_Codat]