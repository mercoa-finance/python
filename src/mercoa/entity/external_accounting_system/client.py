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
from ...entity_types.types.entity_id import EntityId
from .types.external_accounting_system_company_creation_request import ExternalAccountingSystemCompanyCreationRequest
from .types.external_accounting_system_company_response import ExternalAccountingSystemCompanyResponse
from .types.sync_type import SyncType

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ExternalAccountingSystemClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(
        self, entity_id: EntityId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ExternalAccountingSystemCompanyResponse:
        """
        Get the external accounting system connected to an entity

        Parameters
        ----------
        entity_id : EntityId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExternalAccountingSystemCompanyResponse

        Examples
        --------
        from mercoa.client import Mercoa

        client = Mercoa(
            token="YOUR_TOKEN",
        )
        client.entity.external_accounting_system.get(
            entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"entity/{jsonable_encoder(entity_id)}/external-accounting-system",
            method="GET",
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(ExternalAccountingSystemCompanyResponse, _response_json)  # type: ignore
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
        self,
        entity_id: EntityId,
        *,
        request: ExternalAccountingSystemCompanyCreationRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExternalAccountingSystemCompanyResponse:
        """
        Create/Link an entity to an external accounting system like Codat or Rutter. If the entity is already linked to an external accounting system, this will return the existing connection.

        Parameters
        ----------
        entity_id : EntityId

        request : ExternalAccountingSystemCompanyCreationRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExternalAccountingSystemCompanyResponse

        Examples
        --------
        from mercoa.client import Mercoa
        from mercoa.entity import ExternalAccountingSystemCompanyCreationRequest_Rutter

        client = Mercoa(
            token="YOUR_TOKEN",
        )
        client.entity.external_accounting_system.create(
            entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
            request=ExternalAccountingSystemCompanyCreationRequest_Rutter(
                access_token="123",
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"entity/{jsonable_encoder(entity_id)}/external-accounting-system/create",
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
            return pydantic_v1.parse_obj_as(ExternalAccountingSystemCompanyResponse, _response_json)  # type: ignore
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

    def connect(self, entity_id: EntityId, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Get a link to connect an entity to an external accounting system like Quickbooks or Xero

        Parameters
        ----------
        entity_id : EntityId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str

        Examples
        --------
        from mercoa.client import Mercoa

        client = Mercoa(
            token="YOUR_TOKEN",
        )
        client.entity.external_accounting_system.connect(
            entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"entity/{jsonable_encoder(entity_id)}/external-accounting-system/connect",
            method="GET",
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(str, _response_json)  # type: ignore
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

    def sync(
        self,
        entity_id: EntityId,
        *,
        vendors: typing.Optional[SyncType] = None,
        bills: typing.Optional[SyncType] = None,
        gl_accounts: typing.Optional[SyncType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Sync an entity with an external accounting system. Will sync customers/vendors and invoices.

        Parameters
        ----------
        entity_id : EntityId

        vendors : typing.Optional[SyncType]
            Sync vendors from external accounting system. Default is to pull vendors from external system.

        bills : typing.Optional[SyncType]
            Sync bills from external accounting system. Default is to not sync bills. Invoices that already exist in both systems will not be updated, only new invoices not present in the other system will be created.

        gl_accounts : typing.Optional[SyncType]
            Sync GL accounts from external accounting system. Default is to pull GL accounts from external system. Pushing GL accounts is not supported.

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
        client.entity.external_accounting_system.sync(
            entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
            vendors="pull",
            bills="push",
            gl_accounts="pull",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"entity/{jsonable_encoder(entity_id)}/external-accounting-system/sync",
            method="GET",
            params={"vendors": vendors, "bills": bills, "glAccounts": gl_accounts},
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


class AsyncExternalAccountingSystemClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get(
        self, entity_id: EntityId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ExternalAccountingSystemCompanyResponse:
        """
        Get the external accounting system connected to an entity

        Parameters
        ----------
        entity_id : EntityId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExternalAccountingSystemCompanyResponse

        Examples
        --------
        from mercoa.client import AsyncMercoa

        client = AsyncMercoa(
            token="YOUR_TOKEN",
        )
        await client.entity.external_accounting_system.get(
            entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"entity/{jsonable_encoder(entity_id)}/external-accounting-system",
            method="GET",
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(ExternalAccountingSystemCompanyResponse, _response_json)  # type: ignore
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
        self,
        entity_id: EntityId,
        *,
        request: ExternalAccountingSystemCompanyCreationRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExternalAccountingSystemCompanyResponse:
        """
        Create/Link an entity to an external accounting system like Codat or Rutter. If the entity is already linked to an external accounting system, this will return the existing connection.

        Parameters
        ----------
        entity_id : EntityId

        request : ExternalAccountingSystemCompanyCreationRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExternalAccountingSystemCompanyResponse

        Examples
        --------
        from mercoa.client import AsyncMercoa
        from mercoa.entity import ExternalAccountingSystemCompanyCreationRequest_Rutter

        client = AsyncMercoa(
            token="YOUR_TOKEN",
        )
        await client.entity.external_accounting_system.create(
            entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
            request=ExternalAccountingSystemCompanyCreationRequest_Rutter(
                access_token="123",
            ),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"entity/{jsonable_encoder(entity_id)}/external-accounting-system/create",
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
            return pydantic_v1.parse_obj_as(ExternalAccountingSystemCompanyResponse, _response_json)  # type: ignore
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

    async def connect(self, entity_id: EntityId, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Get a link to connect an entity to an external accounting system like Quickbooks or Xero

        Parameters
        ----------
        entity_id : EntityId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str

        Examples
        --------
        from mercoa.client import AsyncMercoa

        client = AsyncMercoa(
            token="YOUR_TOKEN",
        )
        await client.entity.external_accounting_system.connect(
            entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"entity/{jsonable_encoder(entity_id)}/external-accounting-system/connect",
            method="GET",
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(str, _response_json)  # type: ignore
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

    async def sync(
        self,
        entity_id: EntityId,
        *,
        vendors: typing.Optional[SyncType] = None,
        bills: typing.Optional[SyncType] = None,
        gl_accounts: typing.Optional[SyncType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Sync an entity with an external accounting system. Will sync customers/vendors and invoices.

        Parameters
        ----------
        entity_id : EntityId

        vendors : typing.Optional[SyncType]
            Sync vendors from external accounting system. Default is to pull vendors from external system.

        bills : typing.Optional[SyncType]
            Sync bills from external accounting system. Default is to not sync bills. Invoices that already exist in both systems will not be updated, only new invoices not present in the other system will be created.

        gl_accounts : typing.Optional[SyncType]
            Sync GL accounts from external accounting system. Default is to pull GL accounts from external system. Pushing GL accounts is not supported.

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
        await client.entity.external_accounting_system.sync(
            entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
            vendors="pull",
            bills="push",
            gl_accounts="pull",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"entity/{jsonable_encoder(entity_id)}/external-accounting-system/sync",
            method="GET",
            params={"vendors": vendors, "bills": bills, "glAccounts": gl_accounts},
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
