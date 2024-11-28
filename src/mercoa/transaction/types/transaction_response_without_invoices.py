# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ...core.pydantic_utilities import UniversalBaseModel
import typing
from .transaction_failure_reason import TransactionFailureReason
import pydantic
from .transaction_id import TransactionId
from .transaction_status import TransactionStatus
import datetime as dt
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class TransactionResponseWithoutInvoices_BankAccountToBankAccount(UniversalBaseModel):
    type: typing.Literal["bankAccountToBankAccount"] = "bankAccountToBankAccount"
    failure_reason: typing.Optional[TransactionFailureReason] = pydantic.Field(alias="failureReason", default=None)
    id: TransactionId
    status: TransactionStatus
    created_at: dt.datetime = pydantic.Field(alias="createdAt")
    updated_at: dt.datetime = pydantic.Field(alias="updatedAt")

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TransactionResponseWithoutInvoices_BankAccountToMailedCheck(UniversalBaseModel):
    type: typing.Literal["bankAccountToMailedCheck"] = "bankAccountToMailedCheck"
    check_number: int = pydantic.Field(alias="checkNumber")
    id: TransactionId
    status: TransactionStatus
    created_at: dt.datetime = pydantic.Field(alias="createdAt")
    updated_at: dt.datetime = pydantic.Field(alias="updatedAt")

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TransactionResponseWithoutInvoices_Custom(UniversalBaseModel):
    type: typing.Literal["custom"] = "custom"
    id: TransactionId
    status: TransactionStatus
    created_at: dt.datetime = pydantic.Field(alias="createdAt")
    updated_at: dt.datetime = pydantic.Field(alias="updatedAt")

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TransactionResponseWithoutInvoices_OffPlatform(UniversalBaseModel):
    type: typing.Literal["offPlatform"] = "offPlatform"
    id: TransactionId
    status: TransactionStatus
    created_at: dt.datetime = pydantic.Field(alias="createdAt")
    updated_at: dt.datetime = pydantic.Field(alias="updatedAt")

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


TransactionResponseWithoutInvoices = typing.Union[
    TransactionResponseWithoutInvoices_BankAccountToBankAccount,
    TransactionResponseWithoutInvoices_BankAccountToMailedCheck,
    TransactionResponseWithoutInvoices_Custom,
    TransactionResponseWithoutInvoices_OffPlatform,
]
