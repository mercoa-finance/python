# This file was auto-generated by Fern from our API Definition.

import typing
from ...core.client_wrapper import SyncClientWrapper
from ...entity_types.types.entity_id import EntityId
from ...core.request_options import RequestOptions
from ...entity_types.types.notification_policy_response import NotificationPolicyResponse
from ...core.jsonable_encoder import jsonable_encoder
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
from ...entity_types.types.notification_type import NotificationType
from ...entity_types.types.notification_policy_request import NotificationPolicyRequest
from ...core.serialization import convert_and_respect_annotation_metadata
from ...core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class NotificationPolicyClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_all(
        self, entity_id: EntityId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NotificationPolicyResponse]:
        """
        Retrieve all notification policies associated with this entity

        Parameters
        ----------
        entity_id : EntityId
            Entity ID or Entity ForeignID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NotificationPolicyResponse]

        Examples
        --------
        from mercoa import Mercoa

        client = Mercoa(
            token="YOUR_TOKEN",
        )
        client.entity.notification_policy.get_all(
            entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"entity/{jsonable_encoder(entity_id)}/notification-policies",
            method="GET",
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return typing.cast(
                typing.List[NotificationPolicyResponse],
                parse_obj_as(
                    type_=typing.List[NotificationPolicyResponse],  # type: ignore
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
        notification_type: NotificationType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NotificationPolicyResponse:
        """
        Retrieve notification policy associated with this entity

        Parameters
        ----------
        entity_id : EntityId
            Entity ID or Entity ForeignID

        notification_type : NotificationType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NotificationPolicyResponse

        Examples
        --------
        from mercoa import Mercoa

        client = Mercoa(
            token="YOUR_TOKEN",
        )
        client.entity.notification_policy.get(
            entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
            notification_type="INVOICE_APPROVAL_NEEDED",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"entity/{jsonable_encoder(entity_id)}/notification-policy/{jsonable_encoder(notification_type)}",
            method="GET",
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return typing.cast(
                NotificationPolicyResponse,
                parse_obj_as(
                    type_=NotificationPolicyResponse,  # type: ignore
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
        notification_type: NotificationType,
        *,
        request: NotificationPolicyRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NotificationPolicyResponse:
        """
        Update notification policy associated with this entity

        Parameters
        ----------
        entity_id : EntityId
            Entity ID or Entity ForeignID

        notification_type : NotificationType

        request : NotificationPolicyRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NotificationPolicyResponse

        Examples
        --------
        from mercoa import Mercoa
        from mercoa.entity_types import NotificationPolicyRequest

        client = Mercoa(
            token="YOUR_TOKEN",
        )
        client.entity.notification_policy.update(
            entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
            notification_type="INVOICE_APPROVAL_NEEDED",
            request=NotificationPolicyRequest(
                disabled=False,
                additional_roles=["admin", "approver"],
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"entity/{jsonable_encoder(entity_id)}/notification-policy/{jsonable_encoder(notification_type)}",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=NotificationPolicyRequest, direction="write"
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
                NotificationPolicyResponse,
                parse_obj_as(
                    type_=NotificationPolicyResponse,  # type: ignore
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


class AsyncNotificationPolicyClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_all(
        self, entity_id: EntityId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NotificationPolicyResponse]:
        """
        Retrieve all notification policies associated with this entity

        Parameters
        ----------
        entity_id : EntityId
            Entity ID or Entity ForeignID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NotificationPolicyResponse]

        Examples
        --------
        import asyncio

        from mercoa import AsyncMercoa

        client = AsyncMercoa(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.entity.notification_policy.get_all(
                entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"entity/{jsonable_encoder(entity_id)}/notification-policies",
            method="GET",
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return typing.cast(
                typing.List[NotificationPolicyResponse],
                parse_obj_as(
                    type_=typing.List[NotificationPolicyResponse],  # type: ignore
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
        notification_type: NotificationType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NotificationPolicyResponse:
        """
        Retrieve notification policy associated with this entity

        Parameters
        ----------
        entity_id : EntityId
            Entity ID or Entity ForeignID

        notification_type : NotificationType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NotificationPolicyResponse

        Examples
        --------
        import asyncio

        from mercoa import AsyncMercoa

        client = AsyncMercoa(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.entity.notification_policy.get(
                entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
                notification_type="INVOICE_APPROVAL_NEEDED",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"entity/{jsonable_encoder(entity_id)}/notification-policy/{jsonable_encoder(notification_type)}",
            method="GET",
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return typing.cast(
                NotificationPolicyResponse,
                parse_obj_as(
                    type_=NotificationPolicyResponse,  # type: ignore
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
        notification_type: NotificationType,
        *,
        request: NotificationPolicyRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NotificationPolicyResponse:
        """
        Update notification policy associated with this entity

        Parameters
        ----------
        entity_id : EntityId
            Entity ID or Entity ForeignID

        notification_type : NotificationType

        request : NotificationPolicyRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NotificationPolicyResponse

        Examples
        --------
        import asyncio

        from mercoa import AsyncMercoa
        from mercoa.entity_types import NotificationPolicyRequest

        client = AsyncMercoa(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.entity.notification_policy.update(
                entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
                notification_type="INVOICE_APPROVAL_NEEDED",
                request=NotificationPolicyRequest(
                    disabled=False,
                    additional_roles=["admin", "approver"],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"entity/{jsonable_encoder(entity_id)}/notification-policy/{jsonable_encoder(notification_type)}",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=NotificationPolicyRequest, direction="write"
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
                NotificationPolicyResponse,
                parse_obj_as(
                    type_=NotificationPolicyResponse,  # type: ignore
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
