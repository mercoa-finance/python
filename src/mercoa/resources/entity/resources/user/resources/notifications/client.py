# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing
import urllib.parse
from json.decoder import JSONDecodeError

import httpx
import pydantic

from .......core.api_error import ApiError
from .......core.datetime_utils import serialize_datetime
from .......core.remove_none_from_headers import remove_none_from_headers
from .......environment import MercoaEnvironment
from ......commons.errors.auth_header_malformed_error import AuthHeaderMalformedError
from ......commons.errors.auth_header_missing_error import AuthHeaderMissingError
from ......commons.errors.unauthorized import Unauthorized
from ......commons.types.order_direction import OrderDirection
from ......entity_types.types.entity_id import EntityId
from ......entity_types.types.entity_user_id import EntityUserId
from ......entity_types.types.find_notification_response import FindNotificationResponse
from ......entity_types.types.notification_id import NotificationId
from ......entity_types.types.notification_response import NotificationResponse
from ......entity_types.types.notification_type import NotificationType


class NotificationsClient:
    def __init__(self, *, environment: MercoaEnvironment = MercoaEnvironment.PRODUCTION, token: str):
        self._environment = environment
        self._token = token

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
        notification_type: typing.Union[typing.Optional[NotificationType], typing.List[NotificationType]],
    ) -> FindNotificationResponse:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", f"entity/{entity_id}/user/{user_id}/notifications"),
            params={
                "startDate": serialize_datetime(start_date) if start_date is not None else None,
                "endDate": serialize_datetime(end_date) if end_date is not None else None,
                "orderDirection": order_direction,
                "limit": limit,
                "startingAfter": starting_after,
                "notificationType": notification_type,
            },
            headers=remove_none_from_headers(
                {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
            ),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(FindNotificationResponse, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "AuthHeaderMissingError":
                raise AuthHeaderMissingError()
            if _response_json["errorName"] == "AuthHeaderMalformedError":
                raise AuthHeaderMalformedError(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unauthorized":
                raise Unauthorized(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, entity_id: EntityId, user_id: EntityUserId, notification_id: NotificationId) -> NotificationResponse:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._environment.value}/", f"entity/{entity_id}/user/{user_id}/notification/{notification_id}"
            ),
            headers=remove_none_from_headers(
                {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
            ),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(NotificationResponse, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "AuthHeaderMissingError":
                raise AuthHeaderMissingError()
            if _response_json["errorName"] == "AuthHeaderMalformedError":
                raise AuthHeaderMalformedError(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unauthorized":
                raise Unauthorized(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncNotificationsClient:
    def __init__(self, *, environment: MercoaEnvironment = MercoaEnvironment.PRODUCTION, token: str):
        self._environment = environment
        self._token = token

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
        notification_type: typing.Union[typing.Optional[NotificationType], typing.List[NotificationType]],
    ) -> FindNotificationResponse:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(f"{self._environment.value}/", f"entity/{entity_id}/user/{user_id}/notifications"),
                params={
                    "startDate": serialize_datetime(start_date) if start_date is not None else None,
                    "endDate": serialize_datetime(end_date) if end_date is not None else None,
                    "orderDirection": order_direction,
                    "limit": limit,
                    "startingAfter": starting_after,
                    "notificationType": notification_type,
                },
                headers=remove_none_from_headers(
                    {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
                ),
                timeout=60,
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(FindNotificationResponse, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "AuthHeaderMissingError":
                raise AuthHeaderMissingError()
            if _response_json["errorName"] == "AuthHeaderMalformedError":
                raise AuthHeaderMalformedError(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unauthorized":
                raise Unauthorized(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(
        self, entity_id: EntityId, user_id: EntityUserId, notification_id: NotificationId
    ) -> NotificationResponse:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(
                    f"{self._environment.value}/", f"entity/{entity_id}/user/{user_id}/notification/{notification_id}"
                ),
                headers=remove_none_from_headers(
                    {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
                ),
                timeout=60,
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(NotificationResponse, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "AuthHeaderMissingError":
                raise AuthHeaderMissingError()
            if _response_json["errorName"] == "AuthHeaderMalformedError":
                raise AuthHeaderMalformedError(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unauthorized":
                raise Unauthorized(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)
