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

class PkiIssuersGenerateRootResponse(BaseModel):
    """
    PkiIssuersGenerateRootResponse
    """ # noqa: E501
    certificate: Optional[StrictStr] = Field(default=None, description="The generated self-signed CA certificate.")
    expiration: Optional[StrictInt] = Field(default=None, description="The expiration of the given issuer.")
    issuer_id: Optional[StrictStr] = Field(default=None, description="The ID of the issuer")
    issuer_name: Optional[StrictStr] = Field(default=None, description="The name of the issuer.")
    issuing_ca: Optional[StrictStr] = Field(default=None, description="The issuing certificate authority.")
    key_id: Optional[StrictStr] = Field(default=None, description="The ID of the key.")
    key_name: Optional[StrictStr] = Field(default=None, description="The key name if given.")
    private_key: Optional[StrictStr] = Field(default=None, description="The private key if exported was specified.")
    serial_number: Optional[StrictStr] = Field(default=None, description="The requested Subject's named serial number.")
    __properties: ClassVar[List[str]] = ["certificate", "expiration", "issuer_id", "issuer_name", "issuing_ca", "key_id", "key_name", "private_key", "serial_number"]

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
        """Create an instance of PkiIssuersGenerateRootResponse from a JSON string"""
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
        """Create an instance of PkiIssuersGenerateRootResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "certificate": obj.get("certificate"),
            "expiration": obj.get("expiration"),
            "issuer_id": obj.get("issuer_id"),
            "issuer_name": obj.get("issuer_name"),
            "issuing_ca": obj.get("issuing_ca"),
            "key_id": obj.get("key_id"),
            "key_name": obj.get("key_name"),
            "private_key": obj.get("private_key"),
            "serial_number": obj.get("serial_number")
        })
        return _obj


