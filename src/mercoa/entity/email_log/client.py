# This file was auto-generated by Fern from our API Definition.

from ...core.client_wrapper import SyncClientWrapper
from ...entity_types.types.entity_id import EntityId
import typing
import datetime as dt
from ...core.request_options import RequestOptions
from ...email_log_types.types.email_log_response import EmailLogResponse
from ...core.jsonable_encoder import jsonable_encoder
from ...core.datetime_utils import serialize_datetime
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
from ...email_log_types.types.email_log_id import EmailLogId
from ...email_log_types.types.email_log import EmailLog
from ...core.client_wrapper import AsyncClientWrapper


class EmailLogClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def find(
        self,
        entity_id: EntityId,
        *,
        start_date: typing.Optional[dt.datetime] = None,
        end_date: typing.Optional[dt.datetime] = None,
        limit: typing.Optional[int] = None,
        starting_after: typing.Optional[EntityId] = None,
        search: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EmailLogResponse:
        """
        Get all incoming invoice emails for an entity.

        Parameters
        ----------
        entity_id : EntityId
            Entity ID or Entity ForeignID

        start_date : typing.Optional[dt.datetime]

        end_date : typing.Optional[dt.datetime]

        limit : typing.Optional[int]
            Number of logs to return. Limit can range between 1 and 100, and the default is 10.

        starting_after : typing.Optional[EntityId]
            The ID of the log to start after. If not provided, the first page of logs will be returned.

        search : typing.Optional[str]
            Search for logs by email address or subject

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmailLogResponse

        Examples
        --------
        from mercoa import Mercoa

        client = Mercoa(
            token="YOUR_TOKEN",
        )
        client.entity.email_log.find(
            entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"entity/{jsonable_encoder(entity_id)}/emailLogs",
            method="GET",
            params={
                "startDate": serialize_datetime(start_date) if start_date is not None else None,
                "endDate": serialize_datetime(end_date) if end_date is not None else None,
                "limit": limit,
                "startingAfter": starting_after,
                "search": search,
            },
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return typing.cast(
                EmailLogResponse,
                parse_obj_as(
                    type_=EmailLogResponse,  # type: ignore
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
        entity_id: EntityId,
        log_id: EmailLogId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EmailLog:
        """
        Get an email log by ID

        Parameters
        ----------
        entity_id : EntityId
            Entity ID or Entity ForeignID

        log_id : EmailLogId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmailLog

        Examples
        --------
        from mercoa import Mercoa

        client = Mercoa(
            token="YOUR_TOKEN",
        )
        client.entity.email_log.get(
            entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
            log_id="log_8545a84e-a45f-41bf-bdf1-33b42a55812c",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"entity/{jsonable_encoder(entity_id)}/emailLog/{jsonable_encoder(log_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return typing.cast(
                EmailLog,
                parse_obj_as(
                    type_=EmailLog,  # type: ignore
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


class AsyncEmailLogClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def find(
        self,
        entity_id: EntityId,
        *,
        start_date: typing.Optional[dt.datetime] = None,
        end_date: typing.Optional[dt.datetime] = None,
        limit: typing.Optional[int] = None,
        starting_after: typing.Optional[EntityId] = None,
        search: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EmailLogResponse:
        """
        Get all incoming invoice emails for an entity.

        Parameters
        ----------
        entity_id : EntityId
            Entity ID or Entity ForeignID

        start_date : typing.Optional[dt.datetime]

        end_date : typing.Optional[dt.datetime]

        limit : typing.Optional[int]
            Number of logs to return. Limit can range between 1 and 100, and the default is 10.

        starting_after : typing.Optional[EntityId]
            The ID of the log to start after. If not provided, the first page of logs will be returned.

        search : typing.Optional[str]
            Search for logs by email address or subject

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmailLogResponse

        Examples
        --------
        import asyncio

        from mercoa import AsyncMercoa

        client = AsyncMercoa(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.entity.email_log.find(
                entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"entity/{jsonable_encoder(entity_id)}/emailLogs",
            method="GET",
            params={
                "startDate": serialize_datetime(start_date) if start_date is not None else None,
                "endDate": serialize_datetime(end_date) if end_date is not None else None,
                "limit": limit,
                "startingAfter": starting_after,
                "search": search,
            },
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return typing.cast(
                EmailLogResponse,
                parse_obj_as(
                    type_=EmailLogResponse,  # type: ignore
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
        entity_id: EntityId,
        log_id: EmailLogId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EmailLog:
        """
        Get an email log by ID

        Parameters
        ----------
        entity_id : EntityId
            Entity ID or Entity ForeignID

        log_id : EmailLogId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmailLog

        Examples
        --------
        import asyncio

        from mercoa import AsyncMercoa

        client = AsyncMercoa(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.entity.email_log.get(
                entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
                log_id="log_8545a84e-a45f-41bf-bdf1-33b42a55812c",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"entity/{jsonable_encoder(entity_id)}/emailLog/{jsonable_encoder(log_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return typing.cast(
                EmailLog,
                parse_obj_as(
                    type_=EmailLog,  # type: ignore
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
