# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class CustomPaymentMethodSchemaFieldType(str, enum.Enum):
    TEXT = "text"
    NUMBER = "number"
    SELECT = "select"
    DATE = "date"
    PHONE = "phone"
    EMAIL = "email"
    URL = "url"
    ADDRESS = "address"

    def visit(
        self,
        text: typing.Callable[[], T_Result],
        number: typing.Callable[[], T_Result],
        select: typing.Callable[[], T_Result],
        date: typing.Callable[[], T_Result],
        phone: typing.Callable[[], T_Result],
        email: typing.Callable[[], T_Result],
        url: typing.Callable[[], T_Result],
        address: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CustomPaymentMethodSchemaFieldType.TEXT:
            return text()
        if self is CustomPaymentMethodSchemaFieldType.NUMBER:
            return number()
        if self is CustomPaymentMethodSchemaFieldType.SELECT:
            return select()
        if self is CustomPaymentMethodSchemaFieldType.DATE:
            return date()
        if self is CustomPaymentMethodSchemaFieldType.PHONE:
            return phone()
        if self is CustomPaymentMethodSchemaFieldType.EMAIL:
            return email()
        if self is CustomPaymentMethodSchemaFieldType.URL:
            return url()
        if self is CustomPaymentMethodSchemaFieldType.ADDRESS:
            return address()
