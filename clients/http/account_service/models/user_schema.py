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

class UserSchema(BaseModel):
    """
    UserSchema
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="User real name")
    location: Optional[StrictStr] = Field(default=None, description="User real location")
    icq: Optional[StrictStr] = Field(default=None, description="User ICQ")
    skype: Optional[StrictStr] = Field(default=None, description="User Skype")
    info: Optional[StrictStr] = Field(default=None, description="User info")
    profile_picture_url: Optional[StrictStr] = Field(default=None, description="Profile picture URL")
    medium_profile_picture_url: Optional[StrictStr] = Field(default=None, description="Medium profile picture URL")
    small_profile_picture_url: Optional[StrictStr] = Field(default=None, description="Small profile picture URL")
    __properties: ClassVar[List[str]] = ["name", "location", "icq", "skype", "info", "profile_picture_url", "medium_profile_picture_url", "small_profile_picture_url"]

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
        """Create an instance of UserSchema from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UserSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "location": obj.get("location"),
            "icq": obj.get("icq"),
            "skype": obj.get("skype"),
            "info": obj.get("info"),
            "profile_picture_url": obj.get("profile_picture_url"),
            "medium_profile_picture_url": obj.get("medium_profile_picture_url"),
            "small_profile_picture_url": obj.get("small_profile_picture_url")
        })
        return _obj
