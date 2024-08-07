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
from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.pydantic_utilities import pydantic_v1
from ...core.request_options import RequestOptions
from ...invoice_types.types.comment_id import CommentId
from ...invoice_types.types.comment_request import CommentRequest
from ...invoice_types.types.comment_response import CommentResponse
from ...invoice_types.types.invoice_id import InvoiceId

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class CommentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_all(
        self, invoice_id: InvoiceId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[CommentResponse]:
        """
        Get all comments associated with this invoice

        Parameters
        ----------
        invoice_id : InvoiceId
            Invoice ID or Invoice ForeignID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[CommentResponse]

        Examples
        --------
        from mercoa.client import Mercoa

        client = Mercoa(
            token="YOUR_TOKEN",
        )
        client.invoice.comment.get_all(
            invoice_id="inv_3d61faa9-1754-4b7b-9fcb-88ff97f368ff",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"invoice/{jsonable_encoder(invoice_id)}/comments", method="GET", request_options=request_options
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(typing.List[CommentResponse], _response_json)  # type: ignore
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

    def create(
        self, invoice_id: InvoiceId, *, request: CommentRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> CommentResponse:
        """
        Add a comment to this invoice

        Parameters
        ----------
        invoice_id : InvoiceId
            Invoice ID or Invoice ForeignID

        request : CommentRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CommentResponse

        Examples
        --------
        from mercoa import CommentRequest
        from mercoa.client import Mercoa

        client = Mercoa(
            token="YOUR_TOKEN",
        )
        client.invoice.comment.create(
            invoice_id="inv_3d61faa9-1754-4b7b-9fcb-88ff97f368ff",
            request=CommentRequest(
                text="This is a comment",
                user_id="user_e24fc81c-c5ee-47e8-af42-4fe29d895506",
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"invoice/{jsonable_encoder(invoice_id)}/comment",
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
            return pydantic_v1.parse_obj_as(CommentResponse, _response_json)  # type: ignore
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
        self, invoice_id: InvoiceId, comment_id: CommentId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CommentResponse:
        """
        Parameters
        ----------
        invoice_id : InvoiceId
            Invoice ID or Invoice ForeignID

        comment_id : CommentId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CommentResponse

        Examples
        --------
        from mercoa.client import Mercoa

        client = Mercoa(
            token="YOUR_TOKEN",
        )
        client.invoice.comment.get(
            invoice_id="inv_3d61faa9-1754-4b7b-9fcb-88ff97f368ff",
            comment_id="ic_3d61faa9-1754-4b7b-9fcb-88ff97f368ff",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"invoice/{jsonable_encoder(invoice_id)}/comment/{jsonable_encoder(comment_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(CommentResponse, _response_json)  # type: ignore
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
        invoice_id: InvoiceId,
        comment_id: CommentId,
        *,
        request: CommentRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CommentResponse:
        """
        Edit a comment on this invoice

        Parameters
        ----------
        invoice_id : InvoiceId
            Invoice ID or Invoice ForeignID

        comment_id : CommentId

        request : CommentRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CommentResponse

        Examples
        --------
        from mercoa import CommentRequest
        from mercoa.client import Mercoa

        client = Mercoa(
            token="YOUR_TOKEN",
        )
        client.invoice.comment.update(
            invoice_id="inv_3d61faa9-1754-4b7b-9fcb-88ff97f368ff",
            comment_id="ic_3d61faa9-1754-4b7b-9fcb-88ff97f368ff",
            request=CommentRequest(
                text="This is a comment",
                user_id="user_e24fc81c-c5ee-47e8-af42-4fe29d895506",
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"invoice/{jsonable_encoder(invoice_id)}/comment/{jsonable_encoder(comment_id)}",
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
            return pydantic_v1.parse_obj_as(CommentResponse, _response_json)  # type: ignore
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
        self, invoice_id: InvoiceId, comment_id: CommentId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a comment on this invoice

        Parameters
        ----------
        invoice_id : InvoiceId
            Invoice ID or Invoice ForeignID

        comment_id : CommentId

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
        client.invoice.comment.delete(
            invoice_id="inv_3d61faa9-1754-4b7b-9fcb-88ff97f368ff",
            comment_id="ic_3d61faa9-1754-4b7b-9fcb-88ff97f368ff",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"invoice/{jsonable_encoder(invoice_id)}/comment/{jsonable_encoder(comment_id)}",
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


class AsyncCommentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_all(
        self, invoice_id: InvoiceId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[CommentResponse]:
        """
        Get all comments associated with this invoice

        Parameters
        ----------
        invoice_id : InvoiceId
            Invoice ID or Invoice ForeignID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[CommentResponse]

        Examples
        --------
        import asyncio

        from mercoa.client import AsyncMercoa

        client = AsyncMercoa(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.invoice.comment.get_all(
                invoice_id="inv_3d61faa9-1754-4b7b-9fcb-88ff97f368ff",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"invoice/{jsonable_encoder(invoice_id)}/comments", method="GET", request_options=request_options
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(typing.List[CommentResponse], _response_json)  # type: ignore
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

    async def create(
        self, invoice_id: InvoiceId, *, request: CommentRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> CommentResponse:
        """
        Add a comment to this invoice

        Parameters
        ----------
        invoice_id : InvoiceId
            Invoice ID or Invoice ForeignID

        request : CommentRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CommentResponse

        Examples
        --------
        import asyncio

        from mercoa import CommentRequest
        from mercoa.client import AsyncMercoa

        client = AsyncMercoa(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.invoice.comment.create(
                invoice_id="inv_3d61faa9-1754-4b7b-9fcb-88ff97f368ff",
                request=CommentRequest(
                    text="This is a comment",
                    user_id="user_e24fc81c-c5ee-47e8-af42-4fe29d895506",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"invoice/{jsonable_encoder(invoice_id)}/comment",
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
            return pydantic_v1.parse_obj_as(CommentResponse, _response_json)  # type: ignore
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
        self, invoice_id: InvoiceId, comment_id: CommentId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CommentResponse:
        """
        Parameters
        ----------
        invoice_id : InvoiceId
            Invoice ID or Invoice ForeignID

        comment_id : CommentId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CommentResponse

        Examples
        --------
        import asyncio

        from mercoa.client import AsyncMercoa

        client = AsyncMercoa(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.invoice.comment.get(
                invoice_id="inv_3d61faa9-1754-4b7b-9fcb-88ff97f368ff",
                comment_id="ic_3d61faa9-1754-4b7b-9fcb-88ff97f368ff",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"invoice/{jsonable_encoder(invoice_id)}/comment/{jsonable_encoder(comment_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(CommentResponse, _response_json)  # type: ignore
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
        invoice_id: InvoiceId,
        comment_id: CommentId,
        *,
        request: CommentRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CommentResponse:
        """
        Edit a comment on this invoice

        Parameters
        ----------
        invoice_id : InvoiceId
            Invoice ID or Invoice ForeignID

        comment_id : CommentId

        request : CommentRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CommentResponse

        Examples
        --------
        import asyncio

        from mercoa import CommentRequest
        from mercoa.client import AsyncMercoa

        client = AsyncMercoa(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.invoice.comment.update(
                invoice_id="inv_3d61faa9-1754-4b7b-9fcb-88ff97f368ff",
                comment_id="ic_3d61faa9-1754-4b7b-9fcb-88ff97f368ff",
                request=CommentRequest(
                    text="This is a comment",
                    user_id="user_e24fc81c-c5ee-47e8-af42-4fe29d895506",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"invoice/{jsonable_encoder(invoice_id)}/comment/{jsonable_encoder(comment_id)}",
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
            return pydantic_v1.parse_obj_as(CommentResponse, _response_json)  # type: ignore
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
        self, invoice_id: InvoiceId, comment_id: CommentId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a comment on this invoice

        Parameters
        ----------
        invoice_id : InvoiceId
            Invoice ID or Invoice ForeignID

        comment_id : CommentId

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
            await client.invoice.comment.delete(
                invoice_id="inv_3d61faa9-1754-4b7b-9fcb-88ff97f368ff",
                comment_id="ic_3d61faa9-1754-4b7b-9fcb-88ff97f368ff",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"invoice/{jsonable_encoder(invoice_id)}/comment/{jsonable_encoder(comment_id)}",
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
