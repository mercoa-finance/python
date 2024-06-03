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
from ...email_log_types.types.email_log_response import EmailLogResponse
from ...invoice_types.types.document_response import DocumentResponse
from ...invoice_types.types.invoice_id import InvoiceId

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class DocumentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_all(
        self, invoice_id: InvoiceId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[DocumentResponse]:
        """
        Get attachments (scanned/uploaded PDFs and images) associated with this invoice

        Parameters
        ----------
        invoice_id : InvoiceId

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
        client.invoice.document.get_all(
            invoice_id="inv_26e7b5d3-a739-4b23-9ad9-6aaa085f47a9",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"invoice/{jsonable_encoder(invoice_id)}/documents", method="GET", request_options=request_options
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
        invoice_id: InvoiceId,
        *,
        document: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Upload documents (scanned/uploaded PDFs and images) associated with this Invoice

        Parameters
        ----------
        invoice_id : InvoiceId

        document : typing.Optional[str]
            Base64 encoded image or PDF of invoice document. PNG, JPG, and PDF are supported. 10MB max.

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
        client.invoice.document.upload(
            invoice_id="inv_26e7b5d3-a739-4b23-9ad9-6aaa085f47a9",
            document="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAAIAQMAAAD+wSzIAAAABlBMVEX///+/v7+jQ3Y5AAAADklEQVQI12P4AIX8EAgALgAD/aNpbtEAAAAASUVORK5CYII",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"invoice/{jsonable_encoder(invoice_id)}/document",
            method="POST",
            json={"document": document},
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
        self, invoice_id: InvoiceId, document_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete an attachment (scanned/uploaded PDFs and images) associated with this invoice

        Parameters
        ----------
        invoice_id : InvoiceId

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
        client.invoice.document.delete(
            invoice_id="inv_26e7b5d3-a739-4b23-9ad9-6aaa085f47a9",
            document_id="doc_37e6af0a-e637-48fd-b825-d6947b38c4e2",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"invoice/{jsonable_encoder(invoice_id)}/document/{jsonable_encoder(document_id)}",
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

    def generate_invoice_pdf(
        self, invoice_id: InvoiceId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DocumentResponse:
        """
        Generate a PDF of the invoice. This PDF is generated from the data in the invoice, not from the uploaded documents.

        Parameters
        ----------
        invoice_id : InvoiceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocumentResponse
            Link to the PDF file. Will expire after 1 hour.

        Examples
        --------
        from mercoa.client import Mercoa

        client = Mercoa(
            token="YOUR_TOKEN",
        )
        client.invoice.document.generate_invoice_pdf(
            invoice_id="inv_26e7b5d3-a739-4b23-9ad9-6aaa085f47a9",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"invoice/{jsonable_encoder(invoice_id)}/pdf/generate", method="GET", request_options=request_options
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(DocumentResponse, _response_json)  # type: ignore
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

    def generate_check_pdf(
        self, invoice_id: InvoiceId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DocumentResponse:
        """
        Get a PDF of the check for the invoice. If the invoice does not have check as the disbursement method, an error will be returned. If the disbursement option for the check is set to 'MAIL', a void copy of the check will be returned. If the disbursement option for the check is set to 'PRINT', a printable check will be returned. If the invoice is NOT marked as PAID, the check will be a void copy.

        Parameters
        ----------
        invoice_id : InvoiceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocumentResponse
            Link to the PDF file. Will expire after 1 hour.

        Examples
        --------
        from mercoa.client import Mercoa

        client = Mercoa(
            token="YOUR_TOKEN",
        )
        client.invoice.document.generate_check_pdf(
            invoice_id="inv_26e7b5d3-a739-4b23-9ad9-6aaa085f47a9",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"invoice/{jsonable_encoder(invoice_id)}/check/generate", method="GET", request_options=request_options
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(DocumentResponse, _response_json)  # type: ignore
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

    def get_source_email(
        self, invoice_id: InvoiceId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EmailLogResponse:
        """
        Get the email subject and body that was used to create this invoice.

        Parameters
        ----------
        invoice_id : InvoiceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmailLogResponse

        Examples
        --------
        from mercoa.client import Mercoa

        client = Mercoa(
            token="YOUR_TOKEN",
        )
        client.invoice.document.get_source_email(
            invoice_id="inv_26e7b5d3-a739-4b23-9ad9-6aaa085f47a9",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"invoice/{jsonable_encoder(invoice_id)}/source-email", method="GET", request_options=request_options
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(EmailLogResponse, _response_json)  # type: ignore
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
        self, invoice_id: InvoiceId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[DocumentResponse]:
        """
        Get attachments (scanned/uploaded PDFs and images) associated with this invoice

        Parameters
        ----------
        invoice_id : InvoiceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[DocumentResponse]

        Examples
        --------
        from mercoa.client import AsyncMercoa

        client = AsyncMercoa(
            token="YOUR_TOKEN",
        )
        await client.invoice.document.get_all(
            invoice_id="inv_26e7b5d3-a739-4b23-9ad9-6aaa085f47a9",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"invoice/{jsonable_encoder(invoice_id)}/documents", method="GET", request_options=request_options
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
        invoice_id: InvoiceId,
        *,
        document: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Upload documents (scanned/uploaded PDFs and images) associated with this Invoice

        Parameters
        ----------
        invoice_id : InvoiceId

        document : typing.Optional[str]
            Base64 encoded image or PDF of invoice document. PNG, JPG, and PDF are supported. 10MB max.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from mercoa.client import AsyncMercoa

        client = AsyncMercoa(
            token="YOUR_TOKEN",
        )
        await client.invoice.document.upload(
            invoice_id="inv_26e7b5d3-a739-4b23-9ad9-6aaa085f47a9",
            document="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAAIAQMAAAD+wSzIAAAABlBMVEX///+/v7+jQ3Y5AAAADklEQVQI12P4AIX8EAgALgAD/aNpbtEAAAAASUVORK5CYII",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"invoice/{jsonable_encoder(invoice_id)}/document",
            method="POST",
            json={"document": document},
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
        self, invoice_id: InvoiceId, document_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete an attachment (scanned/uploaded PDFs and images) associated with this invoice

        Parameters
        ----------
        invoice_id : InvoiceId

        document_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from mercoa.client import AsyncMercoa

        client = AsyncMercoa(
            token="YOUR_TOKEN",
        )
        await client.invoice.document.delete(
            invoice_id="inv_26e7b5d3-a739-4b23-9ad9-6aaa085f47a9",
            document_id="doc_37e6af0a-e637-48fd-b825-d6947b38c4e2",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"invoice/{jsonable_encoder(invoice_id)}/document/{jsonable_encoder(document_id)}",
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

    async def generate_invoice_pdf(
        self, invoice_id: InvoiceId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DocumentResponse:
        """
        Generate a PDF of the invoice. This PDF is generated from the data in the invoice, not from the uploaded documents.

        Parameters
        ----------
        invoice_id : InvoiceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocumentResponse
            Link to the PDF file. Will expire after 1 hour.

        Examples
        --------
        from mercoa.client import AsyncMercoa

        client = AsyncMercoa(
            token="YOUR_TOKEN",
        )
        await client.invoice.document.generate_invoice_pdf(
            invoice_id="inv_26e7b5d3-a739-4b23-9ad9-6aaa085f47a9",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"invoice/{jsonable_encoder(invoice_id)}/pdf/generate", method="GET", request_options=request_options
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(DocumentResponse, _response_json)  # type: ignore
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

    async def generate_check_pdf(
        self, invoice_id: InvoiceId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DocumentResponse:
        """
        Get a PDF of the check for the invoice. If the invoice does not have check as the disbursement method, an error will be returned. If the disbursement option for the check is set to 'MAIL', a void copy of the check will be returned. If the disbursement option for the check is set to 'PRINT', a printable check will be returned. If the invoice is NOT marked as PAID, the check will be a void copy.

        Parameters
        ----------
        invoice_id : InvoiceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocumentResponse
            Link to the PDF file. Will expire after 1 hour.

        Examples
        --------
        from mercoa.client import AsyncMercoa

        client = AsyncMercoa(
            token="YOUR_TOKEN",
        )
        await client.invoice.document.generate_check_pdf(
            invoice_id="inv_26e7b5d3-a739-4b23-9ad9-6aaa085f47a9",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"invoice/{jsonable_encoder(invoice_id)}/check/generate", method="GET", request_options=request_options
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(DocumentResponse, _response_json)  # type: ignore
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

    async def get_source_email(
        self, invoice_id: InvoiceId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EmailLogResponse:
        """
        Get the email subject and body that was used to create this invoice.

        Parameters
        ----------
        invoice_id : InvoiceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmailLogResponse

        Examples
        --------
        from mercoa.client import AsyncMercoa

        client = AsyncMercoa(
            token="YOUR_TOKEN",
        )
        await client.invoice.document.get_source_email(
            invoice_id="inv_26e7b5d3-a739-4b23-9ad9-6aaa085f47a9",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"invoice/{jsonable_encoder(invoice_id)}/source-email", method="GET", request_options=request_options
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(EmailLogResponse, _response_json)  # type: ignore
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
