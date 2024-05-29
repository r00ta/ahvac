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

class PkiIssuersImportBundleResponse(BaseModel):
    """
    PkiIssuersImportBundleResponse
    """ # noqa: E501
    existing_issuers: Optional[List[StrictStr]] = Field(default=None, description="Existing issuers specified as part of the import bundle of this request")
    existing_keys: Optional[List[StrictStr]] = Field(default=None, description="Existing keys specified as part of the import bundle of this request")
    imported_issuers: Optional[List[StrictStr]] = Field(default=None, description="Net-new issuers imported as a part of this request")
    imported_keys: Optional[List[StrictStr]] = Field(default=None, description="Net-new keys imported as a part of this request")
    mapping: Optional[Dict[str, Any]] = Field(default=None, description="A mapping of issuer_id to key_id for all issuers included in this request")
    __properties: ClassVar[List[str]] = ["existing_issuers", "existing_keys", "imported_issuers", "imported_keys", "mapping"]

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
        """Create an instance of PkiIssuersImportBundleResponse from a JSON string"""
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
        """Create an instance of PkiIssuersImportBundleResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "existing_issuers": obj.get("existing_issuers"),
            "existing_keys": obj.get("existing_keys"),
            "imported_issuers": obj.get("imported_issuers"),
            "imported_keys": obj.get("imported_keys"),
            "mapping": obj.get("mapping")
        })
        return _obj


