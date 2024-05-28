# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...commons.errors.bad_request import BadRequest
from ...commons.errors.conflict import Conflict
from ...commons.errors.forbidden import Forbidden
from ...commons.errors.internal_server_error import InternalServerError
from ...commons.errors.not_found import NotFound
from ...commons.errors.unauthorized import Unauthorized
from ...commons.errors.unimplemented import Unimplemented
from ...commons.types.order_direction import OrderDirection
from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.datetime_utils import serialize_datetime
from ...core.jsonable_encoder import jsonable_encoder
from ...core.pydantic_utilities import pydantic_v1
from ...core.remove_none_from_dict import remove_none_from_dict
from ...core.request_options import RequestOptions
from ...entity_types.types.entity_id import EntityId
from ...entity_types.types.entity_user_id import EntityUserId
from ...invoice_types.types.approver_action import ApproverAction
from ...invoice_types.types.find_invoice_response import FindInvoiceResponse
from ...invoice_types.types.invoice_id import InvoiceId
from ...invoice_types.types.invoice_metadata_filter import InvoiceMetadataFilter
from ...invoice_types.types.invoice_metrics_per_date_group_by import InvoiceMetricsPerDateGroupBy
from ...invoice_types.types.invoice_metrics_response import InvoiceMetricsResponse
from ...invoice_types.types.invoice_order_by_field import InvoiceOrderByField
from ...invoice_types.types.invoice_status import InvoiceStatus
from ...payment_method_types.types.currency_code import CurrencyCode


class InvoiceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def find(
        self,
        entity_id: EntityId,
        *,
        exclude_payables: typing.Optional[bool] = None,
        exclude_receivables: typing.Optional[bool] = None,
        start_date: typing.Optional[dt.datetime] = None,
        end_date: typing.Optional[dt.datetime] = None,
        order_by: typing.Optional[InvoiceOrderByField] = None,
        order_direction: typing.Optional[OrderDirection] = None,
        limit: typing.Optional[int] = None,
        starting_after: typing.Optional[InvoiceId] = None,
        metadata: typing.Optional[typing.Union[InvoiceMetadataFilter, typing.Sequence[InvoiceMetadataFilter]]] = None,
        search: typing.Optional[str] = None,
        payer_id: typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]] = None,
        vendor_id: typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]] = None,
        approver_id: typing.Optional[typing.Union[EntityUserId, typing.Sequence[EntityUserId]]] = None,
        approver_action: typing.Optional[typing.Union[ApproverAction, typing.Sequence[ApproverAction]]] = None,
        invoice_id: typing.Optional[typing.Union[InvoiceId, typing.Sequence[InvoiceId]]] = None,
        status: typing.Optional[typing.Union[InvoiceStatus, typing.Sequence[InvoiceStatus]]] = None,
        include_fees: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FindInvoiceResponse:
        """
        Get invoices for an entity with the given filters.

        Parameters
        ----------
        entity_id : EntityId

        exclude_payables : typing.Optional[bool]
            Return only invoices that are receivable by the entity.

        exclude_receivables : typing.Optional[bool]
            Return only invoices that are payable by the entity.

        start_date : typing.Optional[dt.datetime]
            Start date for invoice created on date filter.

        end_date : typing.Optional[dt.datetime]
            End date for invoice created date filter.

        order_by : typing.Optional[InvoiceOrderByField]
            Field to order invoices by. Defaults to CREATED_AT.

        order_direction : typing.Optional[OrderDirection]
            Direction to order invoices by. Defaults to asc.

        limit : typing.Optional[int]
            Number of invoices to return. Limit can range between 1 and 100, and the default is 10.

        starting_after : typing.Optional[InvoiceId]
            The ID of the invoice to start after. If not provided, the first page of invoices will be returned.

        metadata : typing.Optional[typing.Union[InvoiceMetadataFilter, typing.Sequence[InvoiceMetadataFilter]]]
            Filter invoices by metadata. Each filter will be applied as an AND condition. Duplicate keys will be ignored.

        search : typing.Optional[str]
            Find invoices by vendor name, invoice number, or amount. Partial matches are supported.

        payer_id : typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]]
            Filter invoices by payer ID.

        vendor_id : typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]]
            Filter invoices by vendor ID.

        approver_id : typing.Optional[typing.Union[EntityUserId, typing.Sequence[EntityUserId]]]
            Filter invoices by assigned approver user ID.

        approver_action : typing.Optional[typing.Union[ApproverAction, typing.Sequence[ApproverAction]]]
            Filter invoices by approver action. Needs to be used with approverId. For example, if you want to find all invoices that have been approved by a specific user, you would use approverId and approverAction=APPROVE.

        invoice_id : typing.Optional[typing.Union[InvoiceId, typing.Sequence[InvoiceId]]]
            Filter invoices by invoice ID.

        status : typing.Optional[typing.Union[InvoiceStatus, typing.Sequence[InvoiceStatus]]]
            Invoice status to filter on.

        include_fees : typing.Optional[bool]
            DEPRECATED. Fees are now included by default in the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FindInvoiceResponse

        Examples
        --------
        from mercoa.client import Mercoa

        client = Mercoa(
            token="YOUR_TOKEN",
        )
        client.entity.invoice.find(
            entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
            exclude_receivables=True,
            order_by="CREATED_AT",
            order_direction="ASC",
            limit=10,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"entity/{jsonable_encoder(entity_id)}/invoices"
            ),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "excludePayables": exclude_payables,
                        "excludeReceivables": exclude_receivables,
                        "startDate": serialize_datetime(start_date) if start_date is not None else None,
                        "endDate": serialize_datetime(end_date) if end_date is not None else None,
                        "orderBy": order_by,
                        "orderDirection": order_direction,
                        "limit": limit,
                        "startingAfter": starting_after,
                        "metadata": jsonable_encoder(metadata),
                        "search": search,
                        "payerId": payer_id,
                        "vendorId": vendor_id,
                        "approverId": approver_id,
                        "approverAction": approver_action,
                        "invoiceId": invoice_id,
                        "status": status,
                        "includeFees": include_fees,
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                )
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(FindInvoiceResponse, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "BadRequest":
                raise BadRequest(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unauthorized":
                raise Unauthorized(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Forbidden":
                raise Forbidden(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "NotFound":
                raise NotFound(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Conflict":
                raise Conflict(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "InternalServerError":
                raise InternalServerError(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unimplemented":
                raise Unimplemented(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def metrics(
        self,
        entity_id: EntityId,
        *,
        search: typing.Optional[str] = None,
        exclude_payables: typing.Optional[bool] = None,
        exclude_receivables: typing.Optional[bool] = None,
        return_by_date: typing.Optional[InvoiceMetricsPerDateGroupBy] = None,
        payer_id: typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]] = None,
        vendor_id: typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]] = None,
        approver_id: typing.Optional[typing.Union[EntityUserId, typing.Sequence[EntityUserId]]] = None,
        invoice_id: typing.Optional[typing.Union[InvoiceId, typing.Sequence[InvoiceId]]] = None,
        status: typing.Optional[typing.Union[InvoiceStatus, typing.Sequence[InvoiceStatus]]] = None,
        due_date_start: typing.Optional[dt.datetime] = None,
        due_date_end: typing.Optional[dt.datetime] = None,
        created_date_start: typing.Optional[dt.datetime] = None,
        created_date_end: typing.Optional[dt.datetime] = None,
        currency: typing.Optional[typing.Union[CurrencyCode, typing.Sequence[CurrencyCode]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[InvoiceMetricsResponse]:
        """
        Get invoice metrics for an entity with the given filters. Invoices will be grouped by currency. If none of excludePayables, excludeReceivables, payerId, vendorId, or invoiceId status filters are provided, excludeReceivables will be set to true.

        Parameters
        ----------
        entity_id : EntityId

        search : typing.Optional[str]
            Find invoices by vendor name, invoice number, or amount. Partial matches are supported.

        exclude_payables : typing.Optional[bool]
            Only return invoices that are not payable by the entity. This will return only invoices that are receivable by the entity.

        exclude_receivables : typing.Optional[bool]
            Only return invoices that are not receivable by the entity. This will return only invoices that are payable by the entity.

        return_by_date : typing.Optional[InvoiceMetricsPerDateGroupBy]
            Return invoice metrics grouped by date.

        payer_id : typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]]
            Filter invoices by payer ID.

        vendor_id : typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]]
            Filter invoices by vendor ID.

        approver_id : typing.Optional[typing.Union[EntityUserId, typing.Sequence[EntityUserId]]]
            Filter invoices by assigned approver user ID.

        invoice_id : typing.Optional[typing.Union[InvoiceId, typing.Sequence[InvoiceId]]]
            Filter invoices by invoice ID.

        status : typing.Optional[typing.Union[InvoiceStatus, typing.Sequence[InvoiceStatus]]]
            Invoice status to filter on

        due_date_start : typing.Optional[dt.datetime]
            Start date for invoice dueDate filter.

        due_date_end : typing.Optional[dt.datetime]
            End date for invoice dueDate filter.

        created_date_start : typing.Optional[dt.datetime]
            Start date for invoice created on date filter.

        created_date_end : typing.Optional[dt.datetime]
            End date for invoice created date filter.

        currency : typing.Optional[typing.Union[CurrencyCode, typing.Sequence[CurrencyCode]]]
            Currency to filter on

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[InvoiceMetricsResponse]

        Examples
        --------
        import datetime

        from mercoa.client import Mercoa

        client = Mercoa(
            token="YOUR_TOKEN",
        )
        client.entity.invoice.metrics(
            entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
            return_by_date="CREATION_DATE",
            exclude_receivables=True,
            created_date_start=datetime.datetime.fromisoformat(
                "2021-01-01 00:00:00+00:00",
            ),
            created_date_end=datetime.datetime.fromisoformat(
                "2021-01-31 23:59:59.999000+00:00",
            ),
            currency="USD",
            status="NEW",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"entity/{jsonable_encoder(entity_id)}/invoice-metrics"
            ),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "search": search,
                        "excludePayables": exclude_payables,
                        "excludeReceivables": exclude_receivables,
                        "returnByDate": return_by_date,
                        "payerId": payer_id,
                        "vendorId": vendor_id,
                        "approverId": approver_id,
                        "invoiceId": invoice_id,
                        "status": status,
                        "dueDateStart": serialize_datetime(due_date_start) if due_date_start is not None else None,
                        "dueDateEnd": serialize_datetime(due_date_end) if due_date_end is not None else None,
                        "createdDateStart": serialize_datetime(created_date_start)
                        if created_date_start is not None
                        else None,
                        "createdDateEnd": serialize_datetime(created_date_end)
                        if created_date_end is not None
                        else None,
                        "currency": currency,
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                )
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(typing.List[InvoiceMetricsResponse], _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "BadRequest":
                raise BadRequest(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unauthorized":
                raise Unauthorized(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Forbidden":
                raise Forbidden(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "NotFound":
                raise NotFound(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Conflict":
                raise Conflict(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "InternalServerError":
                raise InternalServerError(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unimplemented":
                raise Unimplemented(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncInvoiceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def find(
        self,
        entity_id: EntityId,
        *,
        exclude_payables: typing.Optional[bool] = None,
        exclude_receivables: typing.Optional[bool] = None,
        start_date: typing.Optional[dt.datetime] = None,
        end_date: typing.Optional[dt.datetime] = None,
        order_by: typing.Optional[InvoiceOrderByField] = None,
        order_direction: typing.Optional[OrderDirection] = None,
        limit: typing.Optional[int] = None,
        starting_after: typing.Optional[InvoiceId] = None,
        metadata: typing.Optional[typing.Union[InvoiceMetadataFilter, typing.Sequence[InvoiceMetadataFilter]]] = None,
        search: typing.Optional[str] = None,
        payer_id: typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]] = None,
        vendor_id: typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]] = None,
        approver_id: typing.Optional[typing.Union[EntityUserId, typing.Sequence[EntityUserId]]] = None,
        approver_action: typing.Optional[typing.Union[ApproverAction, typing.Sequence[ApproverAction]]] = None,
        invoice_id: typing.Optional[typing.Union[InvoiceId, typing.Sequence[InvoiceId]]] = None,
        status: typing.Optional[typing.Union[InvoiceStatus, typing.Sequence[InvoiceStatus]]] = None,
        include_fees: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FindInvoiceResponse:
        """
        Get invoices for an entity with the given filters.

        Parameters
        ----------
        entity_id : EntityId

        exclude_payables : typing.Optional[bool]
            Return only invoices that are receivable by the entity.

        exclude_receivables : typing.Optional[bool]
            Return only invoices that are payable by the entity.

        start_date : typing.Optional[dt.datetime]
            Start date for invoice created on date filter.

        end_date : typing.Optional[dt.datetime]
            End date for invoice created date filter.

        order_by : typing.Optional[InvoiceOrderByField]
            Field to order invoices by. Defaults to CREATED_AT.

        order_direction : typing.Optional[OrderDirection]
            Direction to order invoices by. Defaults to asc.

        limit : typing.Optional[int]
            Number of invoices to return. Limit can range between 1 and 100, and the default is 10.

        starting_after : typing.Optional[InvoiceId]
            The ID of the invoice to start after. If not provided, the first page of invoices will be returned.

        metadata : typing.Optional[typing.Union[InvoiceMetadataFilter, typing.Sequence[InvoiceMetadataFilter]]]
            Filter invoices by metadata. Each filter will be applied as an AND condition. Duplicate keys will be ignored.

        search : typing.Optional[str]
            Find invoices by vendor name, invoice number, or amount. Partial matches are supported.

        payer_id : typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]]
            Filter invoices by payer ID.

        vendor_id : typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]]
            Filter invoices by vendor ID.

        approver_id : typing.Optional[typing.Union[EntityUserId, typing.Sequence[EntityUserId]]]
            Filter invoices by assigned approver user ID.

        approver_action : typing.Optional[typing.Union[ApproverAction, typing.Sequence[ApproverAction]]]
            Filter invoices by approver action. Needs to be used with approverId. For example, if you want to find all invoices that have been approved by a specific user, you would use approverId and approverAction=APPROVE.

        invoice_id : typing.Optional[typing.Union[InvoiceId, typing.Sequence[InvoiceId]]]
            Filter invoices by invoice ID.

        status : typing.Optional[typing.Union[InvoiceStatus, typing.Sequence[InvoiceStatus]]]
            Invoice status to filter on.

        include_fees : typing.Optional[bool]
            DEPRECATED. Fees are now included by default in the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FindInvoiceResponse

        Examples
        --------
        from mercoa.client import AsyncMercoa

        client = AsyncMercoa(
            token="YOUR_TOKEN",
        )
        await client.entity.invoice.find(
            entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
            exclude_receivables=True,
            order_by="CREATED_AT",
            order_direction="ASC",
            limit=10,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"entity/{jsonable_encoder(entity_id)}/invoices"
            ),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "excludePayables": exclude_payables,
                        "excludeReceivables": exclude_receivables,
                        "startDate": serialize_datetime(start_date) if start_date is not None else None,
                        "endDate": serialize_datetime(end_date) if end_date is not None else None,
                        "orderBy": order_by,
                        "orderDirection": order_direction,
                        "limit": limit,
                        "startingAfter": starting_after,
                        "metadata": jsonable_encoder(metadata),
                        "search": search,
                        "payerId": payer_id,
                        "vendorId": vendor_id,
                        "approverId": approver_id,
                        "approverAction": approver_action,
                        "invoiceId": invoice_id,
                        "status": status,
                        "includeFees": include_fees,
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                )
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(FindInvoiceResponse, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "BadRequest":
                raise BadRequest(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unauthorized":
                raise Unauthorized(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Forbidden":
                raise Forbidden(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "NotFound":
                raise NotFound(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Conflict":
                raise Conflict(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "InternalServerError":
                raise InternalServerError(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unimplemented":
                raise Unimplemented(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def metrics(
        self,
        entity_id: EntityId,
        *,
        search: typing.Optional[str] = None,
        exclude_payables: typing.Optional[bool] = None,
        exclude_receivables: typing.Optional[bool] = None,
        return_by_date: typing.Optional[InvoiceMetricsPerDateGroupBy] = None,
        payer_id: typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]] = None,
        vendor_id: typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]] = None,
        approver_id: typing.Optional[typing.Union[EntityUserId, typing.Sequence[EntityUserId]]] = None,
        invoice_id: typing.Optional[typing.Union[InvoiceId, typing.Sequence[InvoiceId]]] = None,
        status: typing.Optional[typing.Union[InvoiceStatus, typing.Sequence[InvoiceStatus]]] = None,
        due_date_start: typing.Optional[dt.datetime] = None,
        due_date_end: typing.Optional[dt.datetime] = None,
        created_date_start: typing.Optional[dt.datetime] = None,
        created_date_end: typing.Optional[dt.datetime] = None,
        currency: typing.Optional[typing.Union[CurrencyCode, typing.Sequence[CurrencyCode]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[InvoiceMetricsResponse]:
        """
        Get invoice metrics for an entity with the given filters. Invoices will be grouped by currency. If none of excludePayables, excludeReceivables, payerId, vendorId, or invoiceId status filters are provided, excludeReceivables will be set to true.

        Parameters
        ----------
        entity_id : EntityId

        search : typing.Optional[str]
            Find invoices by vendor name, invoice number, or amount. Partial matches are supported.

        exclude_payables : typing.Optional[bool]
            Only return invoices that are not payable by the entity. This will return only invoices that are receivable by the entity.

        exclude_receivables : typing.Optional[bool]
            Only return invoices that are not receivable by the entity. This will return only invoices that are payable by the entity.

        return_by_date : typing.Optional[InvoiceMetricsPerDateGroupBy]
            Return invoice metrics grouped by date.

        payer_id : typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]]
            Filter invoices by payer ID.

        vendor_id : typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]]
            Filter invoices by vendor ID.

        approver_id : typing.Optional[typing.Union[EntityUserId, typing.Sequence[EntityUserId]]]
            Filter invoices by assigned approver user ID.

        invoice_id : typing.Optional[typing.Union[InvoiceId, typing.Sequence[InvoiceId]]]
            Filter invoices by invoice ID.

        status : typing.Optional[typing.Union[InvoiceStatus, typing.Sequence[InvoiceStatus]]]
            Invoice status to filter on

        due_date_start : typing.Optional[dt.datetime]
            Start date for invoice dueDate filter.

        due_date_end : typing.Optional[dt.datetime]
            End date for invoice dueDate filter.

        created_date_start : typing.Optional[dt.datetime]
            Start date for invoice created on date filter.

        created_date_end : typing.Optional[dt.datetime]
            End date for invoice created date filter.

        currency : typing.Optional[typing.Union[CurrencyCode, typing.Sequence[CurrencyCode]]]
            Currency to filter on

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[InvoiceMetricsResponse]

        Examples
        --------
        import datetime

        from mercoa.client import AsyncMercoa

        client = AsyncMercoa(
            token="YOUR_TOKEN",
        )
        await client.entity.invoice.metrics(
            entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
            return_by_date="CREATION_DATE",
            exclude_receivables=True,
            created_date_start=datetime.datetime.fromisoformat(
                "2021-01-01 00:00:00+00:00",
            ),
            created_date_end=datetime.datetime.fromisoformat(
                "2021-01-31 23:59:59.999000+00:00",
            ),
            currency="USD",
            status="NEW",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"entity/{jsonable_encoder(entity_id)}/invoice-metrics"
            ),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "search": search,
                        "excludePayables": exclude_payables,
                        "excludeReceivables": exclude_receivables,
                        "returnByDate": return_by_date,
                        "payerId": payer_id,
                        "vendorId": vendor_id,
                        "approverId": approver_id,
                        "invoiceId": invoice_id,
                        "status": status,
                        "dueDateStart": serialize_datetime(due_date_start) if due_date_start is not None else None,
                        "dueDateEnd": serialize_datetime(due_date_end) if due_date_end is not None else None,
                        "createdDateStart": serialize_datetime(created_date_start)
                        if created_date_start is not None
                        else None,
                        "createdDateEnd": serialize_datetime(created_date_end)
                        if created_date_end is not None
                        else None,
                        "currency": currency,
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                )
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(typing.List[InvoiceMetricsResponse], _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "BadRequest":
                raise BadRequest(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unauthorized":
                raise Unauthorized(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Forbidden":
                raise Forbidden(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "NotFound":
                raise NotFound(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Conflict":
                raise Conflict(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "InternalServerError":
                raise InternalServerError(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unimplemented":
                raise Unimplemented(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)
