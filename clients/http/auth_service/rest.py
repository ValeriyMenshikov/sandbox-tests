# coding: utf-8

"""
    Auth API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import asyncio
import io
import json
import re
import ssl
from typing import Optional, Union

import aiohttp
import aiohttp_retry
import structlog

from clients.http.auth_service.exceptions import ApiException, ApiValueError

RESTResponseType = aiohttp.ClientResponse

ALLOW_RETRY_METHODS = frozenset({'DELETE', 'GET', 'HEAD', 'OPTIONS', 'PUT', 'TRACE'})

class RESTResponse(io.IOBase):

    def __init__(self, resp) -> None:
        self.response = resp
        self.status = resp.status
        self.reason = resp.reason
        self.data = None

    async def read(self):
        if self.data is None:
            self.data = await self.response.read()
        return self.data

    def getheaders(self):
        """Returns a CIMultiDictProxy of the response headers."""
        return self.response.headers

    def getheader(self, name, default=None):
        """Returns a given response header."""
        return self.response.headers.get(name, default)


class RESTClientObject:

    def __init__(self, configuration) -> None:

        # maxsize is number of requests to host that are allowed in parallel
        maxsize = configuration.connection_pool_maxsize

        ssl_context = ssl.create_default_context(
            cafile=configuration.ssl_ca_cert
        )
        if configuration.cert_file:
            ssl_context.load_cert_chain(
                configuration.cert_file, keyfile=configuration.key_file
            )

        if not configuration.verify_ssl:
            ssl_context.check_hostname = False
            ssl_context.verify_mode = ssl.CERT_NONE

        connector = aiohttp.TCPConnector(
            limit=maxsize,
            ssl=ssl_context
        )

        self.proxy = configuration.proxy
        self.proxy_headers = configuration.proxy_headers

        # https pool manager
        self.pool_manager = aiohttp.ClientSession(
            connector=connector,
            trust_env=True
        )

        retries = configuration.retries
        self.retry_client: Optional[aiohttp_retry.RetryClient]
        if retries is not None:
            self.retry_client = aiohttp_retry.RetryClient(
                client_session=self.pool_manager,
                retry_options=aiohttp_retry.ExponentialRetry(
                    attempts=retries,
                    factor=2.0,
                    start_timeout=0.1,
                    max_timeout=120.0
                )
            )
        else:
            self.retry_client = None

    async def close(self):
        await self.pool_manager.close()
        if self.retry_client is not None:
            await self.retry_client.close()

    async def request(
        self,
        method,
        url,
        headers=None,
        body=None,
        post_params=None,
        _request_timeout=None
    ):
        """Execute request

        :param method: http request method
        :param url: http request url
        :param headers: http request headers
        :param body: request json body, for `application/json`
        :param post_params: request post parameters,
                            `application/x-www-form-urlencoded`
                            and `multipart/form-data`
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        """
        method = method.upper()
        assert method in [
            'GET',
            'HEAD',
            'DELETE',
            'POST',
            'PUT',
            'PATCH',
            'OPTIONS'
        ]

        if post_params and body:
            raise ApiValueError(
                "body parameter cannot be used with post_params parameter."
            )

        post_params = post_params or {}
        headers = headers or {}
        # url already contains the URL query string
        timeout = _request_timeout or 5 * 60

        if 'Content-Type' not in headers:
            headers['Content-Type'] = 'application/json'

        args = {
            "method": method,
            "url": url,
            "timeout": timeout,
            "headers": headers
        }

        if self.proxy:
            args["proxy"] = self.proxy
        if self.proxy_headers:
            args["proxy_headers"] = self.proxy_headers

        # For `POST`, `PUT`, `PATCH`, `OPTIONS`, `DELETE`
        if method in ['POST', 'PUT', 'PATCH', 'OPTIONS', 'DELETE']:
            if re.search('json', headers['Content-Type'], re.IGNORECASE):
                if body is not None:
                    body = json.dumps(body)
                args["data"] = body
            elif headers['Content-Type'] == 'application/x-www-form-urlencoded':
                args["data"] = aiohttp.FormData(post_params)
            elif headers['Content-Type'] == 'multipart/form-data':
                # must del headers['Content-Type'], or the correct
                # Content-Type which generated by aiohttp
                del headers['Content-Type']
                data = aiohttp.FormData()
                for param in post_params:
                    k, v = param
                    if isinstance(v, tuple) and len(v) == 3:
                        data.add_field(
                            k,
                            value=v[1],
                            filename=v[0],
                            content_type=v[2]
                        )
                    else:
                        # Ensures that dict objects are serialized
                        if isinstance(v, dict):
                            v = json.dumps(v)
                        elif isinstance(v, int):
                            v = str(v)
                        data.add_field(k, v)
                args["data"] = data

            # Pass a `bytes` or `str` parameter directly in the body to support
            # other content types than Json when `body` argument is provided
            # in serialized form
            elif isinstance(body, str) or isinstance(body, bytes):
                args["data"] = body
            else:
                # Cannot generate the request from given parameters
                msg = """Cannot prepare a request message for provided
                         arguments. Please check that your arguments match
                         declared content type."""
                raise ApiException(status=0, reason=msg)

        pool_manager: Union[aiohttp.ClientSession, aiohttp_retry.RetryClient]
        if self.retry_client is not None and method in ALLOW_RETRY_METHODS:
            pool_manager = self.retry_client
        else:
            pool_manager = self.pool_manager

        return await self._logged_request(pool_manager, **args)

    async def _logged_request(self, pool_manager, **args) -> RESTResponse:
        log = structlog.get_logger().bind(service="api")
        json_data = args.get("data")
        log.msg(
            "request",
            url=args.get("url", None),
            method=args.get("method"),
            json=json.loads(json_data) if isinstance(json_data, str) else {},
            headers=args.get("headers", {}),
        )
        try:
            r = await pool_manager.request(**args)
        except RuntimeError as e:
            if 'Event loop is closed' in e.args[0]:
                asyncio.run(self.pool_manager.__aexit__(None, None, None))
        else:
            log_response = r.__dict__
            data = await r.read()
            log.msg(
                "response",
                method=args.get("url", None),
                url=log_response.get("_url", None),
                json=json.loads(data) if isinstance(data, bytes) and data else "{}",
                headers=dict(log_response.get("_headers", {})),
                status_code=log_response.get("status", None),
            )
            return RESTResponse(r)
