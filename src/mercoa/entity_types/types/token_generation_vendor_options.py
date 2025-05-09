# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ...core.serialization import FieldMetadata
import pydantic
from .vendor_network import VendorNetwork
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class TokenGenerationVendorOptions(UniversalBaseModel):
    disable_creation: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="disableCreation")] = (
        pydantic.Field(default=None)
    )
    """
    If true, the user will not be able to create new vendors.
    """

    network: VendorNetwork

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
