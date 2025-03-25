# This file was auto-generated by Fern from our API Definition.

import typing
from ...core.client_wrapper import SyncClientWrapper
from ...invoice_types.types.invoice_id import InvoiceId
from ...invoice_types.types.invoice_line_item_id import InvoiceLineItemId
from ...invoice_types.types.invoice_line_item_individual_update_request import (
    InvoiceLineItemIndividualUpdateRequest,
)
from ...core.request_options import RequestOptions
from ...invoice_types.types.invoice_response import InvoiceResponse
from ...core.jsonable_encoder import jsonable_encoder
from ...core.serialization import convert_and_respect_annotation_metadata
from json.decoder import JSONDecodeError
from ...core.api_error import ApiError
from ...core.pydantic_utilities import parse_obj_as
from ...commons.errors.bad_request import BadRequest
from ...commons.errors.unauthorized import Unauthorized
from ...commons.errors.forbidden import Forbidden
from ...commons.errors.not_found import NotFound
from ...commons.errors.conflict import Conflict
from ...commons.errors.internal_server_error import InternalServerError
from ...commons.errors.unimplemented import Unimplemented
from ...core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class LineItemClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def update(
        self,
        invoice_id: InvoiceId,
        line_item_id: InvoiceLineItemId,
        *,
        request: InvoiceLineItemIndividualUpdateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InvoiceResponse:
        """
        Update invoice line item

        Parameters
        ----------
        invoice_id : InvoiceId
            Invoice ID

        line_item_id : InvoiceLineItemId
            Invoice Line Item ID

        request : InvoiceLineItemIndividualUpdateRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InvoiceResponse

        Examples
        --------
        import datetime

        from mercoa import Mercoa
        from mercoa.invoice_types import InvoiceLineItemIndividualUpdateRequest

        client = Mercoa(
            token="YOUR_TOKEN",
        )
        client.invoice.line_item.update(
            invoice_id="in_d8f68285-1c6d-4d5a-a9e3-252c3180fac4",
            line_item_id="inli_8aa84cb8-2ae7-4579-8fa3-87586e7c14a7",
            request=InvoiceLineItemIndividualUpdateRequest(
                name="Product A",
                description="Product A",
                service_start_date=datetime.datetime.fromisoformat(
                    "2021-01-01 00:00:00+00:00",
                ),
                service_end_date=datetime.datetime.fromisoformat(
                    "2021-01-31 00:00:00+00:00",
                ),
                metadata={"key1": "value1", "key2": "value2"},
                gl_account_id="600394",
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"invoice/{jsonable_encoder(invoice_id)}/line-item/{jsonable_encoder(line_item_id)}",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request,
                annotation=InvoiceLineItemIndividualUpdateRequest,
                direction="write",
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return typing.cast(
                InvoiceResponse,
                parse_obj_as(
                    type_=InvoiceResponse,  # type: ignore
                    object_=_response_json,
                ),
            )
        if "errorName" in _response_json:
            if _response_json["errorName"] == "BadRequest":
                raise BadRequest(
                    typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,  # type: ignore
                            object_=_response_json["content"],
                        ),
                    )
                )
            if _response_json["errorName"] == "Unauthorized":
                raise Unauthorized(
                    typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,  # type: ignore
                            object_=_response_json["content"],
                        ),
                    )
                )
            if _response_json["errorName"] == "Forbidden":
                raise Forbidden(
                    typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,  # type: ignore
                            object_=_response_json["content"],
                        ),
                    )
                )
            if _response_json["errorName"] == "NotFound":
                raise NotFound(
                    typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,  # type: ignore
                            object_=_response_json["content"],
                        ),
                    )
                )
            if _response_json["errorName"] == "Conflict":
                raise Conflict(
                    typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,  # type: ignore
                            object_=_response_json["content"],
                        ),
                    )
                )
            if _response_json["errorName"] == "InternalServerError":
                raise InternalServerError(
                    typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,  # type: ignore
                            object_=_response_json["content"],
                        ),
                    )
                )
            if _response_json["errorName"] == "Unimplemented":
                raise Unimplemented(
                    typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,  # type: ignore
                            object_=_response_json["content"],
                        ),
                    )
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncLineItemClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def update(
        self,
        invoice_id: InvoiceId,
        line_item_id: InvoiceLineItemId,
        *,
        request: InvoiceLineItemIndividualUpdateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InvoiceResponse:
        """
        Update invoice line item

        Parameters
        ----------
        invoice_id : InvoiceId
            Invoice ID

        line_item_id : InvoiceLineItemId
            Invoice Line Item ID

        request : InvoiceLineItemIndividualUpdateRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InvoiceResponse

        Examples
        --------
        import asyncio
        import datetime

        from mercoa import AsyncMercoa
        from mercoa.invoice_types import InvoiceLineItemIndividualUpdateRequest

        client = AsyncMercoa(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.invoice.line_item.update(
                invoice_id="in_d8f68285-1c6d-4d5a-a9e3-252c3180fac4",
                line_item_id="inli_8aa84cb8-2ae7-4579-8fa3-87586e7c14a7",
                request=InvoiceLineItemIndividualUpdateRequest(
                    name="Product A",
                    description="Product A",
                    service_start_date=datetime.datetime.fromisoformat(
                        "2021-01-01 00:00:00+00:00",
                    ),
                    service_end_date=datetime.datetime.fromisoformat(
                        "2021-01-31 00:00:00+00:00",
                    ),
                    metadata={"key1": "value1", "key2": "value2"},
                    gl_account_id="600394",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"invoice/{jsonable_encoder(invoice_id)}/line-item/{jsonable_encoder(line_item_id)}",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request,
                annotation=InvoiceLineItemIndividualUpdateRequest,
                direction="write",
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return typing.cast(
                InvoiceResponse,
                parse_obj_as(
                    type_=InvoiceResponse,  # type: ignore
                    object_=_response_json,
                ),
            )
        if "errorName" in _response_json:
            if _response_json["errorName"] == "BadRequest":
                raise BadRequest(
                    typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,  # type: ignore
                            object_=_response_json["content"],
                        ),
                    )
                )
            if _response_json["errorName"] == "Unauthorized":
                raise Unauthorized(
                    typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,  # type: ignore
                            object_=_response_json["content"],
                        ),
                    )
                )
            if _response_json["errorName"] == "Forbidden":
                raise Forbidden(
                    typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,  # type: ignore
                            object_=_response_json["content"],
                        ),
                    )
                )
            if _response_json["errorName"] == "NotFound":
                raise NotFound(
                    typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,  # type: ignore
                            object_=_response_json["content"],
                        ),
                    )
                )
            if _response_json["errorName"] == "Conflict":
                raise Conflict(
                    typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,  # type: ignore
                            object_=_response_json["content"],
                        ),
                    )
                )
            if _response_json["errorName"] == "InternalServerError":
                raise InternalServerError(
                    typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,  # type: ignore
                            object_=_response_json["content"],
                        ),
                    )
                )
            if _response_json["errorName"] == "Unimplemented":
                raise Unimplemented(
                    typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,  # type: ignore
                            object_=_response_json["content"],
                        ),
                    )
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)
