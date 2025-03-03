# This file was auto-generated by Fern from our API Definition.

from ....core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ....core.serialization import FieldMetadata
import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2


class CodatCompanyCreationRequest(UniversalBaseModel):
    company_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="companyId")] = pydantic.Field(
        default=None
    )
    """
    If the company already exists in Codat, provide the company ID to link the company to the entity. If the company does not exist, leave this field blank and Codat will create a new company.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
