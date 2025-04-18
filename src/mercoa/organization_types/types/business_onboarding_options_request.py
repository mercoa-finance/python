# This file was auto-generated by Fern from our API Definition.

from .common_onboarding_options_request import CommonOnboardingOptionsRequest
import typing
from .onboarding_option_request import OnboardingOptionRequest
import typing_extensions
from ...core.serialization import FieldMetadata
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class BusinessOnboardingOptionsRequest(CommonOnboardingOptionsRequest):
    type: typing.Optional[OnboardingOptionRequest] = None
    doing_business_as: typing_extensions.Annotated[
        typing.Optional[OnboardingOptionRequest], FieldMetadata(alias="doingBusinessAs")
    ] = None
    ein: typing.Optional[OnboardingOptionRequest] = None
    mcc: typing.Optional[OnboardingOptionRequest] = None
    formation_date: typing_extensions.Annotated[
        typing.Optional[OnboardingOptionRequest], FieldMetadata(alias="formationDate")
    ] = None
    website: typing.Optional[OnboardingOptionRequest] = None
    description: typing.Optional[OnboardingOptionRequest] = None
    representatives: typing.Optional[OnboardingOptionRequest] = None
    logo: typing.Optional[OnboardingOptionRequest] = None
    average_transaction_size: typing_extensions.Annotated[
        typing.Optional[OnboardingOptionRequest],
        FieldMetadata(alias="averageTransactionSize"),
    ] = None
    average_monthly_transaction_volume: typing_extensions.Annotated[
        typing.Optional[OnboardingOptionRequest],
        FieldMetadata(alias="averageMonthlyTransactionVolume"),
    ] = None
    max_transaction_size: typing_extensions.Annotated[
        typing.Optional[OnboardingOptionRequest],
        FieldMetadata(alias="maxTransactionSize"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
