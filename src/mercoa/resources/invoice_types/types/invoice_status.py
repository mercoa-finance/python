# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class InvoiceStatus(str, enum.Enum):
    DRAFT = "DRAFT"
    NEW = "NEW"
    APPROVED = "APPROVED"
    SCHEDULED = "SCHEDULED"
    PENDING = "PENDING"
    PAID = "PAID"
    ARCHIVED = "ARCHIVED"
    REFUSED = "REFUSED"
    CANCELED = "CANCELED"

    def visit(
        self,
        draft: typing.Callable[[], T_Result],
        new: typing.Callable[[], T_Result],
        approved: typing.Callable[[], T_Result],
        scheduled: typing.Callable[[], T_Result],
        pending: typing.Callable[[], T_Result],
        paid: typing.Callable[[], T_Result],
        archived: typing.Callable[[], T_Result],
        refused: typing.Callable[[], T_Result],
        canceled: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is InvoiceStatus.DRAFT:
            return draft()
        if self is InvoiceStatus.NEW:
            return new()
        if self is InvoiceStatus.APPROVED:
            return approved()
        if self is InvoiceStatus.SCHEDULED:
            return scheduled()
        if self is InvoiceStatus.PENDING:
            return pending()
        if self is InvoiceStatus.PAID:
            return paid()
        if self is InvoiceStatus.ARCHIVED:
            return archived()
        if self is InvoiceStatus.REFUSED:
            return refused()
        if self is InvoiceStatus.CANCELED:
            return canceled()