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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class KvV2WriteMetadataRequest(BaseModel):
    """
    KvV2WriteMetadataRequest
    """ # noqa: E501
    cas_required: Optional[StrictBool] = Field(default=None, description="If true the key will require the cas parameter to be set on all write requests. If false, the backend’s configuration will be used.")
    custom_metadata: Optional[Dict[str, Any]] = Field(default=None, description="User-provided key-value pairs that are used to describe arbitrary and version-agnostic information about a secret.")
    delete_version_after: Optional[StrictStr] = Field(default=None, description="The length of time before a version is deleted. If not set, the backend's configured delete_version_after is used. Cannot be greater than the backend's delete_version_after. A zero duration clears the current setting. A negative duration will cause an error.")
    max_versions: Optional[StrictInt] = Field(default=None, description="The number of versions to keep. If not set, the backend’s configured max version is used.")
    __properties: ClassVar[List[str]] = ["cas_required", "custom_metadata", "delete_version_after", "max_versions"]

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
        """Create an instance of KvV2WriteMetadataRequest from a JSON string"""
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
        """Create an instance of KvV2WriteMetadataRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cas_required": obj.get("cas_required"),
            "custom_metadata": obj.get("custom_metadata"),
            "delete_version_after": obj.get("delete_version_after"),
            "max_versions": obj.get("max_versions")
        })
        return _obj


