# coding: utf-8

# flake8: noqa

"""
    Auth API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# import apis into sdk package
from clients.http.auth_service.api.auth_api import AuthApi

# import ApiClient
from clients.http.auth_service.api_response import ApiResponse
from clients.http.auth_service.api_client import ApiClient
from clients.http.auth_service.configuration import Configuration
from clients.http.auth_service.exceptions import OpenApiException
from clients.http.auth_service.exceptions import ApiTypeError
from clients.http.auth_service.exceptions import ApiValueError
from clients.http.auth_service.exceptions import ApiKeyError
from clients.http.auth_service.exceptions import ApiAttributeError
from clients.http.auth_service.exceptions import ApiException

# import models into sdk package
from clients.http.auth_service.models.http_validation_error import HTTPValidationError
from clients.http.auth_service.models.login_credentials import LoginCredentials
from clients.http.auth_service.models.rating import Rating
from clients.http.auth_service.models.user import User
from clients.http.auth_service.models.user_envelope import UserEnvelope
from clients.http.auth_service.models.user_role import UserRole
from clients.http.auth_service.models.validation_error import ValidationError
from clients.http.auth_service.models.validation_error_loc_inner import ValidationErrorLocInner
