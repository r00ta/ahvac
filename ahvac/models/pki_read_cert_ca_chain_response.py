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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class PkiReadCertCaChainResponse(BaseModel):
    """
    PkiReadCertCaChainResponse
    """ # noqa: E501
    ca_chain: Optional[StrictStr] = Field(default=None, description="Issuing CA Chain")
    certificate: Optional[StrictStr] = Field(default=None, description="Certificate")
    issuer_id: Optional[StrictStr] = Field(default=None, description="ID of the issuer")
    revocation_time: Optional[StrictInt] = Field(default=None, description="Revocation time")
    revocation_time_rfc3339: Optional[StrictStr] = Field(default=None, description="Revocation time RFC 3339 formatted")
    __properties: ClassVar[List[str]] = ["ca_chain", "certificate", "issuer_id", "revocation_time", "revocation_time_rfc3339"]

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
        """Create an instance of PkiReadCertCaChainResponse from a JSON string"""
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
        """Create an instance of PkiReadCertCaChainResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ca_chain": obj.get("ca_chain"),
            "certificate": obj.get("certificate"),
            "issuer_id": obj.get("issuer_id"),
            "revocation_time": obj.get("revocation_time"),
            "revocation_time_rfc3339": obj.get("revocation_time_rfc3339")
        })
        return _obj


