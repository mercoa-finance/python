# This file was auto-generated by Fern from our API Definition.

import typing
from ...core.client_wrapper import SyncClientWrapper
from ...entity_types.types.entity_id import EntityId
from ...core.request_options import RequestOptions
from ...entity_types.types.entity_customization_response import EntityCustomizationResponse
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
from ...entity_types.types.entity_customization_request import EntityCustomizationRequest
from ...core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class CustomizationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(
        self, entity_id: EntityId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EntityCustomizationResponse:
        """
        Get entity customization.

        Parameters
        ----------
        entity_id : EntityId
            Entity ID or Entity ForeignID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EntityCustomizationResponse

        Examples
        --------
        from mercoa import Mercoa

        client = Mercoa(
            token="YOUR_TOKEN",
        )
        client.entity.customization.get(
            entity_id="ent_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"entity/{jsonable_encoder(entity_id)}/customization",
            method="GET",
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return typing.cast(
                EntityCustomizationResponse,
                parse_obj_as(
                    type_=EntityCustomizationResponse,  # type: ignore
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
        *,
        request: EntityCustomizationRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EntityCustomizationResponse:
        """
        Update entity customization. This lets you turn off metadata and payment methods for an entity.

        Parameters
        ----------
        entity_id : EntityId
            Entity ID or Entity ForeignID

        request : EntityCustomizationRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EntityCustomizationResponse

        Examples
        --------
        from mercoa import Mercoa
        from mercoa.entity_types import (
            EntityCustomizationRequest,
            MetadataCustomizationRequest,
            NotificationCustomizationRequest,
            OcrCustomizationRequest,
            PaymentMethodCustomizationRequest,
        )

        client = Mercoa(
            token="YOUR_TOKEN",
        )
        client.entity.customization.update(
            entity_id="ent_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
            request=EntityCustomizationRequest(
                metadata=[
                    MetadataCustomizationRequest(
                        key="my_custom_field",
                        disabled=True,
                    ),
                    MetadataCustomizationRequest(
                        key="my_other_field",
                        disabled=False,
                    ),
                ],
                payment_source=[
                    PaymentMethodCustomizationRequest(
                        type="bankAccount",
                        disabled=True,
                    ),
                    PaymentMethodCustomizationRequest(
                        type="custom",
                        schema_id="cpms_7df2974a-4069-454c-912f-7e58ebe030fb",
                        disabled=True,
                    ),
                ],
                backup_disbursement=[
                    PaymentMethodCustomizationRequest(
                        type="check",
                        disabled=True,
                    )
                ],
                payment_destination=[
                    PaymentMethodCustomizationRequest(
                        type="bankAccount",
                        disabled=True,
                    ),
                    PaymentMethodCustomizationRequest(
                        type="check",
                        disabled=True,
                    ),
                ],
                ocr=OcrCustomizationRequest(
                    line_items=True,
                    invoice_metadata=True,
                    line_item_metadata=True,
                    line_item_gl_account_id=True,
                    predict_metadata=True,
                ),
                notifications=NotificationCustomizationRequest(
                    assume_role="admin",
                ),
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"entity/{jsonable_encoder(entity_id)}/customization",
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
            return typing.cast(
                EntityCustomizationResponse,
                parse_obj_as(
                    type_=EntityCustomizationResponse,  # type: ignore
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


class AsyncCustomizationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get(
        self, entity_id: EntityId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EntityCustomizationResponse:
        """
        Get entity customization.

        Parameters
        ----------
        entity_id : EntityId
            Entity ID or Entity ForeignID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EntityCustomizationResponse

        Examples
        --------
        import asyncio

        from mercoa import AsyncMercoa

        client = AsyncMercoa(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.entity.customization.get(
                entity_id="ent_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"entity/{jsonable_encoder(entity_id)}/customization",
            method="GET",
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return typing.cast(
                EntityCustomizationResponse,
                parse_obj_as(
                    type_=EntityCustomizationResponse,  # type: ignore
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
        *,
        request: EntityCustomizationRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EntityCustomizationResponse:
        """
        Update entity customization. This lets you turn off metadata and payment methods for an entity.

        Parameters
        ----------
        entity_id : EntityId
            Entity ID or Entity ForeignID

        request : EntityCustomizationRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EntityCustomizationResponse

        Examples
        --------
        import asyncio

        from mercoa import AsyncMercoa
        from mercoa.entity_types import (
            EntityCustomizationRequest,
            MetadataCustomizationRequest,
            NotificationCustomizationRequest,
            OcrCustomizationRequest,
            PaymentMethodCustomizationRequest,
        )

        client = AsyncMercoa(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.entity.customization.update(
                entity_id="ent_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
                request=EntityCustomizationRequest(
                    metadata=[
                        MetadataCustomizationRequest(
                            key="my_custom_field",
                            disabled=True,
                        ),
                        MetadataCustomizationRequest(
                            key="my_other_field",
                            disabled=False,
                        ),
                    ],
                    payment_source=[
                        PaymentMethodCustomizationRequest(
                            type="bankAccount",
                            disabled=True,
                        ),
                        PaymentMethodCustomizationRequest(
                            type="custom",
                            schema_id="cpms_7df2974a-4069-454c-912f-7e58ebe030fb",
                            disabled=True,
                        ),
                    ],
                    backup_disbursement=[
                        PaymentMethodCustomizationRequest(
                            type="check",
                            disabled=True,
                        )
                    ],
                    payment_destination=[
                        PaymentMethodCustomizationRequest(
                            type="bankAccount",
                            disabled=True,
                        ),
                        PaymentMethodCustomizationRequest(
                            type="check",
                            disabled=True,
                        ),
                    ],
                    ocr=OcrCustomizationRequest(
                        line_items=True,
                        invoice_metadata=True,
                        line_item_metadata=True,
                        line_item_gl_account_id=True,
                        predict_metadata=True,
                    ),
                    notifications=NotificationCustomizationRequest(
                        assume_role="admin",
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"entity/{jsonable_encoder(entity_id)}/customization",
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
            return typing.cast(
                EntityCustomizationResponse,
                parse_obj_as(
                    type_=EntityCustomizationResponse,  # type: ignore
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
