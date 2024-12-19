# coding: utf-8

"""
    Register API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
import allure
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import StrictStr
from typing import Any
from clients.http.register_service.models.registration import Registration
from clients.http.register_service.models.user_envelope import UserEnvelope

from clients.http.register_service.api_client import ApiClient, RequestSerialized
from clients.http.register_service.api_response import ApiResponse
from clients.http.register_service.rest import RESTResponseType


class AccountApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    async def activate_user_activate_put(
        self,
        token: StrictStr,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> UserEnvelope:
        """Подтвердить регистрацию

        Метод для подтверждения регистрации пользователя с помощью токена из письма.

        :param token: (required)
        :type token: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._activate_user_activate_put_serialize(
            token=token,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "UserEnvelope",
            '422': "HTTPValidationError",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    async def activate_user_activate_put_with_http_info(
        self,
        token: StrictStr,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[UserEnvelope]:
        """Подтвердить регистрацию

        Метод для подтверждения регистрации пользователя с помощью токена из письма.

        :param token: (required)
        :type token: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._activate_user_activate_put_serialize(
            token=token,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "UserEnvelope",
            '422': "HTTPValidationError",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    async def activate_user_activate_put_without_preload_content(
        self,
        token: StrictStr,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Подтвердить регистрацию

        Метод для подтверждения регистрации пользователя с помощью токена из письма.

        :param token: (required)
        :type token: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._activate_user_activate_put_serialize(
            token=token,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "UserEnvelope",
            '422': "HTTPValidationError",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _activate_user_activate_put_serialize(
        self,
        token,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        with allure.step("PUT /user/activate"):
            _host = None

            _collection_formats: Dict[str, str] = {
            }

            _path_params: Dict[str, str] = {}
            _query_params: List[Tuple[str, str]] = []
            _header_params: Dict[str, Optional[str]] = _headers or {}
            _form_params: List[Tuple[str, str]] = []
            _files: Dict[
                str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
            ] = {}
            _body_params: Optional[bytes] = None

            # process the path parameters
            # process the query parameters
            if token is not None:

                _query_params.append(('token', token))

            # process the header parameters
            # process the form parameters
            # process the body parameter


            # set the HTTP header `Accept`
            if 'Accept' not in _header_params:
                _header_params['Accept'] = self.api_client.select_header_accept(
                    [
                        'application/json'
                    ]
                )


            # authentication setting
            _auth_settings: List[str] = [
            ]

            return self.api_client.param_serialize(
                method='PUT',
                resource_path='/user/activate',
                path_params=_path_params,
                query_params=_query_params,
                header_params=_header_params,
                body=_body_params,
                post_params=_form_params,
                files=_files,
                auth_settings=_auth_settings,
                collection_formats=_collection_formats,
                _host=_host,
                _request_auth=_request_auth
            )




    @validate_call
    async def register_user_register_post(
        self,
        registration: Registration,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> object:
        """Регистрация пользователя

        Метод для регистрации пользователя,     после успешного выполнения на почтовый сервер будет отправлено письмо для подтверждения регистрации,     с помощью токена необходимо подтвердить регистрацию в методе activate

        :param registration: (required)
        :type registration: Registration
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._register_user_register_post_serialize(
            registration=registration,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "object",
            '422': "HTTPValidationError",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    async def register_user_register_post_with_http_info(
        self,
        registration: Registration,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[object]:
        """Регистрация пользователя

        Метод для регистрации пользователя,     после успешного выполнения на почтовый сервер будет отправлено письмо для подтверждения регистрации,     с помощью токена необходимо подтвердить регистрацию в методе activate

        :param registration: (required)
        :type registration: Registration
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._register_user_register_post_serialize(
            registration=registration,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "object",
            '422': "HTTPValidationError",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    async def register_user_register_post_without_preload_content(
        self,
        registration: Registration,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Регистрация пользователя

        Метод для регистрации пользователя,     после успешного выполнения на почтовый сервер будет отправлено письмо для подтверждения регистрации,     с помощью токена необходимо подтвердить регистрацию в методе activate

        :param registration: (required)
        :type registration: Registration
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._register_user_register_post_serialize(
            registration=registration,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "object",
            '422': "HTTPValidationError",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _register_user_register_post_serialize(
        self,
        registration,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        with allure.step("POST /user/register"):
            _host = None

            _collection_formats: Dict[str, str] = {
            }

            _path_params: Dict[str, str] = {}
            _query_params: List[Tuple[str, str]] = []
            _header_params: Dict[str, Optional[str]] = _headers or {}
            _form_params: List[Tuple[str, str]] = []
            _files: Dict[
                str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
            ] = {}
            _body_params: Optional[bytes] = None

            # process the path parameters
            # process the query parameters
            # process the header parameters
            # process the form parameters
            # process the body parameter
            if registration is not None:
                _body_params = registration


            # set the HTTP header `Accept`
            if 'Accept' not in _header_params:
                _header_params['Accept'] = self.api_client.select_header_accept(
                    [
                        'application/json'
                    ]
                )

            # set the HTTP header `Content-Type`
            if _content_type:
                _header_params['Content-Type'] = _content_type
            else:
                _default_content_type = (
                    self.api_client.select_header_content_type(
                        [
                            'application/json'
                        ]
                    )
                )
                if _default_content_type is not None:
                    _header_params['Content-Type'] = _default_content_type

            # authentication setting
            _auth_settings: List[str] = [
            ]

            return self.api_client.param_serialize(
                method='POST',
                resource_path='/user/register',
                path_params=_path_params,
                query_params=_query_params,
                header_params=_header_params,
                body=_body_params,
                post_params=_form_params,
                files=_files,
                auth_settings=_auth_settings,
                collection_formats=_collection_formats,
                _host=_host,
                _request_auth=_request_auth
            )
