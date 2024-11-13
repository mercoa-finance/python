# This file was auto-generated by Fern from our API Definition.

import typing
from ....core.client_wrapper import SyncClientWrapper
from ....entity_types.types.entity_id import EntityId
from ....core.request_options import RequestOptions
from ....vendor_credit_types.types.find_vendor_credit_response import FindVendorCreditResponse
from ....core.jsonable_encoder import jsonable_encoder
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
from ....vendor_credit_types.types.vendor_credit_id import VendorCreditId
from ....vendor_credit_types.types.vendor_credit_response import VendorCreditResponse
from ....vendor_credit_types.types.vendor_credit_request import VendorCreditRequest
from ....core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class VendorCreditClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_all(
        self, entity_id: EntityId, counterparty_id: EntityId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FindVendorCreditResponse:
        """
        Parameters
        ----------
        entity_id : EntityId
            Entity ID or Entity ForeignID

        counterparty_id : EntityId
            Counterparty Entity ID or Counterparty Entity ForeignID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FindVendorCreditResponse

        Examples
        --------
        from mercoa import Mercoa

        client = Mercoa(
            token="YOUR_TOKEN",
        )
        client.entity.counterparty.vendor_credit.get_all(
            entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
            counterparty_id="ent_21661ac1-a2a8-4465-a6c0-64474ba8181d",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"entity/{jsonable_encoder(entity_id)}/counterparty/{jsonable_encoder(counterparty_id)}/vendor-credits",
            method="GET",
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return typing.cast(
                FindVendorCreditResponse,
                parse_obj_as(
                    type_=FindVendorCreditResponse,  # type: ignore
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
        counterparty_id: EntityId,
        vendor_credit_id: VendorCreditId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VendorCreditResponse:
        """
        Parameters
        ----------
        entity_id : EntityId
            Entity ID or Entity ForeignID

        counterparty_id : EntityId
            Counterparty Entity ID or Counterparty Entity ForeignID

        vendor_credit_id : VendorCreditId
            ID of the vendor credit to retrieve

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VendorCreditResponse

        Examples
        --------
        from mercoa import Mercoa

        client = Mercoa(
            token="YOUR_TOKEN",
        )
        client.entity.counterparty.vendor_credit.get(
            entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
            counterparty_id="ent_21661ac1-a2a8-4465-a6c0-64474ba8181d",
            vendor_credit_id="vcr_c3f4c87d-794d-4543-9562-575cdddfc0d7",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"entity/{jsonable_encoder(entity_id)}/counterparty/{jsonable_encoder(counterparty_id)}/vendor-credit/{jsonable_encoder(vendor_credit_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return typing.cast(
                VendorCreditResponse,
                parse_obj_as(
                    type_=VendorCreditResponse,  # type: ignore
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

    def create(
        self,
        entity_id: EntityId,
        counterparty_id: EntityId,
        *,
        request: VendorCreditRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VendorCreditResponse:
        """
        Parameters
        ----------
        entity_id : EntityId
            Entity ID or Entity ForeignID

        counterparty_id : EntityId
            Counterparty Entity ID or Counterparty Entity ForeignID

        request : VendorCreditRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VendorCreditResponse

        Examples
        --------
        from mercoa import Mercoa
        from mercoa.vendor_credit_types import VendorCreditRequest

        client = Mercoa(
            token="YOUR_TOKEN",
        )
        client.entity.counterparty.vendor_credit.create(
            entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
            counterparty_id="ent_21661ac1-a2a8-4465-a6c0-64474ba8181d",
            request=VendorCreditRequest(
                total_amount=100.0,
                currency="USD",
                note="This is a note",
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"entity/{jsonable_encoder(entity_id)}/counterparty/{jsonable_encoder(counterparty_id)}/vendor-credit",
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
                VendorCreditResponse,
                parse_obj_as(
                    type_=VendorCreditResponse,  # type: ignore
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

    def delete(
        self,
        entity_id: EntityId,
        counterparty_id: EntityId,
        vendor_credit_id: VendorCreditId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        entity_id : EntityId
            Entity ID or Entity ForeignID

        counterparty_id : EntityId
            Counterparty Entity ID or Counterparty Entity ForeignID

        vendor_credit_id : VendorCreditId
            ID of the vendor credit to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from mercoa import Mercoa

        client = Mercoa(
            token="YOUR_TOKEN",
        )
        client.entity.counterparty.vendor_credit.delete(
            entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
            counterparty_id="ent_21661ac1-a2a8-4465-a6c0-64474ba8181d",
            vendor_credit_id="vcr_c3f4c87d-794d-4543-9562-575cdddfc0d7",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"entity/{jsonable_encoder(entity_id)}/counterparty/{jsonable_encoder(counterparty_id)}/vendor-credit/{jsonable_encoder(vendor_credit_id)}",
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


class AsyncVendorCreditClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_all(
        self, entity_id: EntityId, counterparty_id: EntityId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FindVendorCreditResponse:
        """
        Parameters
        ----------
        entity_id : EntityId
            Entity ID or Entity ForeignID

        counterparty_id : EntityId
            Counterparty Entity ID or Counterparty Entity ForeignID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FindVendorCreditResponse

        Examples
        --------
        import asyncio

        from mercoa import AsyncMercoa

        client = AsyncMercoa(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.entity.counterparty.vendor_credit.get_all(
                entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
                counterparty_id="ent_21661ac1-a2a8-4465-a6c0-64474ba8181d",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"entity/{jsonable_encoder(entity_id)}/counterparty/{jsonable_encoder(counterparty_id)}/vendor-credits",
            method="GET",
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return typing.cast(
                FindVendorCreditResponse,
                parse_obj_as(
                    type_=FindVendorCreditResponse,  # type: ignore
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
        counterparty_id: EntityId,
        vendor_credit_id: VendorCreditId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VendorCreditResponse:
        """
        Parameters
        ----------
        entity_id : EntityId
            Entity ID or Entity ForeignID

        counterparty_id : EntityId
            Counterparty Entity ID or Counterparty Entity ForeignID

        vendor_credit_id : VendorCreditId
            ID of the vendor credit to retrieve

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VendorCreditResponse

        Examples
        --------
        import asyncio

        from mercoa import AsyncMercoa

        client = AsyncMercoa(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.entity.counterparty.vendor_credit.get(
                entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
                counterparty_id="ent_21661ac1-a2a8-4465-a6c0-64474ba8181d",
                vendor_credit_id="vcr_c3f4c87d-794d-4543-9562-575cdddfc0d7",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"entity/{jsonable_encoder(entity_id)}/counterparty/{jsonable_encoder(counterparty_id)}/vendor-credit/{jsonable_encoder(vendor_credit_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return typing.cast(
                VendorCreditResponse,
                parse_obj_as(
                    type_=VendorCreditResponse,  # type: ignore
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

    async def create(
        self,
        entity_id: EntityId,
        counterparty_id: EntityId,
        *,
        request: VendorCreditRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VendorCreditResponse:
        """
        Parameters
        ----------
        entity_id : EntityId
            Entity ID or Entity ForeignID

        counterparty_id : EntityId
            Counterparty Entity ID or Counterparty Entity ForeignID

        request : VendorCreditRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VendorCreditResponse

        Examples
        --------
        import asyncio

        from mercoa import AsyncMercoa
        from mercoa.vendor_credit_types import VendorCreditRequest

        client = AsyncMercoa(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.entity.counterparty.vendor_credit.create(
                entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
                counterparty_id="ent_21661ac1-a2a8-4465-a6c0-64474ba8181d",
                request=VendorCreditRequest(
                    total_amount=100.0,
                    currency="USD",
                    note="This is a note",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"entity/{jsonable_encoder(entity_id)}/counterparty/{jsonable_encoder(counterparty_id)}/vendor-credit",
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
                VendorCreditResponse,
                parse_obj_as(
                    type_=VendorCreditResponse,  # type: ignore
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

    async def delete(
        self,
        entity_id: EntityId,
        counterparty_id: EntityId,
        vendor_credit_id: VendorCreditId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        entity_id : EntityId
            Entity ID or Entity ForeignID

        counterparty_id : EntityId
            Counterparty Entity ID or Counterparty Entity ForeignID

        vendor_credit_id : VendorCreditId
            ID of the vendor credit to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from mercoa import AsyncMercoa

        client = AsyncMercoa(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.entity.counterparty.vendor_credit.delete(
                entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
                counterparty_id="ent_21661ac1-a2a8-4465-a6c0-64474ba8181d",
                vendor_credit_id="vcr_c3f4c87d-794d-4543-9562-575cdddfc0d7",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"entity/{jsonable_encoder(entity_id)}/counterparty/{jsonable_encoder(counterparty_id)}/vendor-credit/{jsonable_encoder(vendor_credit_id)}",
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
