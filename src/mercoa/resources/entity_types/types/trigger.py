# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

from .amount_trigger import AmountTrigger
from .metadata_trigger import MetadataTrigger
from .vendor_trigger import VendorTrigger


class Trigger_Amount(AmountTrigger):
    type: typing.Literal["amount"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Trigger_Vendor(VendorTrigger):
    type: typing.Literal["vendor"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Trigger_Metadata(MetadataTrigger):
    type: typing.Literal["metadata"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


Trigger = typing.Union[Trigger_Amount, Trigger_Vendor, Trigger_Metadata]
