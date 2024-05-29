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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class PkiConfigureCrlResponse(BaseModel):
    """
    PkiConfigureCrlResponse
    """ # noqa: E501
    auto_rebuild: Optional[StrictBool] = Field(default=None, description="If set to true, enables automatic rebuilding of the CRL")
    auto_rebuild_grace_period: Optional[StrictStr] = Field(default='12h', description="The time before the CRL expires to automatically rebuild it, when enabled. Must be shorter than the CRL expiry. Defaults to 12h.")
    cross_cluster_revocation: Optional[StrictBool] = Field(default=None, description="Whether to enable a global, cross-cluster revocation queue. Must be used with auto_rebuild=true.")
    delta_rebuild_interval: Optional[StrictStr] = Field(default='15m', description="The time between delta CRL rebuilds if a new revocation has occurred. Must be shorter than the CRL expiry. Defaults to 15m.")
    disable: Optional[StrictBool] = Field(default=None, description="If set to true, disables generating the CRL entirely.")
    enable_delta: Optional[StrictBool] = Field(default=None, description="Whether to enable delta CRLs between authoritative CRL rebuilds")
    expiry: Optional[StrictStr] = Field(default='72h', description="The amount of time the generated CRL should be valid; defaults to 72 hours")
    ocsp_disable: Optional[StrictBool] = Field(default=None, description="If set to true, ocsp unauthorized responses will be returned.")
    ocsp_expiry: Optional[StrictStr] = Field(default='1h', description="The amount of time an OCSP response will be valid (controls the NextUpdate field); defaults to 12 hours")
    unified_crl: Optional[StrictBool] = Field(default=None, description="If set to true enables global replication of revocation entries, also enabling unified versions of OCSP and CRLs if their respective features are enabled. disable for CRLs and ocsp_disable for OCSP.")
    unified_crl_on_existing_paths: Optional[StrictBool] = Field(default=None, description="If set to true, existing CRL and OCSP paths will return the unified CRL instead of a response based on cluster-local data")
    __properties: ClassVar[List[str]] = ["auto_rebuild", "auto_rebuild_grace_period", "cross_cluster_revocation", "delta_rebuild_interval", "disable", "enable_delta", "expiry", "ocsp_disable", "ocsp_expiry", "unified_crl", "unified_crl_on_existing_paths"]

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
        """Create an instance of PkiConfigureCrlResponse from a JSON string"""
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
        """Create an instance of PkiConfigureCrlResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "auto_rebuild": obj.get("auto_rebuild"),
            "auto_rebuild_grace_period": obj.get("auto_rebuild_grace_period") if obj.get("auto_rebuild_grace_period") is not None else '12h',
            "cross_cluster_revocation": obj.get("cross_cluster_revocation"),
            "delta_rebuild_interval": obj.get("delta_rebuild_interval") if obj.get("delta_rebuild_interval") is not None else '15m',
            "disable": obj.get("disable"),
            "enable_delta": obj.get("enable_delta"),
            "expiry": obj.get("expiry") if obj.get("expiry") is not None else '72h',
            "ocsp_disable": obj.get("ocsp_disable"),
            "ocsp_expiry": obj.get("ocsp_expiry") if obj.get("ocsp_expiry") is not None else '1h',
            "unified_crl": obj.get("unified_crl"),
            "unified_crl_on_existing_paths": obj.get("unified_crl_on_existing_paths")
        })
        return _obj


