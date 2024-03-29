# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

from .codat_company_response import CodatCompanyResponse


class ExternalAccountingSystemCompanyResponse_Codat(CodatCompanyResponse):
    type: typing.Literal["codat"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


ExternalAccountingSystemCompanyResponse = typing.Union[ExternalAccountingSystemCompanyResponse_Codat]
