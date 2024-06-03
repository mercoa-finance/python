# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ....commons.errors.bad_request import BadRequest
from ....commons.errors.conflict import Conflict
from ....commons.errors.forbidden import Forbidden
from ....commons.errors.internal_server_error import InternalServerError
from ....commons.errors.not_found import NotFound
from ....commons.errors.unauthorized import Unauthorized
from ....commons.errors.unimplemented import Unimplemented
from ....commons.types.order_direction import OrderDirection
from ....core.api_error import ApiError
from ....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ....core.datetime_utils import serialize_datetime
from ....core.jsonable_encoder import jsonable_encoder
from ....core.pydantic_utilities import pydantic_v1
from ....core.request_options import RequestOptions
from ....entity_types.types.entity_id import EntityId
from ....entity_types.types.entity_user_id import EntityUserId
from ....entity_types.types.find_notification_response import FindNotificationResponse
from ....entity_types.types.notification_id import NotificationId
from ....entity_types.types.notification_response import NotificationResponse
from ....entity_types.types.notification_type import NotificationType


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
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FindNotificationResponse:
        """
        Parameters
        ----------
        entity_id : EntityId

        user_id : EntityUserId

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

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FindNotificationResponse

        Examples
        --------
        from mercoa.client import Mercoa

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
            },
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(FindNotificationResponse, _response_json)  # type: ignore
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

        user_id : EntityUserId

        notification_id : NotificationId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NotificationResponse

        Examples
        --------
        from mercoa.client import Mercoa

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
            return pydantic_v1.parse_obj_as(NotificationResponse, _response_json)  # type: ignore
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
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FindNotificationResponse:
        """
        Parameters
        ----------
        entity_id : EntityId

        user_id : EntityUserId

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

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FindNotificationResponse

        Examples
        --------
        from mercoa.client import AsyncMercoa

        client = AsyncMercoa(
            token="YOUR_TOKEN",
        )
        await client.entity.user.notifications.find(
            entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
            user_id="user_e24fc81c-c5ee-47e8-af42-4fe29d895506",
        )
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
            },
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(FindNotificationResponse, _response_json)  # type: ignore
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

        user_id : EntityUserId

        notification_id : NotificationId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NotificationResponse

        Examples
        --------
        from mercoa.client import AsyncMercoa

        client = AsyncMercoa(
            token="YOUR_TOKEN",
        )
        await client.entity.user.notifications.get(
            entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
            user_id="user_e24fc81c-c5ee-47e8-af42-4fe29d895506",
            notification_id="notif_7df2974a-4069-454c-912f-7e58ebe030fb",
        )
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
            return pydantic_v1.parse_obj_as(NotificationResponse, _response_json)  # type: ignore
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
