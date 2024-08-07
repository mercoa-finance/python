# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ..commons.errors.bad_request import BadRequest
from ..commons.errors.conflict import Conflict
from ..commons.errors.forbidden import Forbidden
from ..commons.errors.internal_server_error import InternalServerError
from ..commons.errors.not_found import NotFound
from ..commons.errors.unauthorized import Unauthorized
from ..commons.errors.unimplemented import Unimplemented
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import pydantic_v1
from ..core.request_options import RequestOptions
from ..payment_method_types.types.custom_payment_method_schema_id import CustomPaymentMethodSchemaId
from ..payment_method_types.types.custom_payment_method_schema_request import CustomPaymentMethodSchemaRequest
from ..payment_method_types.types.custom_payment_method_schema_response import CustomPaymentMethodSchemaResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class CustomPaymentMethodSchemaClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_all(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[CustomPaymentMethodSchemaResponse]:
        """
        Get all custom payment method schemas

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[CustomPaymentMethodSchemaResponse]

        Examples
        --------
        from mercoa.client import Mercoa

        client = Mercoa(
            token="YOUR_TOKEN",
        )
        client.custom_payment_method_schema.get_all()
        """
        _response = self._client_wrapper.httpx_client.request(
            "paymentMethod/schema", method="GET", request_options=request_options
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(typing.List[CustomPaymentMethodSchemaResponse], _response_json)  # type: ignore
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
        self, *, request: CustomPaymentMethodSchemaRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> CustomPaymentMethodSchemaResponse:
        """
        Create custom payment method schema

        Parameters
        ----------
        request : CustomPaymentMethodSchemaRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CustomPaymentMethodSchemaResponse

        Examples
        --------
        from mercoa import (
            CustomPaymentMethodSchemaField,
            CustomPaymentMethodSchemaRequest,
        )
        from mercoa.client import Mercoa

        client = Mercoa(
            token="YOUR_TOKEN",
        )
        client.custom_payment_method_schema.create(
            request=CustomPaymentMethodSchemaRequest(
                name="Wire",
                is_source=False,
                is_destination=True,
                supported_currencies=["USD", "EUR"],
                fields=[
                    CustomPaymentMethodSchemaField(
                        name="bankName",
                        display_name="Bank Name",
                        type="text",
                        optional=False,
                    ),
                    CustomPaymentMethodSchemaField(
                        name="recipientName",
                        display_name="Recipient Name",
                        type="text",
                        optional=False,
                    ),
                    CustomPaymentMethodSchemaField(
                        name="accountNumber",
                        display_name="Account Number",
                        type="usBankAccountNumber",
                        optional=False,
                        use_as_account_number=True,
                    ),
                    CustomPaymentMethodSchemaField(
                        name="routingNumber",
                        display_name="Routing Number",
                        type="usBankRoutingNumber",
                        optional=False,
                    ),
                ],
                estimated_processing_time=0,
                max_amount=100000.0,
                min_amount=1.0,
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "paymentMethod/schema", method="POST", json=request, request_options=request_options, omit=OMIT
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(CustomPaymentMethodSchemaResponse, _response_json)  # type: ignore
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
        schema_id: CustomPaymentMethodSchemaId,
        *,
        request: CustomPaymentMethodSchemaRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CustomPaymentMethodSchemaResponse:
        """
        Update custom payment method schema

        Parameters
        ----------
        schema_id : CustomPaymentMethodSchemaId

        request : CustomPaymentMethodSchemaRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CustomPaymentMethodSchemaResponse

        Examples
        --------
        from mercoa import (
            CustomPaymentMethodSchemaField,
            CustomPaymentMethodSchemaRequest,
        )
        from mercoa.client import Mercoa

        client = Mercoa(
            token="YOUR_TOKEN",
        )
        client.custom_payment_method_schema.update(
            schema_id="cpms_14f78dcd-4614-426e-a37a-7af262431d41",
            request=CustomPaymentMethodSchemaRequest(
                name="Check",
                is_source=False,
                is_destination=True,
                supported_currencies=["USD"],
                fields=[
                    CustomPaymentMethodSchemaField(
                        name="payToTheOrderOf",
                        display_name="Pay To The Order Of",
                        type="text",
                        optional=False,
                    ),
                    CustomPaymentMethodSchemaField(
                        name="accountNumber",
                        display_name="Account Number",
                        type="usBankAccountNumber",
                        optional=False,
                        use_as_account_number=True,
                    ),
                    CustomPaymentMethodSchemaField(
                        name="routingNumber",
                        display_name="Routing Number",
                        type="usBankRoutingNumber",
                        optional=False,
                    ),
                    CustomPaymentMethodSchemaField(
                        name="address",
                        display_name="Address",
                        type="address",
                        optional=False,
                    ),
                ],
                estimated_processing_time=7,
                max_amount=50000.0,
                min_amount=1.0,
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"paymentMethod/schema/{jsonable_encoder(schema_id)}",
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
            return pydantic_v1.parse_obj_as(CustomPaymentMethodSchemaResponse, _response_json)  # type: ignore
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
        self, schema_id: CustomPaymentMethodSchemaId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CustomPaymentMethodSchemaResponse:
        """
        Get custom payment method schema

        Parameters
        ----------
        schema_id : CustomPaymentMethodSchemaId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CustomPaymentMethodSchemaResponse

        Examples
        --------
        from mercoa.client import Mercoa

        client = Mercoa(
            token="YOUR_TOKEN",
        )
        client.custom_payment_method_schema.get(
            schema_id="cpms_14f78dcd-4614-426e-a37a-7af262431d41",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"paymentMethod/schema/{jsonable_encoder(schema_id)}", method="GET", request_options=request_options
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(CustomPaymentMethodSchemaResponse, _response_json)  # type: ignore
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
        self, schema_id: CustomPaymentMethodSchemaId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete custom payment method schema. Schema that have been used in an invoice cannot be deleted.

        Parameters
        ----------
        schema_id : CustomPaymentMethodSchemaId

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
        client.custom_payment_method_schema.delete(
            schema_id="cpms_14f78dcd-4614-426e-a37a-7af262431d41",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"paymentMethod/schema/{jsonable_encoder(schema_id)}", method="DELETE", request_options=request_options
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


class AsyncCustomPaymentMethodSchemaClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_all(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[CustomPaymentMethodSchemaResponse]:
        """
        Get all custom payment method schemas

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[CustomPaymentMethodSchemaResponse]

        Examples
        --------
        import asyncio

        from mercoa.client import AsyncMercoa

        client = AsyncMercoa(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.custom_payment_method_schema.get_all()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "paymentMethod/schema", method="GET", request_options=request_options
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(typing.List[CustomPaymentMethodSchemaResponse], _response_json)  # type: ignore
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
        self, *, request: CustomPaymentMethodSchemaRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> CustomPaymentMethodSchemaResponse:
        """
        Create custom payment method schema

        Parameters
        ----------
        request : CustomPaymentMethodSchemaRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CustomPaymentMethodSchemaResponse

        Examples
        --------
        import asyncio

        from mercoa import (
            CustomPaymentMethodSchemaField,
            CustomPaymentMethodSchemaRequest,
        )
        from mercoa.client import AsyncMercoa

        client = AsyncMercoa(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.custom_payment_method_schema.create(
                request=CustomPaymentMethodSchemaRequest(
                    name="Wire",
                    is_source=False,
                    is_destination=True,
                    supported_currencies=["USD", "EUR"],
                    fields=[
                        CustomPaymentMethodSchemaField(
                            name="bankName",
                            display_name="Bank Name",
                            type="text",
                            optional=False,
                        ),
                        CustomPaymentMethodSchemaField(
                            name="recipientName",
                            display_name="Recipient Name",
                            type="text",
                            optional=False,
                        ),
                        CustomPaymentMethodSchemaField(
                            name="accountNumber",
                            display_name="Account Number",
                            type="usBankAccountNumber",
                            optional=False,
                            use_as_account_number=True,
                        ),
                        CustomPaymentMethodSchemaField(
                            name="routingNumber",
                            display_name="Routing Number",
                            type="usBankRoutingNumber",
                            optional=False,
                        ),
                    ],
                    estimated_processing_time=0,
                    max_amount=100000.0,
                    min_amount=1.0,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "paymentMethod/schema", method="POST", json=request, request_options=request_options, omit=OMIT
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(CustomPaymentMethodSchemaResponse, _response_json)  # type: ignore
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
        schema_id: CustomPaymentMethodSchemaId,
        *,
        request: CustomPaymentMethodSchemaRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CustomPaymentMethodSchemaResponse:
        """
        Update custom payment method schema

        Parameters
        ----------
        schema_id : CustomPaymentMethodSchemaId

        request : CustomPaymentMethodSchemaRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CustomPaymentMethodSchemaResponse

        Examples
        --------
        import asyncio

        from mercoa import (
            CustomPaymentMethodSchemaField,
            CustomPaymentMethodSchemaRequest,
        )
        from mercoa.client import AsyncMercoa

        client = AsyncMercoa(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.custom_payment_method_schema.update(
                schema_id="cpms_14f78dcd-4614-426e-a37a-7af262431d41",
                request=CustomPaymentMethodSchemaRequest(
                    name="Check",
                    is_source=False,
                    is_destination=True,
                    supported_currencies=["USD"],
                    fields=[
                        CustomPaymentMethodSchemaField(
                            name="payToTheOrderOf",
                            display_name="Pay To The Order Of",
                            type="text",
                            optional=False,
                        ),
                        CustomPaymentMethodSchemaField(
                            name="accountNumber",
                            display_name="Account Number",
                            type="usBankAccountNumber",
                            optional=False,
                            use_as_account_number=True,
                        ),
                        CustomPaymentMethodSchemaField(
                            name="routingNumber",
                            display_name="Routing Number",
                            type="usBankRoutingNumber",
                            optional=False,
                        ),
                        CustomPaymentMethodSchemaField(
                            name="address",
                            display_name="Address",
                            type="address",
                            optional=False,
                        ),
                    ],
                    estimated_processing_time=7,
                    max_amount=50000.0,
                    min_amount=1.0,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"paymentMethod/schema/{jsonable_encoder(schema_id)}",
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
            return pydantic_v1.parse_obj_as(CustomPaymentMethodSchemaResponse, _response_json)  # type: ignore
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
        self, schema_id: CustomPaymentMethodSchemaId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CustomPaymentMethodSchemaResponse:
        """
        Get custom payment method schema

        Parameters
        ----------
        schema_id : CustomPaymentMethodSchemaId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CustomPaymentMethodSchemaResponse

        Examples
        --------
        import asyncio

        from mercoa.client import AsyncMercoa

        client = AsyncMercoa(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.custom_payment_method_schema.get(
                schema_id="cpms_14f78dcd-4614-426e-a37a-7af262431d41",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"paymentMethod/schema/{jsonable_encoder(schema_id)}", method="GET", request_options=request_options
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(CustomPaymentMethodSchemaResponse, _response_json)  # type: ignore
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
        self, schema_id: CustomPaymentMethodSchemaId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete custom payment method schema. Schema that have been used in an invoice cannot be deleted.

        Parameters
        ----------
        schema_id : CustomPaymentMethodSchemaId

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
            await client.custom_payment_method_schema.delete(
                schema_id="cpms_14f78dcd-4614-426e-a37a-7af262431d41",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"paymentMethod/schema/{jsonable_encoder(schema_id)}", method="DELETE", request_options=request_options
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
