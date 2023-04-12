# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class EntityStatus(str, enum.Enum):
    UNVERIFIED = "unverified"
    PENDING = "pending"
    RESUBMIT = "resubmit"
    REVIEW = "review"
    VERIFIED = "verified"
    FAILED = "failed"

    def visit(
        self,
        unverified: typing.Callable[[], T_Result],
        pending: typing.Callable[[], T_Result],
        resubmit: typing.Callable[[], T_Result],
        review: typing.Callable[[], T_Result],
        verified: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EntityStatus.UNVERIFIED:
            return unverified()
        if self is EntityStatus.PENDING:
            return pending()
        if self is EntityStatus.RESUBMIT:
            return resubmit()
        if self is EntityStatus.REVIEW:
            return review()
        if self is EntityStatus.VERIFIED:
            return verified()
        if self is EntityStatus.FAILED:
            return failed()