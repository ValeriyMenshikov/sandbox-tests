# coding: utf-8

# flake8: noqa

"""
    Mail API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# import apis into sdk package
from clients.http.mail_service.api.mail_api import MailApi

# import ApiClient
from clients.http.mail_service.api_response import ApiResponse
from clients.http.mail_service.api_client import ApiClient
from clients.http.mail_service.configuration import Configuration
from clients.http.mail_service.exceptions import OpenApiException
from clients.http.mail_service.exceptions import ApiTypeError
from clients.http.mail_service.exceptions import ApiValueError
from clients.http.mail_service.exceptions import ApiKeyError
from clients.http.mail_service.exceptions import ApiAttributeError
from clients.http.mail_service.exceptions import ApiException

# import models into sdk package
from clients.http.mail_service.models.content import Content
from clients.http.mail_service.models.http_validation_error import HTTPValidationError
from clients.http.mail_service.models.headers import Headers
from clients.http.mail_service.models.item import Item
from clients.http.mail_service.models.messages import Messages
from clients.http.mail_service.models.model_from import ModelFrom
from clients.http.mail_service.models.raw import Raw
from clients.http.mail_service.models.to_item import ToItem
from clients.http.mail_service.models.validation_error import ValidationError
from clients.http.mail_service.models.validation_error_loc_inner import ValidationErrorLocInner
