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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class EntityUpdateAliasByIdRequest(BaseModel):
    """
    EntityUpdateAliasByIdRequest
    """ # noqa: E501
    canonical_id: Optional[StrictStr] = Field(default=None, description="Entity ID to which this alias should be tied to")
    custom_metadata: Optional[Dict[str, Any]] = Field(default=None, description="User provided key-value pairs")
    entity_id: Optional[StrictStr] = Field(default=None, description="Entity ID to which this alias belongs to. This field is deprecated, use canonical_id.")
    mount_accessor: Optional[StrictStr] = Field(default=None, description="(Unused)")
    name: Optional[StrictStr] = Field(default=None, description="(Unused)")
    __properties: ClassVar[List[str]] = ["canonical_id", "custom_metadata", "entity_id", "mount_accessor", "name"]

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
        """Create an instance of EntityUpdateAliasByIdRequest from a JSON string"""
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
        """Create an instance of EntityUpdateAliasByIdRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "canonical_id": obj.get("canonical_id"),
            "custom_metadata": obj.get("custom_metadata"),
            "entity_id": obj.get("entity_id"),
            "mount_accessor": obj.get("mount_accessor"),
            "name": obj.get("name")
        })
        return _obj


