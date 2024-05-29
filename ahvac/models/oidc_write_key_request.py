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

class OidcWriteKeyRequest(BaseModel):
    """
    OidcWriteKeyRequest
    """ # noqa: E501
    algorithm: Optional[StrictStr] = Field(default='RS256', description="Signing algorithm to use. This will default to RS256.")
    allowed_client_ids: Optional[List[StrictStr]] = Field(default=None, description="Comma separated string or array of role client ids allowed to use this key for signing. If empty no roles are allowed. If \"*\" all roles are allowed.")
    rotation_period: Optional[StrictStr] = Field(default='24h', description="How often to generate a new keypair.")
    verification_ttl: Optional[StrictStr] = Field(default='24h', description="Controls how long the public portion of a key will be available for verification after being rotated.")
    __properties: ClassVar[List[str]] = ["algorithm", "allowed_client_ids", "rotation_period", "verification_ttl"]

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
        """Create an instance of OidcWriteKeyRequest from a JSON string"""
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
        """Create an instance of OidcWriteKeyRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "algorithm": obj.get("algorithm") if obj.get("algorithm") is not None else 'RS256',
            "allowed_client_ids": obj.get("allowed_client_ids"),
            "rotation_period": obj.get("rotation_period") if obj.get("rotation_period") is not None else '24h',
            "verification_ttl": obj.get("verification_ttl") if obj.get("verification_ttl") is not None else '24h'
        })
        return _obj


