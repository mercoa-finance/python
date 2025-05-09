# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
from ...commons.types.full_name import FullName
from ...commons.types.phone_number import PhoneNumber
from ...commons.types.address import Address
import typing_extensions
from ...commons.types.birth_date import BirthDate
from ...core.serialization import FieldMetadata
from ...commons.types.individual_government_id import IndividualGovernmentId
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class IndividualProfileRequest(UniversalBaseModel):
    email: typing.Optional[str] = None
    name: FullName
    phone: typing.Optional[PhoneNumber] = None
    address: typing.Optional[Address] = None
    birth_date: typing_extensions.Annotated[typing.Optional[BirthDate], FieldMetadata(alias="birthDate")] = None
    government_id: typing_extensions.Annotated[
        typing.Optional[IndividualGovernmentId], FieldMetadata(alias="governmentID")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
