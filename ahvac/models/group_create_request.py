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

class GroupCreateRequest(BaseModel):
    """
    GroupCreateRequest
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="ID of the group. If set, updates the corresponding existing group.")
    member_entity_ids: Optional[List[StrictStr]] = Field(default=None, description="Entity IDs to be assigned as group members.")
    member_group_ids: Optional[List[StrictStr]] = Field(default=None, description="Group IDs to be assigned as group members.")
    metadata: Optional[Dict[str, Any]] = Field(default=None, description="Metadata to be associated with the group. In CLI, this parameter can be repeated multiple times, and it all gets merged together. For example: vault <command> <path> metadata=key1=value1 metadata=key2=value2")
    name: Optional[StrictStr] = Field(default=None, description="Name of the group.")
    policies: Optional[List[StrictStr]] = Field(default=None, description="Policies to be tied to the group.")
    type: Optional[StrictStr] = Field(default=None, description="Type of the group, 'internal' or 'external'. Defaults to 'internal'")
    __properties: ClassVar[List[str]] = ["id", "member_entity_ids", "member_group_ids", "metadata", "name", "policies", "type"]

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
        """Create an instance of GroupCreateRequest from a JSON string"""
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
        """Create an instance of GroupCreateRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "member_entity_ids": obj.get("member_entity_ids"),
            "member_group_ids": obj.get("member_group_ids"),
            "metadata": obj.get("metadata"),
            "name": obj.get("name"),
            "policies": obj.get("policies"),
            "type": obj.get("type")
        })
        return _obj


