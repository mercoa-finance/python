# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ...commons.errors.bad_request import BadRequest
from ...commons.errors.conflict import Conflict
from ...commons.errors.forbidden import Forbidden
from ...commons.errors.internal_server_error import InternalServerError
from ...commons.errors.not_found import NotFound
from ...commons.errors.unauthorized import Unauthorized
from ...commons.errors.unimplemented import Unimplemented
from ...commons.types.document_response import DocumentResponse
from ...commons.types.document_type import DocumentType
from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.pydantic_utilities import pydantic_v1
from ...core.request_options import RequestOptions
from ...entity_types.types.entity_id import EntityId

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class DocumentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_all(
        self,
        entity_id: EntityId,
        *,
        type: typing.Optional[typing.Union[DocumentType, typing.Sequence[DocumentType]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[DocumentResponse]:
        """
        Get documents (1099/W9) associated with this entity

        Parameters
        ----------
        entity_id : EntityId

        type : typing.Optional[typing.Union[DocumentType, typing.Sequence[DocumentType]]]
            Filter by document type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[DocumentResponse]

        Examples
        --------
        from mercoa.client import Mercoa

        client = Mercoa(
            token="YOUR_TOKEN",
        )
        client.entity.document.get_all(
            entity_id="ent_26e7b5d3-a739-4b23-9ad9-6aaa085f47a9",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"entity/{jsonable_encoder(entity_id)}/documents",
            method="GET",
            params={"type": type},
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(typing.List[DocumentResponse], _response_json)  # type: ignore
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

    def upload(
        self,
        entity_id: EntityId,
        *,
        document: str,
        type: DocumentType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Upload documents associated with this entity

        Parameters
        ----------
        entity_id : EntityId

        document : str
            Base64 encoded image or PDF of document. PNG, JPG, WEBP, and PDF are supported. 10MB max.

        type : DocumentType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from mercoa.client import Mercoa

        client = Mercoa(
            token="YOUR_TOKEN",
        )
        client.entity.document.upload(
            entity_id="ent_26e7b5d3-a739-4b23-9ad9-6aaa085f47a9",
            document="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAAIAQMAAAD+wSzIAAAABlBMVEX///+/v7+jQ3Y5AAAADklEQVQI12P4AIX8EAgALgAD/aNpbtEAAAAASUVORK5CYII",
            type="TEN_NINETY_NINE",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"entity/{jsonable_encoder(entity_id)}/document",
            method="POST",
            json={"document": document, "type": type},
            request_options=request_options,
            omit=OMIT,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
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

    def delete(
        self, entity_id: EntityId, document_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a document associated with this entity

        Parameters
        ----------
        entity_id : EntityId

        document_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from mercoa.client import Mercoa

        client = Mercoa(
            token="YOUR_TOKEN",
        )
        client.entity.document.delete(
            entity_id="ent_26e7b5d3-a739-4b23-9ad9-6aaa085f47a9",
            document_id="doc_37e6af0a-e637-48fd-b825-d6947b38c4e2",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"entity/{jsonable_encoder(entity_id)}/document/{jsonable_encoder(document_id)}",
            method="DELETE",
            request_options=request_options,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
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


class AsyncDocumentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_all(
        self,
        entity_id: EntityId,
        *,
        type: typing.Optional[typing.Union[DocumentType, typing.Sequence[DocumentType]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[DocumentResponse]:
        """
        Get documents (1099/W9) associated with this entity

        Parameters
        ----------
        entity_id : EntityId

        type : typing.Optional[typing.Union[DocumentType, typing.Sequence[DocumentType]]]
            Filter by document type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[DocumentResponse]

        Examples
        --------
        import asyncio

        from mercoa.client import AsyncMercoa

        client = AsyncMercoa(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.entity.document.get_all(
                entity_id="ent_26e7b5d3-a739-4b23-9ad9-6aaa085f47a9",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"entity/{jsonable_encoder(entity_id)}/documents",
            method="GET",
            params={"type": type},
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(typing.List[DocumentResponse], _response_json)  # type: ignore
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

    async def upload(
        self,
        entity_id: EntityId,
        *,
        document: str,
        type: DocumentType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Upload documents associated with this entity

        Parameters
        ----------
        entity_id : EntityId

        document : str
            Base64 encoded image or PDF of document. PNG, JPG, WEBP, and PDF are supported. 10MB max.

        type : DocumentType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from mercoa.client import AsyncMercoa

        client = AsyncMercoa(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.entity.document.upload(
                entity_id="ent_26e7b5d3-a739-4b23-9ad9-6aaa085f47a9",
                document="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAAIAQMAAAD+wSzIAAAABlBMVEX///+/v7+jQ3Y5AAAADklEQVQI12P4AIX8EAgALgAD/aNpbtEAAAAASUVORK5CYII",
                type="TEN_NINETY_NINE",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"entity/{jsonable_encoder(entity_id)}/document",
            method="POST",
            json={"document": document, "type": type},
            request_options=request_options,
            omit=OMIT,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
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

    async def delete(
        self, entity_id: EntityId, document_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a document associated with this entity

        Parameters
        ----------
        entity_id : EntityId

        document_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from mercoa.client import AsyncMercoa

        client = AsyncMercoa(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.entity.document.delete(
                entity_id="ent_26e7b5d3-a739-4b23-9ad9-6aaa085f47a9",
                document_id="doc_37e6af0a-e637-48fd-b825-d6947b38c4e2",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"entity/{jsonable_encoder(entity_id)}/document/{jsonable_encoder(document_id)}",
            method="DELETE",
            request_options=request_options,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
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
