# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ....commons.errors.bad_request import BadRequest
from ....commons.errors.conflict import Conflict
from ....commons.errors.forbidden import Forbidden
from ....commons.errors.internal_server_error import InternalServerError
from ....commons.errors.not_found import NotFound
from ....commons.errors.unauthorized import Unauthorized
from ....commons.errors.unimplemented import Unimplemented
from ....core.api_error import ApiError
from ....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ....core.jsonable_encoder import jsonable_encoder
from ....core.pydantic_utilities import pydantic_v1
from ....core.request_options import RequestOptions
from ....entity_types.types.entity_id import EntityId
from ....entity_types.types.entity_user_id import EntityUserId
from ....entity_types.types.notification_type import NotificationType
from ....entity_types.types.user_notification_policy_request import UserNotificationPolicyRequest
from ....entity_types.types.user_notification_policy_response import UserNotificationPolicyResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class NotificationPolicyClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_all(
        self, entity_id: EntityId, user_id: EntityUserId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[UserNotificationPolicyResponse]:
        """
        Retrieve all notification policies associated with this entity user

        Parameters
        ----------
        entity_id : EntityId
            Entity ID or Entity ForeignID

        user_id : EntityUserId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[UserNotificationPolicyResponse]

        Examples
        --------
        from mercoa.client import Mercoa

        client = Mercoa(
            token="YOUR_TOKEN",
        )
        client.entity.user.notification_policy.get_all(
            entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
            user_id="user_e24fc81c-c5ee-47e8-af42-4fe29d895506",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"entity/{jsonable_encoder(entity_id)}/user/{jsonable_encoder(user_id)}/notification-policies",
            method="GET",
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(typing.List[UserNotificationPolicyResponse], _response_json)  # type: ignore
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
        notification_type: NotificationType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UserNotificationPolicyResponse:
        """
        Retrieve notification policy associated with this entity user

        Parameters
        ----------
        entity_id : EntityId
            Entity ID or Entity ForeignID

        user_id : EntityUserId

        notification_type : NotificationType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserNotificationPolicyResponse

        Examples
        --------
        from mercoa.client import Mercoa

        client = Mercoa(
            token="YOUR_TOKEN",
        )
        client.entity.user.notification_policy.get(
            entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
            user_id="user_e24fc81c-c5ee-47e8-af42-4fe29d895506",
            notification_type="INVOICE_APPROVED",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"entity/{jsonable_encoder(entity_id)}/user/{jsonable_encoder(user_id)}/notification-policy/{jsonable_encoder(notification_type)}",
            method="GET",
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(UserNotificationPolicyResponse, _response_json)  # type: ignore
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

    def update(
        self,
        entity_id: EntityId,
        user_id: EntityUserId,
        notification_type: NotificationType,
        *,
        request: UserNotificationPolicyRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UserNotificationPolicyResponse:
        """
        Update notification policy associated with this entity user

        Parameters
        ----------
        entity_id : EntityId
            Entity ID or Entity ForeignID

        user_id : EntityUserId

        notification_type : NotificationType

        request : UserNotificationPolicyRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserNotificationPolicyResponse

        Examples
        --------
        from mercoa import UserNotificationPolicyRequest
        from mercoa.client import Mercoa

        client = Mercoa(
            token="YOUR_TOKEN",
        )
        client.entity.user.notification_policy.update(
            entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
            user_id="user_e24fc81c-c5ee-47e8-af42-4fe29d895506",
            notification_type="INVOICE_APPROVED",
            request=UserNotificationPolicyRequest(
                disabled=True,
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"entity/{jsonable_encoder(entity_id)}/user/{jsonable_encoder(user_id)}/notification-policy/{jsonable_encoder(notification_type)}",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(UserNotificationPolicyResponse, _response_json)  # type: ignore
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


class AsyncNotificationPolicyClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_all(
        self, entity_id: EntityId, user_id: EntityUserId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[UserNotificationPolicyResponse]:
        """
        Retrieve all notification policies associated with this entity user

        Parameters
        ----------
        entity_id : EntityId
            Entity ID or Entity ForeignID

        user_id : EntityUserId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[UserNotificationPolicyResponse]

        Examples
        --------
        import asyncio

        from mercoa.client import AsyncMercoa

        client = AsyncMercoa(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.entity.user.notification_policy.get_all(
                entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
                user_id="user_e24fc81c-c5ee-47e8-af42-4fe29d895506",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"entity/{jsonable_encoder(entity_id)}/user/{jsonable_encoder(user_id)}/notification-policies",
            method="GET",
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(typing.List[UserNotificationPolicyResponse], _response_json)  # type: ignore
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
        notification_type: NotificationType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UserNotificationPolicyResponse:
        """
        Retrieve notification policy associated with this entity user

        Parameters
        ----------
        entity_id : EntityId
            Entity ID or Entity ForeignID

        user_id : EntityUserId

        notification_type : NotificationType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserNotificationPolicyResponse

        Examples
        --------
        import asyncio

        from mercoa.client import AsyncMercoa

        client = AsyncMercoa(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.entity.user.notification_policy.get(
                entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
                user_id="user_e24fc81c-c5ee-47e8-af42-4fe29d895506",
                notification_type="INVOICE_APPROVED",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"entity/{jsonable_encoder(entity_id)}/user/{jsonable_encoder(user_id)}/notification-policy/{jsonable_encoder(notification_type)}",
            method="GET",
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(UserNotificationPolicyResponse, _response_json)  # type: ignore
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

    async def update(
        self,
        entity_id: EntityId,
        user_id: EntityUserId,
        notification_type: NotificationType,
        *,
        request: UserNotificationPolicyRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UserNotificationPolicyResponse:
        """
        Update notification policy associated with this entity user

        Parameters
        ----------
        entity_id : EntityId
            Entity ID or Entity ForeignID

        user_id : EntityUserId

        notification_type : NotificationType

        request : UserNotificationPolicyRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserNotificationPolicyResponse

        Examples
        --------
        import asyncio

        from mercoa import UserNotificationPolicyRequest
        from mercoa.client import AsyncMercoa

        client = AsyncMercoa(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.entity.user.notification_policy.update(
                entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
                user_id="user_e24fc81c-c5ee-47e8-af42-4fe29d895506",
                notification_type="INVOICE_APPROVED",
                request=UserNotificationPolicyRequest(
                    disabled=True,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"entity/{jsonable_encoder(entity_id)}/user/{jsonable_encoder(user_id)}/notification-policy/{jsonable_encoder(notification_type)}",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(UserNotificationPolicyResponse, _response_json)  # type: ignore
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
