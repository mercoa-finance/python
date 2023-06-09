# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class OrderDirection(str, enum.Enum):
    ASC = "ASC"
    DESC = "DESC"

    def visit(self, asc: typing.Callable[[], T_Result], desc: typing.Callable[[], T_Result]) -> T_Result:
        if self is OrderDirection.ASC:
            return asc()
        if self is OrderDirection.DESC:
            return desc()
