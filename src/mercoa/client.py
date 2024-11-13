# This file was auto-generated by Fern from our API Definition.

import typing
from .environment import MercoaEnvironment
import httpx
from .core.client_wrapper import SyncClientWrapper
from .entity_group.client import EntityGroupClient
from .entity.client import EntityClient
from .invoice_template.client import InvoiceTemplateClient
from .invoice.client import InvoiceClient
from .organization.client import OrganizationClient
from .bank_lookup.client import BankLookupClient
from .calculate.client import CalculateClient
from .custom_payment_method_schema.client import CustomPaymentMethodSchemaClient
from .ocr.client import OcrClient
from .payment_methods.client import PaymentMethodsClient
from .core.client_wrapper import AsyncClientWrapper
from .entity_group.client import AsyncEntityGroupClient
from .entity.client import AsyncEntityClient
from .invoice_template.client import AsyncInvoiceTemplateClient
from .invoice.client import AsyncInvoiceClient
from .organization.client import AsyncOrganizationClient
from .bank_lookup.client import AsyncBankLookupClient
from .calculate.client import AsyncCalculateClient
from .custom_payment_method_schema.client import AsyncCustomPaymentMethodSchemaClient
from .ocr.client import AsyncOcrClient
from .payment_methods.client import AsyncPaymentMethodsClient


class Mercoa:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : MercoaEnvironment
        The environment to use for requests from the client. from .environment import MercoaEnvironment



        Defaults to MercoaEnvironment.PRODUCTION



    token : typing.Union[str, typing.Callable[[], str]]
    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.Client]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    Examples
    --------
    from mercoa import Mercoa

    client = Mercoa(
        token="YOUR_TOKEN",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: MercoaEnvironment = MercoaEnvironment.PRODUCTION,
        token: typing.Union[str, typing.Callable[[], str]],
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            token=token,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.Client(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.Client(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self.entity_group = EntityGroupClient(client_wrapper=self._client_wrapper)
        self.entity = EntityClient(client_wrapper=self._client_wrapper)
        self.invoice_template = InvoiceTemplateClient(client_wrapper=self._client_wrapper)
        self.invoice = InvoiceClient(client_wrapper=self._client_wrapper)
        self.organization = OrganizationClient(client_wrapper=self._client_wrapper)
        self.bank_lookup = BankLookupClient(client_wrapper=self._client_wrapper)
        self.calculate = CalculateClient(client_wrapper=self._client_wrapper)
        self.custom_payment_method_schema = CustomPaymentMethodSchemaClient(client_wrapper=self._client_wrapper)
        self.ocr = OcrClient(client_wrapper=self._client_wrapper)
        self.payment_methods = PaymentMethodsClient(client_wrapper=self._client_wrapper)


class AsyncMercoa:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : MercoaEnvironment
        The environment to use for requests from the client. from .environment import MercoaEnvironment



        Defaults to MercoaEnvironment.PRODUCTION



    token : typing.Union[str, typing.Callable[[], str]]
    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.AsyncClient]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    Examples
    --------
    from mercoa import AsyncMercoa

    client = AsyncMercoa(
        token="YOUR_TOKEN",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: MercoaEnvironment = MercoaEnvironment.PRODUCTION,
        token: typing.Union[str, typing.Callable[[], str]],
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            token=token,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self.entity_group = AsyncEntityGroupClient(client_wrapper=self._client_wrapper)
        self.entity = AsyncEntityClient(client_wrapper=self._client_wrapper)
        self.invoice_template = AsyncInvoiceTemplateClient(client_wrapper=self._client_wrapper)
        self.invoice = AsyncInvoiceClient(client_wrapper=self._client_wrapper)
        self.organization = AsyncOrganizationClient(client_wrapper=self._client_wrapper)
        self.bank_lookup = AsyncBankLookupClient(client_wrapper=self._client_wrapper)
        self.calculate = AsyncCalculateClient(client_wrapper=self._client_wrapper)
        self.custom_payment_method_schema = AsyncCustomPaymentMethodSchemaClient(client_wrapper=self._client_wrapper)
        self.ocr = AsyncOcrClient(client_wrapper=self._client_wrapper)
        self.payment_methods = AsyncPaymentMethodsClient(client_wrapper=self._client_wrapper)


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: MercoaEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
