# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing
import urllib.parse
from json.decoder import JSONDecodeError

import pydantic

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.datetime_utils import serialize_datetime
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_dict import remove_none_from_dict
from ..commons.errors.auth_header_malformed_error import AuthHeaderMalformedError
from ..commons.errors.auth_header_missing_error import AuthHeaderMissingError
from ..commons.errors.forbidden import Forbidden
from ..commons.errors.not_found import NotFound
from ..commons.errors.unauthorized import Unauthorized
from ..commons.errors.unimplemented import Unimplemented
from ..commons.types.order_direction import OrderDirection
from ..entity_types.types.entity_id import EntityId
from ..entity_types.types.entity_user_id import EntityUserId
from ..invoice_types.errors.duplicate_invoice_number import DuplicateInvoiceNumber
from ..invoice_types.errors.invoice_error import InvoiceError
from ..invoice_types.errors.invoice_status_error import InvoiceStatusError
from ..invoice_types.errors.vendor_not_found import VendorNotFound
from ..invoice_types.types.find_invoice_response import FindInvoiceResponse
from ..invoice_types.types.invoice_id import InvoiceId
from ..invoice_types.types.invoice_order_by_field import InvoiceOrderByField
from ..invoice_types.types.invoice_request import InvoiceRequest
from ..invoice_types.types.invoice_response import InvoiceResponse
from ..invoice_types.types.invoice_status import InvoiceStatus
from .resources.approval.client import ApprovalClient, AsyncApprovalClient
from .resources.comment.client import AsyncCommentClient, CommentClient
from .resources.document.client import AsyncDocumentClient, DocumentClient

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class InvoiceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper
        self.approval = ApprovalClient(client_wrapper=self._client_wrapper)
        self.comment = CommentClient(client_wrapper=self._client_wrapper)
        self.document = DocumentClient(client_wrapper=self._client_wrapper)

    def find(
        self,
        *,
        entity_id: typing.Union[typing.Optional[EntityId], typing.List[EntityId]],
        start_date: typing.Optional[dt.datetime] = None,
        end_date: typing.Optional[dt.datetime] = None,
        order_by: typing.Optional[InvoiceOrderByField] = None,
        order_direction: typing.Optional[OrderDirection] = None,
        limit: typing.Optional[int] = None,
        starting_after: typing.Optional[InvoiceId] = None,
        search: typing.Optional[str] = None,
        vendor_id: typing.Union[typing.Optional[EntityId], typing.List[EntityId]],
        approver_id: typing.Union[typing.Optional[EntityUserId], typing.List[EntityUserId]],
        invoice_id: typing.Union[typing.Optional[InvoiceId], typing.List[InvoiceId]],
        status: typing.Union[typing.Optional[InvoiceStatus], typing.List[InvoiceStatus]],
    ) -> FindInvoiceResponse:
        """
        Search invoices for all entities in the organization

        Parameters:
            - entity_id: typing.Union[typing.Optional[EntityId], typing.List[EntityId]]. Filter invoices by entity ID.

            - start_date: typing.Optional[dt.datetime]. Start date for invoice created on date filter.

            - end_date: typing.Optional[dt.datetime]. End date for invoice created date filter.

            - order_by: typing.Optional[InvoiceOrderByField]. Field to order invoices by. Defaults to CREATED_AT.

            - order_direction: typing.Optional[OrderDirection]. Direction to order invoices by. Defaults to asc.

            - limit: typing.Optional[int]. Number of invoices to return. Limit can range between 1 and 100, and the default is 10.

            - starting_after: typing.Optional[InvoiceId]. The ID of the invoice to start after. If not provided, the first page of invoices will be returned.

            - search: typing.Optional[str]. Filter vendors by name. Partial matches are supported.

            - vendor_id: typing.Union[typing.Optional[EntityId], typing.List[EntityId]]. Filter invoices by vendor ID.

            - approver_id: typing.Union[typing.Optional[EntityUserId], typing.List[EntityUserId]]. Filter invoices by assigned approver user ID.

            - invoice_id: typing.Union[typing.Optional[InvoiceId], typing.List[InvoiceId]]. Filter invoices by invoice ID.

            - status: typing.Union[typing.Optional[InvoiceStatus], typing.List[InvoiceStatus]]. Invoice status to filter on
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "invoices"),
            params=remove_none_from_dict(
                {
                    "entityId": entity_id,
                    "startDate": serialize_datetime(start_date) if start_date is not None else None,
                    "endDate": serialize_datetime(end_date) if end_date is not None else None,
                    "orderBy": order_by,
                    "orderDirection": order_direction,
                    "limit": limit,
                    "startingAfter": starting_after,
                    "search": search,
                    "vendorId": vendor_id,
                    "approverId": approver_id,
                    "invoiceId": invoice_id,
                    "status": status,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(FindInvoiceResponse, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "AuthHeaderMissingError":
                raise AuthHeaderMissingError()
            if _response_json["errorName"] == "AuthHeaderMalformedError":
                raise AuthHeaderMalformedError(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unauthorized":
                raise Unauthorized(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Forbidden":
                raise Forbidden(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "NotFound":
                raise NotFound(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unimplemented":
                raise Unimplemented(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(self, *, request: InvoiceRequest) -> InvoiceResponse:
        """
        Create invoice

        Parameters:
            - request: InvoiceRequest.
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "invoice"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(InvoiceResponse, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "DuplicateInvoiceNumber":
                raise DuplicateInvoiceNumber(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "InvoiceError":
                raise InvoiceError(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "AuthHeaderMissingError":
                raise AuthHeaderMissingError()
            if _response_json["errorName"] == "AuthHeaderMalformedError":
                raise AuthHeaderMalformedError(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unauthorized":
                raise Unauthorized(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Forbidden":
                raise Forbidden(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "NotFound":
                raise NotFound(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unimplemented":
                raise Unimplemented(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, invoice_id: InvoiceId) -> InvoiceResponse:
        """
        Get invoice

        Parameters:
            - invoice_id: InvoiceId.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"invoice/{invoice_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(InvoiceResponse, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "AuthHeaderMissingError":
                raise AuthHeaderMissingError()
            if _response_json["errorName"] == "AuthHeaderMalformedError":
                raise AuthHeaderMalformedError(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unauthorized":
                raise Unauthorized(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Forbidden":
                raise Forbidden(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "NotFound":
                raise NotFound(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unimplemented":
                raise Unimplemented(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update(self, invoice_id: InvoiceId, *, request: InvoiceRequest) -> InvoiceResponse:
        """
        Update invoice

        Parameters:
            - invoice_id: InvoiceId.

            - request: InvoiceRequest.
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"invoice/{invoice_id}"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(InvoiceResponse, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "DuplicateInvoiceNumber":
                raise DuplicateInvoiceNumber(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "InvoiceError":
                raise InvoiceError(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "AuthHeaderMissingError":
                raise AuthHeaderMissingError()
            if _response_json["errorName"] == "AuthHeaderMalformedError":
                raise AuthHeaderMalformedError(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unauthorized":
                raise Unauthorized(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Forbidden":
                raise Forbidden(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "NotFound":
                raise NotFound(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unimplemented":
                raise Unimplemented(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(self, invoice_id: InvoiceId) -> None:
        """
        Delete invoice. Only invoices in the DRAFT and NEW status can be deleted.

        Parameters:
            - invoice_id: InvoiceId.
        """
        _response = self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"invoice/{invoice_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if "errorName" in _response_json:
            if _response_json["errorName"] == "InvoiceStatusError":
                raise InvoiceStatusError(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "AuthHeaderMissingError":
                raise AuthHeaderMissingError()
            if _response_json["errorName"] == "AuthHeaderMalformedError":
                raise AuthHeaderMalformedError(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unauthorized":
                raise Unauthorized(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Forbidden":
                raise Forbidden(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "NotFound":
                raise NotFound(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unimplemented":
                raise Unimplemented(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_vendor_link(self, invoice_id: InvoiceId) -> str:
        """
        Get temporary link for vendor to accept payment

        Parameters:
            - invoice_id: InvoiceId.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"invoice/{invoice_id}/vendorlink"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(str, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "VendorNotFound":
                raise VendorNotFound(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "AuthHeaderMissingError":
                raise AuthHeaderMissingError()
            if _response_json["errorName"] == "AuthHeaderMalformedError":
                raise AuthHeaderMalformedError(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unauthorized":
                raise Unauthorized(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Forbidden":
                raise Forbidden(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "NotFound":
                raise NotFound(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unimplemented":
                raise Unimplemented(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncInvoiceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper
        self.approval = AsyncApprovalClient(client_wrapper=self._client_wrapper)
        self.comment = AsyncCommentClient(client_wrapper=self._client_wrapper)
        self.document = AsyncDocumentClient(client_wrapper=self._client_wrapper)

    async def find(
        self,
        *,
        entity_id: typing.Union[typing.Optional[EntityId], typing.List[EntityId]],
        start_date: typing.Optional[dt.datetime] = None,
        end_date: typing.Optional[dt.datetime] = None,
        order_by: typing.Optional[InvoiceOrderByField] = None,
        order_direction: typing.Optional[OrderDirection] = None,
        limit: typing.Optional[int] = None,
        starting_after: typing.Optional[InvoiceId] = None,
        search: typing.Optional[str] = None,
        vendor_id: typing.Union[typing.Optional[EntityId], typing.List[EntityId]],
        approver_id: typing.Union[typing.Optional[EntityUserId], typing.List[EntityUserId]],
        invoice_id: typing.Union[typing.Optional[InvoiceId], typing.List[InvoiceId]],
        status: typing.Union[typing.Optional[InvoiceStatus], typing.List[InvoiceStatus]],
    ) -> FindInvoiceResponse:
        """
        Search invoices for all entities in the organization

        Parameters:
            - entity_id: typing.Union[typing.Optional[EntityId], typing.List[EntityId]]. Filter invoices by entity ID.

            - start_date: typing.Optional[dt.datetime]. Start date for invoice created on date filter.

            - end_date: typing.Optional[dt.datetime]. End date for invoice created date filter.

            - order_by: typing.Optional[InvoiceOrderByField]. Field to order invoices by. Defaults to CREATED_AT.

            - order_direction: typing.Optional[OrderDirection]. Direction to order invoices by. Defaults to asc.

            - limit: typing.Optional[int]. Number of invoices to return. Limit can range between 1 and 100, and the default is 10.

            - starting_after: typing.Optional[InvoiceId]. The ID of the invoice to start after. If not provided, the first page of invoices will be returned.

            - search: typing.Optional[str]. Filter vendors by name. Partial matches are supported.

            - vendor_id: typing.Union[typing.Optional[EntityId], typing.List[EntityId]]. Filter invoices by vendor ID.

            - approver_id: typing.Union[typing.Optional[EntityUserId], typing.List[EntityUserId]]. Filter invoices by assigned approver user ID.

            - invoice_id: typing.Union[typing.Optional[InvoiceId], typing.List[InvoiceId]]. Filter invoices by invoice ID.

            - status: typing.Union[typing.Optional[InvoiceStatus], typing.List[InvoiceStatus]]. Invoice status to filter on
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "invoices"),
            params=remove_none_from_dict(
                {
                    "entityId": entity_id,
                    "startDate": serialize_datetime(start_date) if start_date is not None else None,
                    "endDate": serialize_datetime(end_date) if end_date is not None else None,
                    "orderBy": order_by,
                    "orderDirection": order_direction,
                    "limit": limit,
                    "startingAfter": starting_after,
                    "search": search,
                    "vendorId": vendor_id,
                    "approverId": approver_id,
                    "invoiceId": invoice_id,
                    "status": status,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(FindInvoiceResponse, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "AuthHeaderMissingError":
                raise AuthHeaderMissingError()
            if _response_json["errorName"] == "AuthHeaderMalformedError":
                raise AuthHeaderMalformedError(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unauthorized":
                raise Unauthorized(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Forbidden":
                raise Forbidden(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "NotFound":
                raise NotFound(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unimplemented":
                raise Unimplemented(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(self, *, request: InvoiceRequest) -> InvoiceResponse:
        """
        Create invoice

        Parameters:
            - request: InvoiceRequest.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "invoice"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(InvoiceResponse, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "DuplicateInvoiceNumber":
                raise DuplicateInvoiceNumber(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "InvoiceError":
                raise InvoiceError(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "AuthHeaderMissingError":
                raise AuthHeaderMissingError()
            if _response_json["errorName"] == "AuthHeaderMalformedError":
                raise AuthHeaderMalformedError(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unauthorized":
                raise Unauthorized(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Forbidden":
                raise Forbidden(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "NotFound":
                raise NotFound(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unimplemented":
                raise Unimplemented(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(self, invoice_id: InvoiceId) -> InvoiceResponse:
        """
        Get invoice

        Parameters:
            - invoice_id: InvoiceId.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"invoice/{invoice_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(InvoiceResponse, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "AuthHeaderMissingError":
                raise AuthHeaderMissingError()
            if _response_json["errorName"] == "AuthHeaderMalformedError":
                raise AuthHeaderMalformedError(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unauthorized":
                raise Unauthorized(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Forbidden":
                raise Forbidden(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "NotFound":
                raise NotFound(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unimplemented":
                raise Unimplemented(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update(self, invoice_id: InvoiceId, *, request: InvoiceRequest) -> InvoiceResponse:
        """
        Update invoice

        Parameters:
            - invoice_id: InvoiceId.

            - request: InvoiceRequest.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"invoice/{invoice_id}"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(InvoiceResponse, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "DuplicateInvoiceNumber":
                raise DuplicateInvoiceNumber(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "InvoiceError":
                raise InvoiceError(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "AuthHeaderMissingError":
                raise AuthHeaderMissingError()
            if _response_json["errorName"] == "AuthHeaderMalformedError":
                raise AuthHeaderMalformedError(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unauthorized":
                raise Unauthorized(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Forbidden":
                raise Forbidden(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "NotFound":
                raise NotFound(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unimplemented":
                raise Unimplemented(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(self, invoice_id: InvoiceId) -> None:
        """
        Delete invoice. Only invoices in the DRAFT and NEW status can be deleted.

        Parameters:
            - invoice_id: InvoiceId.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"invoice/{invoice_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if "errorName" in _response_json:
            if _response_json["errorName"] == "InvoiceStatusError":
                raise InvoiceStatusError(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "AuthHeaderMissingError":
                raise AuthHeaderMissingError()
            if _response_json["errorName"] == "AuthHeaderMalformedError":
                raise AuthHeaderMalformedError(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unauthorized":
                raise Unauthorized(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Forbidden":
                raise Forbidden(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "NotFound":
                raise NotFound(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unimplemented":
                raise Unimplemented(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_vendor_link(self, invoice_id: InvoiceId) -> str:
        """
        Get temporary link for vendor to accept payment

        Parameters:
            - invoice_id: InvoiceId.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"invoice/{invoice_id}/vendorlink"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(str, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "VendorNotFound":
                raise VendorNotFound(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "AuthHeaderMissingError":
                raise AuthHeaderMissingError()
            if _response_json["errorName"] == "AuthHeaderMalformedError":
                raise AuthHeaderMalformedError(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unauthorized":
                raise Unauthorized(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Forbidden":
                raise Forbidden(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "NotFound":
                raise NotFound(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unimplemented":
                raise Unimplemented(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)
