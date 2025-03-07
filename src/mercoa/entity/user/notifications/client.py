# This file was auto-generated by Fern from our API Definition.

import typing
from ....core.client_wrapper import SyncClientWrapper
from ....entity_types.types.entity_id import EntityId
from ....entity_types.types.entity_user_id import EntityUserId
import datetime as dt
from ....commons.types.order_direction import OrderDirection
from ....entity_types.types.notification_id import NotificationId
from ....entity_types.types.notification_type import NotificationType
from ....entity_types.types.notification_status import NotificationStatus
from ....core.request_options import RequestOptions
from ....entity_types.types.find_notification_response import FindNotificationResponse
from ....core.jsonable_encoder import jsonable_encoder
from ....core.datetime_utils import serialize_datetime
from json.decoder import JSONDecodeError
from ....core.api_error import ApiError
from ....core.pydantic_utilities import parse_obj_as
from ....commons.errors.bad_request import BadRequest
from ....commons.errors.unauthorized import Unauthorized
from ....commons.errors.forbidden import Forbidden
from ....commons.errors.not_found import NotFound
from ....commons.errors.conflict import Conflict
from ....commons.errors.internal_server_error import InternalServerError
from ....commons.errors.unimplemented import Unimplemented
from ....entity_types.types.notification_response import NotificationResponse
from ....entity_types.types.notification_update_request import NotificationUpdateRequest
from ....core.serialization import convert_and_respect_annotation_metadata
from ....core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class NotificationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def find(
        self,
        entity_id: EntityId,
        user_id: EntityUserId,
        *,
        start_date: typing.Optional[dt.datetime] = None,
        end_date: typing.Optional[dt.datetime] = None,
        order_direction: typing.Optional[OrderDirection] = None,
        limit: typing.Optional[int] = None,
        starting_after: typing.Optional[NotificationId] = None,
        notification_type: typing.Optional[typing.Union[NotificationType, typing.Sequence[NotificationType]]] = None,
        status: typing.Optional[NotificationStatus] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FindNotificationResponse:
        """
        Parameters
        ----------
        entity_id : EntityId
            Entity ID or Entity ForeignID

        user_id : EntityUserId
            User ID or User ForeignID

        start_date : typing.Optional[dt.datetime]
            Start date for notification created on date filter.

        end_date : typing.Optional[dt.datetime]
            End date for notification created date filter.

        order_direction : typing.Optional[OrderDirection]
            Direction to order notifications by. Defaults to asc.

        limit : typing.Optional[int]
            Number of invoices to return. Limit can range between 1 and 100, and the default is 10.

        starting_after : typing.Optional[NotificationId]
            The ID of the notification to start after. If not provided, the first page of invoices will be returned.

        notification_type : typing.Optional[typing.Union[NotificationType, typing.Sequence[NotificationType]]]
            The type of notification to filter by.

        status : typing.Optional[NotificationStatus]
            The status of the notification to filter by.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FindNotificationResponse

        Examples
        --------
        from mercoa import Mercoa

        client = Mercoa(
            token="YOUR_TOKEN",
        )
        client.entity.user.notifications.find(
            entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
            user_id="user_e24fc81c-c5ee-47e8-af42-4fe29d895506",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"entity/{jsonable_encoder(entity_id)}/user/{jsonable_encoder(user_id)}/notifications",
            method="GET",
            params={
                "startDate": serialize_datetime(start_date) if start_date is not None else None,
                "endDate": serialize_datetime(end_date) if end_date is not None else None,
                "orderDirection": order_direction,
                "limit": limit,
                "startingAfter": starting_after,
                "notificationType": notification_type,
                "status": status,
            },
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return typing.cast(
                FindNotificationResponse,
                parse_obj_as(
                    type_=FindNotificationResponse,  # type: ignore
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
        user_id: EntityUserId,
        notification_id: NotificationId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NotificationResponse:
        """
        Parameters
        ----------
        entity_id : EntityId
            Entity ID or Entity ForeignID

        user_id : EntityUserId
            User ID or User ForeignID

        notification_id : NotificationId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NotificationResponse

        Examples
        --------
        from mercoa import Mercoa

        client = Mercoa(
            token="YOUR_TOKEN",
        )
        client.entity.user.notifications.get(
            entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
            user_id="user_e24fc81c-c5ee-47e8-af42-4fe29d895506",
            notification_id="notif_7df2974a-4069-454c-912f-7e58ebe030fb",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"entity/{jsonable_encoder(entity_id)}/user/{jsonable_encoder(user_id)}/notification/{jsonable_encoder(notification_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return typing.cast(
                NotificationResponse,
                parse_obj_as(
                    type_=NotificationResponse,  # type: ignore
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

    def update(
        self,
        entity_id: EntityId,
        user_id: EntityUserId,
        notification_id: NotificationId,
        *,
        request: NotificationUpdateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NotificationResponse:
        """
        Update the status of a notification.

        Parameters
        ----------
        entity_id : EntityId
            Entity ID or Entity ForeignID

        user_id : EntityUserId
            User ID or User ForeignID

        notification_id : NotificationId

        request : NotificationUpdateRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NotificationResponse

        Examples
        --------
        from mercoa import Mercoa
        from mercoa.entity_types import NotificationUpdateRequest

        client = Mercoa(
            token="YOUR_TOKEN",
        )
        client.entity.user.notifications.update(
            entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
            user_id="user_e24fc81c-c5ee-47e8-af42-4fe29d895506",
            notification_id="notif_7df2974a-4069-454c-912f-7e58ebe030fb",
            request=NotificationUpdateRequest(
                status="READ",
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"entity/{jsonable_encoder(entity_id)}/user/{jsonable_encoder(user_id)}/notification/{jsonable_encoder(notification_id)}",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=NotificationUpdateRequest, direction="write"
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
                NotificationResponse,
                parse_obj_as(
                    type_=NotificationResponse,  # type: ignore
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


class AsyncNotificationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def find(
        self,
        entity_id: EntityId,
        user_id: EntityUserId,
        *,
        start_date: typing.Optional[dt.datetime] = None,
        end_date: typing.Optional[dt.datetime] = None,
        order_direction: typing.Optional[OrderDirection] = None,
        limit: typing.Optional[int] = None,
        starting_after: typing.Optional[NotificationId] = None,
        notification_type: typing.Optional[typing.Union[NotificationType, typing.Sequence[NotificationType]]] = None,
        status: typing.Optional[NotificationStatus] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FindNotificationResponse:
        """
        Parameters
        ----------
        entity_id : EntityId
            Entity ID or Entity ForeignID

        user_id : EntityUserId
            User ID or User ForeignID

        start_date : typing.Optional[dt.datetime]
            Start date for notification created on date filter.

        end_date : typing.Optional[dt.datetime]
            End date for notification created date filter.

        order_direction : typing.Optional[OrderDirection]
            Direction to order notifications by. Defaults to asc.

        limit : typing.Optional[int]
            Number of invoices to return. Limit can range between 1 and 100, and the default is 10.

        starting_after : typing.Optional[NotificationId]
            The ID of the notification to start after. If not provided, the first page of invoices will be returned.

        notification_type : typing.Optional[typing.Union[NotificationType, typing.Sequence[NotificationType]]]
            The type of notification to filter by.

        status : typing.Optional[NotificationStatus]
            The status of the notification to filter by.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FindNotificationResponse

        Examples
        --------
        import asyncio

        from mercoa import AsyncMercoa

        client = AsyncMercoa(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.entity.user.notifications.find(
                entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
                user_id="user_e24fc81c-c5ee-47e8-af42-4fe29d895506",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"entity/{jsonable_encoder(entity_id)}/user/{jsonable_encoder(user_id)}/notifications",
            method="GET",
            params={
                "startDate": serialize_datetime(start_date) if start_date is not None else None,
                "endDate": serialize_datetime(end_date) if end_date is not None else None,
                "orderDirection": order_direction,
                "limit": limit,
                "startingAfter": starting_after,
                "notificationType": notification_type,
                "status": status,
            },
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return typing.cast(
                FindNotificationResponse,
                parse_obj_as(
                    type_=FindNotificationResponse,  # type: ignore
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
        user_id: EntityUserId,
        notification_id: NotificationId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NotificationResponse:
        """
        Parameters
        ----------
        entity_id : EntityId
            Entity ID or Entity ForeignID

        user_id : EntityUserId
            User ID or User ForeignID

        notification_id : NotificationId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NotificationResponse

        Examples
        --------
        import asyncio

        from mercoa import AsyncMercoa

        client = AsyncMercoa(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.entity.user.notifications.get(
                entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
                user_id="user_e24fc81c-c5ee-47e8-af42-4fe29d895506",
                notification_id="notif_7df2974a-4069-454c-912f-7e58ebe030fb",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"entity/{jsonable_encoder(entity_id)}/user/{jsonable_encoder(user_id)}/notification/{jsonable_encoder(notification_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return typing.cast(
                NotificationResponse,
                parse_obj_as(
                    type_=NotificationResponse,  # type: ignore
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

    async def update(
        self,
        entity_id: EntityId,
        user_id: EntityUserId,
        notification_id: NotificationId,
        *,
        request: NotificationUpdateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NotificationResponse:
        """
        Update the status of a notification.

        Parameters
        ----------
        entity_id : EntityId
            Entity ID or Entity ForeignID

        user_id : EntityUserId
            User ID or User ForeignID

        notification_id : NotificationId

        request : NotificationUpdateRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NotificationResponse

        Examples
        --------
        import asyncio

        from mercoa import AsyncMercoa
        from mercoa.entity_types import NotificationUpdateRequest

        client = AsyncMercoa(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.entity.user.notifications.update(
                entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
                user_id="user_e24fc81c-c5ee-47e8-af42-4fe29d895506",
                notification_id="notif_7df2974a-4069-454c-912f-7e58ebe030fb",
                request=NotificationUpdateRequest(
                    status="READ",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"entity/{jsonable_encoder(entity_id)}/user/{jsonable_encoder(user_id)}/notification/{jsonable_encoder(notification_id)}",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=NotificationUpdateRequest, direction="write"
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
                NotificationResponse,
                parse_obj_as(
                    type_=NotificationResponse,  # type: ignore
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
