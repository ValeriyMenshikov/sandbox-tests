# coding: utf-8

"""
    Account API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ChangePassword(BaseModel):
    """
    ChangePassword
    """ # noqa: E501
    login: Optional[StrictStr] = None
    token: Optional[StrictStr] = None
    old_password: Optional[StrictStr] = Field(default=None, alias="oldPassword")
    new_password: Optional[StrictStr] = Field(default=None, alias="newPassword")
    __properties: ClassVar[List[str]] = ["login", "token", "oldPassword", "newPassword"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ChangePassword from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if login (nullable) is None
        # and model_fields_set contains the field
        if self.login is None and "login" in self.model_fields_set:
            _dict['login'] = None

        # set to None if token (nullable) is None
        # and model_fields_set contains the field
        if self.token is None and "token" in self.model_fields_set:
            _dict['token'] = None

        # set to None if old_password (nullable) is None
        # and model_fields_set contains the field
        if self.old_password is None and "old_password" in self.model_fields_set:
            _dict['oldPassword'] = None

        # set to None if new_password (nullable) is None
        # and model_fields_set contains the field
        if self.new_password is None and "new_password" in self.model_fields_set:
            _dict['newPassword'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ChangePassword from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "login": obj.get("login"),
            "token": obj.get("token"),
            "oldPassword": obj.get("oldPassword"),
            "newPassword": obj.get("newPassword")
        })
        return _obj
