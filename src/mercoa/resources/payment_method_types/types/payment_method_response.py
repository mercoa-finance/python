# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

from .bank_account_response import BankAccountResponse
from .card_response import CardResponse
from .check_response import CheckResponse
from .custom_payment_method_response import CustomPaymentMethodResponse
from .payment_method_base_response import PaymentMethodBaseResponse


class PaymentMethodResponse_BankAccount(BankAccountResponse):
    type: typing.Literal["bankAccount"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class PaymentMethodResponse_Card(CardResponse):
    type: typing.Literal["card"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class PaymentMethodResponse_Check(CheckResponse):
    type: typing.Literal["check"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class PaymentMethodResponse_Custom(CustomPaymentMethodResponse):
    type: typing.Literal["custom"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class PaymentMethodResponse_OffPlatform(PaymentMethodBaseResponse):
    type: typing.Literal["offPlatform"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


PaymentMethodResponse = typing.Union[
    PaymentMethodResponse_BankAccount,
    PaymentMethodResponse_Card,
    PaymentMethodResponse_Check,
    PaymentMethodResponse_Custom,
    PaymentMethodResponse_OffPlatform,
]
