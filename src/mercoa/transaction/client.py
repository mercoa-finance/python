# This file was auto-generated by Fern from our API Definition.

from ..core.client_wrapper import SyncClientWrapper
import typing
from ..entity_types.types.entity_id import EntityId
import datetime as dt
from .types.transaction_id import TransactionId
from ..invoice_types.types.metadata_filter import MetadataFilter
from ..entity_types.types.entity_user_id import EntityUserId
from ..invoice_types.types.invoice_id import InvoiceId
from .types.transaction_status import TransactionStatus
from .types.transaction_type import TransactionType
from ..core.request_options import RequestOptions
from .types.find_transactions_response import FindTransactionsResponse
from ..core.datetime_utils import serialize_datetime
from ..core.serialization import convert_and_respect_annotation_metadata
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..core.pydantic_utilities import parse_obj_as
from ..commons.errors.bad_request import BadRequest
from ..commons.errors.unauthorized import Unauthorized
from ..commons.errors.forbidden import Forbidden
from ..commons.errors.not_found import NotFound
from ..commons.errors.conflict import Conflict
from ..commons.errors.internal_server_error import InternalServerError
from ..commons.errors.unimplemented import Unimplemented
from .types.transaction_response import TransactionResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.client_wrapper import AsyncClientWrapper


class TransactionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def find(
        self,
        *,
        entity_id: typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]] = None,
        start_date: typing.Optional[dt.datetime] = None,
        end_date: typing.Optional[dt.datetime] = None,
        limit: typing.Optional[int] = None,
        starting_after: typing.Optional[TransactionId] = None,
        search: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Union[MetadataFilter, typing.Sequence[MetadataFilter]]] = None,
        line_item_metadata: typing.Optional[typing.Union[MetadataFilter, typing.Sequence[MetadataFilter]]] = None,
        line_item_gl_account_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        payer_id: typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]] = None,
        vendor_id: typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]] = None,
        creator_user_id: typing.Optional[typing.Union[EntityUserId, typing.Sequence[EntityUserId]]] = None,
        invoice_id: typing.Optional[typing.Union[InvoiceId, typing.Sequence[InvoiceId]]] = None,
        transaction_id: typing.Optional[typing.Union[TransactionId, typing.Sequence[TransactionId]]] = None,
        status: typing.Optional[typing.Union[TransactionStatus, typing.Sequence[TransactionStatus]]] = None,
        transaction_type: typing.Optional[typing.Union[TransactionType, typing.Sequence[TransactionType]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FindTransactionsResponse:
        """
        Search transactions

        Parameters
        ----------
        entity_id : typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]]
            Filter transactions by the ID or foreign ID of the entity that is the payer or the vendor of the invoice that created the transaction.

        start_date : typing.Optional[dt.datetime]
            CREATED_AT Start date filter.

        end_date : typing.Optional[dt.datetime]
            CREATED_AT End date filter.

        limit : typing.Optional[int]
            Number of transactions to return. Limit can range between 1 and 100, and the default is 10.

        starting_after : typing.Optional[TransactionId]
            The ID of the transactions to start after. If not provided, the first page of transactions will be returned.

        search : typing.Optional[str]
            Find transactions by vendor name, invoice number, check number, or amount. Partial matches are supported.

        metadata : typing.Optional[typing.Union[MetadataFilter, typing.Sequence[MetadataFilter]]]
            Filter transactions by invoice metadata. Each filter will be applied as an AND condition. Duplicate keys will be ignored.

        line_item_metadata : typing.Optional[typing.Union[MetadataFilter, typing.Sequence[MetadataFilter]]]
            Filter transactions by invoice line item metadata. Each filter will be applied as an AND condition. Duplicate keys will be ignored.

        line_item_gl_account_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Filter transactions by invoice line item GL account ID. Each filter will be applied as an OR condition. Duplicate keys will be ignored.

        payer_id : typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]]
            Filter transactions by payer ID or payer foreign ID.

        vendor_id : typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]]
            Filter transactions by vendor ID or vendor foreign ID.

        creator_user_id : typing.Optional[typing.Union[EntityUserId, typing.Sequence[EntityUserId]]]
            Filter transactions by the ID or foreign ID of the user that created the invoice that created the transaction.

        invoice_id : typing.Optional[typing.Union[InvoiceId, typing.Sequence[InvoiceId]]]
            Filter transactions by invoice ID. Does not support foreign ID.

        transaction_id : typing.Optional[typing.Union[TransactionId, typing.Sequence[TransactionId]]]
            Filter transactions by transaction ID.

        status : typing.Optional[typing.Union[TransactionStatus, typing.Sequence[TransactionStatus]]]
            Transaction status to filter on

        transaction_type : typing.Optional[typing.Union[TransactionType, typing.Sequence[TransactionType]]]
            Filter transactions by transaction type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FindTransactionsResponse

        Examples
        --------
        import datetime

        from mercoa import Mercoa

        client = Mercoa(
            token="YOUR_TOKEN",
        )
        client.transaction.find(
            start_date=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            end_date=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            limit=10,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "transactions",
            method="GET",
            params={
                "entityId": entity_id,
                "startDate": serialize_datetime(start_date) if start_date is not None else None,
                "endDate": serialize_datetime(end_date) if end_date is not None else None,
                "limit": limit,
                "startingAfter": starting_after,
                "search": search,
                "metadata": convert_and_respect_annotation_metadata(
                    object_=metadata, annotation=MetadataFilter, direction="write"
                ),
                "lineItemMetadata": convert_and_respect_annotation_metadata(
                    object_=line_item_metadata,
                    annotation=MetadataFilter,
                    direction="write",
                ),
                "lineItemGlAccountId": line_item_gl_account_id,
                "payerId": payer_id,
                "vendorId": vendor_id,
                "creatorUserId": creator_user_id,
                "invoiceId": invoice_id,
                "transactionId": transaction_id,
                "status": status,
                "transactionType": transaction_type,
            },
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return typing.cast(
                FindTransactionsResponse,
                parse_obj_as(
                    type_=FindTransactionsResponse,  # type: ignore
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

    def get(
        self,
        transaction_id: TransactionId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransactionResponse:
        """
        Get Transaction

        Parameters
        ----------
        transaction_id : TransactionId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransactionResponse

        Examples
        --------
        from mercoa import Mercoa

        client = Mercoa(
            token="YOUR_TOKEN",
        )
        client.transaction.get(
            transaction_id="trx_bb08e72f-19f8-45f3-bcf9-46fdc46cb2f4",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"transaction/{jsonable_encoder(transaction_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return typing.cast(
                TransactionResponse,
                parse_obj_as(
                    type_=TransactionResponse,  # type: ignore
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


class AsyncTransactionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def find(
        self,
        *,
        entity_id: typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]] = None,
        start_date: typing.Optional[dt.datetime] = None,
        end_date: typing.Optional[dt.datetime] = None,
        limit: typing.Optional[int] = None,
        starting_after: typing.Optional[TransactionId] = None,
        search: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Union[MetadataFilter, typing.Sequence[MetadataFilter]]] = None,
        line_item_metadata: typing.Optional[typing.Union[MetadataFilter, typing.Sequence[MetadataFilter]]] = None,
        line_item_gl_account_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        payer_id: typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]] = None,
        vendor_id: typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]] = None,
        creator_user_id: typing.Optional[typing.Union[EntityUserId, typing.Sequence[EntityUserId]]] = None,
        invoice_id: typing.Optional[typing.Union[InvoiceId, typing.Sequence[InvoiceId]]] = None,
        transaction_id: typing.Optional[typing.Union[TransactionId, typing.Sequence[TransactionId]]] = None,
        status: typing.Optional[typing.Union[TransactionStatus, typing.Sequence[TransactionStatus]]] = None,
        transaction_type: typing.Optional[typing.Union[TransactionType, typing.Sequence[TransactionType]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FindTransactionsResponse:
        """
        Search transactions

        Parameters
        ----------
        entity_id : typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]]
            Filter transactions by the ID or foreign ID of the entity that is the payer or the vendor of the invoice that created the transaction.

        start_date : typing.Optional[dt.datetime]
            CREATED_AT Start date filter.

        end_date : typing.Optional[dt.datetime]
            CREATED_AT End date filter.

        limit : typing.Optional[int]
            Number of transactions to return. Limit can range between 1 and 100, and the default is 10.

        starting_after : typing.Optional[TransactionId]
            The ID of the transactions to start after. If not provided, the first page of transactions will be returned.

        search : typing.Optional[str]
            Find transactions by vendor name, invoice number, check number, or amount. Partial matches are supported.

        metadata : typing.Optional[typing.Union[MetadataFilter, typing.Sequence[MetadataFilter]]]
            Filter transactions by invoice metadata. Each filter will be applied as an AND condition. Duplicate keys will be ignored.

        line_item_metadata : typing.Optional[typing.Union[MetadataFilter, typing.Sequence[MetadataFilter]]]
            Filter transactions by invoice line item metadata. Each filter will be applied as an AND condition. Duplicate keys will be ignored.

        line_item_gl_account_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Filter transactions by invoice line item GL account ID. Each filter will be applied as an OR condition. Duplicate keys will be ignored.

        payer_id : typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]]
            Filter transactions by payer ID or payer foreign ID.

        vendor_id : typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]]
            Filter transactions by vendor ID or vendor foreign ID.

        creator_user_id : typing.Optional[typing.Union[EntityUserId, typing.Sequence[EntityUserId]]]
            Filter transactions by the ID or foreign ID of the user that created the invoice that created the transaction.

        invoice_id : typing.Optional[typing.Union[InvoiceId, typing.Sequence[InvoiceId]]]
            Filter transactions by invoice ID. Does not support foreign ID.

        transaction_id : typing.Optional[typing.Union[TransactionId, typing.Sequence[TransactionId]]]
            Filter transactions by transaction ID.

        status : typing.Optional[typing.Union[TransactionStatus, typing.Sequence[TransactionStatus]]]
            Transaction status to filter on

        transaction_type : typing.Optional[typing.Union[TransactionType, typing.Sequence[TransactionType]]]
            Filter transactions by transaction type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FindTransactionsResponse

        Examples
        --------
        import asyncio
        import datetime

        from mercoa import AsyncMercoa

        client = AsyncMercoa(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.transaction.find(
                start_date=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                end_date=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                limit=10,
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "transactions",
            method="GET",
            params={
                "entityId": entity_id,
                "startDate": serialize_datetime(start_date) if start_date is not None else None,
                "endDate": serialize_datetime(end_date) if end_date is not None else None,
                "limit": limit,
                "startingAfter": starting_after,
                "search": search,
                "metadata": convert_and_respect_annotation_metadata(
                    object_=metadata, annotation=MetadataFilter, direction="write"
                ),
                "lineItemMetadata": convert_and_respect_annotation_metadata(
                    object_=line_item_metadata,
                    annotation=MetadataFilter,
                    direction="write",
                ),
                "lineItemGlAccountId": line_item_gl_account_id,
                "payerId": payer_id,
                "vendorId": vendor_id,
                "creatorUserId": creator_user_id,
                "invoiceId": invoice_id,
                "transactionId": transaction_id,
                "status": status,
                "transactionType": transaction_type,
            },
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return typing.cast(
                FindTransactionsResponse,
                parse_obj_as(
                    type_=FindTransactionsResponse,  # type: ignore
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

    async def get(
        self,
        transaction_id: TransactionId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransactionResponse:
        """
        Get Transaction

        Parameters
        ----------
        transaction_id : TransactionId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransactionResponse

        Examples
        --------
        import asyncio

        from mercoa import AsyncMercoa

        client = AsyncMercoa(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.transaction.get(
                transaction_id="trx_bb08e72f-19f8-45f3-bcf9-46fdc46cb2f4",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"transaction/{jsonable_encoder(transaction_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return typing.cast(
                TransactionResponse,
                parse_obj_as(
                    type_=TransactionResponse,  # type: ignore
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
