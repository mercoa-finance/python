# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...commons.errors.auth_header_malformed_error import AuthHeaderMalformedError
from ...commons.errors.auth_header_missing_error import AuthHeaderMissingError
from ...commons.errors.forbidden import Forbidden
from ...commons.errors.invalid_postal_code import InvalidPostalCode
from ...commons.errors.invalid_state_or_province import InvalidStateOrProvince
from ...commons.errors.not_found import NotFound
from ...commons.errors.unauthorized import Unauthorized
from ...commons.errors.unimplemented import Unimplemented
from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.pydantic_utilities import pydantic_v1
from ...core.remove_none_from_dict import remove_none_from_dict
from ...core.request_options import RequestOptions
from ...entity_types.errors.entity_error import EntityError
from ...entity_types.errors.invalid_tax_id import InvalidTaxId
from ...entity_types.types.entity_id import EntityId
from ...entity_types.types.representative_id import RepresentativeId
from ...entity_types.types.representative_request import RepresentativeRequest
from ...entity_types.types.representative_response import RepresentativeResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class RepresentativeClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_all(
        self, entity_id: EntityId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[RepresentativeResponse]:
        """
        Get representatives for an entity

        Parameters
        ----------
        entity_id : EntityId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[RepresentativeResponse]

        Examples
        --------
        from mercoa.client import Mercoa

        client = Mercoa(
            token="YOUR_TOKEN",
        )
        client.entity.representative.get_all(
            entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"entity/{jsonable_encoder(entity_id)}/representatives"
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(typing.List[RepresentativeResponse], _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "AuthHeaderMissingError":
                raise AuthHeaderMissingError()
            if _response_json["errorName"] == "AuthHeaderMalformedError":
                raise AuthHeaderMalformedError(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unauthorized":
                raise Unauthorized(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Forbidden":
                raise Forbidden(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "NotFound":
                raise NotFound(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unimplemented":
                raise Unimplemented(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self,
        entity_id: EntityId,
        *,
        request: RepresentativeRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RepresentativeResponse:
        """
        Parameters
        ----------
        entity_id : EntityId

        request : RepresentativeRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RepresentativeResponse

        Examples
        --------
        from mercoa import (
            Address,
            BirthDate,
            FullName,
            IndividualGovernmentId,
            PhoneNumber,
            RepresentativeRequest,
            Responsibilities,
        )
        from mercoa.client import Mercoa

        client = Mercoa(
            token="YOUR_TOKEN",
        )
        client.entity.representative.create(
            entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
            request=RepresentativeRequest(
                name=FullName(
                    first_name="John",
                    middle_name="Quincy",
                    last_name="Adams",
                    suffix="Jr.",
                ),
                phone=PhoneNumber(
                    country_code="1",
                    number="4155551234",
                ),
                email="john.doe@acme.com",
                address=Address(
                    address_line_1="123 Main St",
                    address_line_2="Unit 1",
                    city="San Francisco",
                    state_or_province="CA",
                    postal_code="94105",
                    country="US",
                ),
                birth_date=BirthDate(
                    day="1",
                    month="1",
                    year="1980",
                ),
                government_id=IndividualGovernmentId(
                    ssn="123-45-6789",
                ),
                responsibilities=Responsibilities(
                    is_owner=True,
                    ownership_percentage=40,
                    is_controller=True,
                ),
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            method="POST",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"entity/{jsonable_encoder(entity_id)}/representative"
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(RepresentativeResponse, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "InvalidTaxId":
                raise InvalidTaxId(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "EntityError":
                raise EntityError(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "InvalidPostalCode":
                raise InvalidPostalCode(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "InvalidStateOrProvince":
                raise InvalidStateOrProvince(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "AuthHeaderMissingError":
                raise AuthHeaderMissingError()
            if _response_json["errorName"] == "AuthHeaderMalformedError":
                raise AuthHeaderMalformedError(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unauthorized":
                raise Unauthorized(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Forbidden":
                raise Forbidden(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "NotFound":
                raise NotFound(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unimplemented":
                raise Unimplemented(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(
        self,
        entity_id: EntityId,
        representative_id: RepresentativeId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RepresentativeResponse:
        """
        Parameters
        ----------
        entity_id : EntityId

        representative_id : RepresentativeId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RepresentativeResponse

        Examples
        --------
        from mercoa.client import Mercoa

        client = Mercoa(
            token="YOUR_TOKEN",
        )
        client.entity.representative.get(
            entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
            representative_id="rep_7df2974a-4069-454c-912f-7e58ebe030fb",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"entity/{jsonable_encoder(entity_id)}/representative/{jsonable_encoder(representative_id)}",
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(RepresentativeResponse, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "AuthHeaderMissingError":
                raise AuthHeaderMissingError()
            if _response_json["errorName"] == "AuthHeaderMalformedError":
                raise AuthHeaderMalformedError(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unauthorized":
                raise Unauthorized(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Forbidden":
                raise Forbidden(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "NotFound":
                raise NotFound(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unimplemented":
                raise Unimplemented(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(
        self,
        entity_id: EntityId,
        representative_id: RepresentativeId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        entity_id : EntityId

        representative_id : RepresentativeId

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
        client.entity.representative.delete(
            entity_id="string",
            representative_id="string",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            method="DELETE",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"entity/{jsonable_encoder(entity_id)}/representative/{jsonable_encoder(representative_id)}",
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if "errorName" in _response_json:
            if _response_json["errorName"] == "AuthHeaderMissingError":
                raise AuthHeaderMissingError()
            if _response_json["errorName"] == "AuthHeaderMalformedError":
                raise AuthHeaderMalformedError(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unauthorized":
                raise Unauthorized(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Forbidden":
                raise Forbidden(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "NotFound":
                raise NotFound(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unimplemented":
                raise Unimplemented(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncRepresentativeClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_all(
        self, entity_id: EntityId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[RepresentativeResponse]:
        """
        Get representatives for an entity

        Parameters
        ----------
        entity_id : EntityId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[RepresentativeResponse]

        Examples
        --------
        from mercoa.client import AsyncMercoa

        client = AsyncMercoa(
            token="YOUR_TOKEN",
        )
        await client.entity.representative.get_all(
            entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"entity/{jsonable_encoder(entity_id)}/representatives"
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(typing.List[RepresentativeResponse], _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "AuthHeaderMissingError":
                raise AuthHeaderMissingError()
            if _response_json["errorName"] == "AuthHeaderMalformedError":
                raise AuthHeaderMalformedError(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unauthorized":
                raise Unauthorized(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Forbidden":
                raise Forbidden(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "NotFound":
                raise NotFound(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unimplemented":
                raise Unimplemented(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(
        self,
        entity_id: EntityId,
        *,
        request: RepresentativeRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RepresentativeResponse:
        """
        Parameters
        ----------
        entity_id : EntityId

        request : RepresentativeRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RepresentativeResponse

        Examples
        --------
        from mercoa import (
            Address,
            BirthDate,
            FullName,
            IndividualGovernmentId,
            PhoneNumber,
            RepresentativeRequest,
            Responsibilities,
        )
        from mercoa.client import AsyncMercoa

        client = AsyncMercoa(
            token="YOUR_TOKEN",
        )
        await client.entity.representative.create(
            entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
            request=RepresentativeRequest(
                name=FullName(
                    first_name="John",
                    middle_name="Quincy",
                    last_name="Adams",
                    suffix="Jr.",
                ),
                phone=PhoneNumber(
                    country_code="1",
                    number="4155551234",
                ),
                email="john.doe@acme.com",
                address=Address(
                    address_line_1="123 Main St",
                    address_line_2="Unit 1",
                    city="San Francisco",
                    state_or_province="CA",
                    postal_code="94105",
                    country="US",
                ),
                birth_date=BirthDate(
                    day="1",
                    month="1",
                    year="1980",
                ),
                government_id=IndividualGovernmentId(
                    ssn="123-45-6789",
                ),
                responsibilities=Responsibilities(
                    is_owner=True,
                    ownership_percentage=40,
                    is_controller=True,
                ),
            ),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="POST",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"entity/{jsonable_encoder(entity_id)}/representative"
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(RepresentativeResponse, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "InvalidTaxId":
                raise InvalidTaxId(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "EntityError":
                raise EntityError(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "InvalidPostalCode":
                raise InvalidPostalCode(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "InvalidStateOrProvince":
                raise InvalidStateOrProvince(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "AuthHeaderMissingError":
                raise AuthHeaderMissingError()
            if _response_json["errorName"] == "AuthHeaderMalformedError":
                raise AuthHeaderMalformedError(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unauthorized":
                raise Unauthorized(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Forbidden":
                raise Forbidden(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "NotFound":
                raise NotFound(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unimplemented":
                raise Unimplemented(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(
        self,
        entity_id: EntityId,
        representative_id: RepresentativeId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RepresentativeResponse:
        """
        Parameters
        ----------
        entity_id : EntityId

        representative_id : RepresentativeId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RepresentativeResponse

        Examples
        --------
        from mercoa.client import AsyncMercoa

        client = AsyncMercoa(
            token="YOUR_TOKEN",
        )
        await client.entity.representative.get(
            entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
            representative_id="rep_7df2974a-4069-454c-912f-7e58ebe030fb",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"entity/{jsonable_encoder(entity_id)}/representative/{jsonable_encoder(representative_id)}",
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(RepresentativeResponse, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "AuthHeaderMissingError":
                raise AuthHeaderMissingError()
            if _response_json["errorName"] == "AuthHeaderMalformedError":
                raise AuthHeaderMalformedError(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unauthorized":
                raise Unauthorized(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Forbidden":
                raise Forbidden(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "NotFound":
                raise NotFound(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unimplemented":
                raise Unimplemented(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(
        self,
        entity_id: EntityId,
        representative_id: RepresentativeId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        entity_id : EntityId

        representative_id : RepresentativeId

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
        await client.entity.representative.delete(
            entity_id="string",
            representative_id="string",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="DELETE",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"entity/{jsonable_encoder(entity_id)}/representative/{jsonable_encoder(representative_id)}",
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if "errorName" in _response_json:
            if _response_json["errorName"] == "AuthHeaderMissingError":
                raise AuthHeaderMissingError()
            if _response_json["errorName"] == "AuthHeaderMalformedError":
                raise AuthHeaderMalformedError(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unauthorized":
                raise Unauthorized(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Forbidden":
                raise Forbidden(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "NotFound":
                raise NotFound(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unimplemented":
                raise Unimplemented(pydantic_v1.parse_obj_as(str, _response_json["content"]))  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)
