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

class TokenCreateRequest(BaseModel):
    """
    TokenCreateRequest
    """ # noqa: E501
    display_name: Optional[StrictStr] = Field(default=None, description="Name to associate with this token")
    entity_alias: Optional[StrictStr] = Field(default=None, description="Name of the entity alias to associate with this token")
    explicit_max_ttl: Optional[StrictStr] = Field(default=None, description="Explicit Max TTL of this token")
    id: Optional[StrictStr] = Field(default=None, description="Value for the token")
    lease: Optional[StrictStr] = Field(default=None, description="Use 'ttl' instead")
    meta: Optional[Dict[str, Any]] = Field(default=None, description="Arbitrary key=value metadata to associate with the token")
    no_default_policy: Optional[StrictBool] = Field(default=None, description="Do not include default policy for this token")
    no_parent: Optional[StrictBool] = Field(default=None, description="Create the token with no parent")
    num_uses: Optional[StrictInt] = Field(default=None, description="Max number of uses for this token")
    period: Optional[StrictStr] = Field(default=None, description="Renew period")
    policies: Optional[List[StrictStr]] = Field(default=None, description="List of policies for the token")
    renewable: Optional[StrictBool] = Field(default=True, description="Allow token to be renewed past its initial TTL up to system/mount maximum TTL")
    ttl: Optional[StrictStr] = Field(default=None, description="Time to live for this token")
    type: Optional[StrictStr] = Field(default=None, description="Token type")
    __properties: ClassVar[List[str]] = ["display_name", "entity_alias", "explicit_max_ttl", "id", "lease", "meta", "no_default_policy", "no_parent", "num_uses", "period", "policies", "renewable", "ttl", "type"]

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
        """Create an instance of TokenCreateRequest from a JSON string"""
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
        """Create an instance of TokenCreateRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "display_name": obj.get("display_name"),
            "entity_alias": obj.get("entity_alias"),
            "explicit_max_ttl": obj.get("explicit_max_ttl"),
            "id": obj.get("id"),
            "lease": obj.get("lease"),
            "meta": obj.get("meta"),
            "no_default_policy": obj.get("no_default_policy"),
            "no_parent": obj.get("no_parent"),
            "num_uses": obj.get("num_uses"),
            "period": obj.get("period"),
            "policies": obj.get("policies"),
            "renewable": obj.get("renewable") if obj.get("renewable") is not None else True,
            "ttl": obj.get("ttl"),
            "type": obj.get("type")
        })
        return _obj


