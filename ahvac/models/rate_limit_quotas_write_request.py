# coding: utf-8

"""
    HashiCorp Vault API

    HTTP API that gives you full access to Vault. All API routes are prefixed with `/v1/`.

    The version of the OpenAPI document: 1.15.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class RateLimitQuotasWriteRequest(BaseModel):
    """
    RateLimitQuotasWriteRequest
    """ # noqa: E501
    block_interval: Optional[StrictStr] = Field(default=None, description="If set, when a client reaches a rate limit threshold, the client will be prohibited from any further requests until after the 'block_interval' has elapsed.")
    inheritable: Optional[StrictBool] = Field(default=None, description="Whether all child namespaces can inherit this namespace quota.")
    interval: Optional[StrictStr] = Field(default=None, description="The duration to enforce rate limiting for (default '1s').")
    path: Optional[StrictStr] = Field(default=None, description="Path of the mount or namespace to apply the quota. A blank path configures a global quota. For example namespace1/ adds a quota to a full namespace, namespace1/auth/userpass adds a quota to userpass in namespace1.")
    rate: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The maximum number of requests in a given interval to be allowed by the quota rule. The 'rate' must be positive.")
    role: Optional[StrictStr] = Field(default=None, description="Login role to apply this quota to. Note that when set, path must be configured to a valid auth method with a concept of roles.")
    type: Optional[StrictStr] = Field(default=None, description="Type of the quota rule.")
    __properties: ClassVar[List[str]] = ["block_interval", "inheritable", "interval", "path", "rate", "role", "type"]

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
        """Create an instance of RateLimitQuotasWriteRequest from a JSON string"""
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
        """Create an instance of RateLimitQuotasWriteRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "block_interval": obj.get("block_interval"),
            "inheritable": obj.get("inheritable"),
            "interval": obj.get("interval"),
            "path": obj.get("path"),
            "rate": obj.get("rate"),
            "role": obj.get("role"),
            "type": obj.get("type")
        })
        return _obj


