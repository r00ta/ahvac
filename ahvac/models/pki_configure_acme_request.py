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

class PkiConfigureAcmeRequest(BaseModel):
    """
    PkiConfigureAcmeRequest
    """ # noqa: E501
    allow_role_ext_key_usage: Optional[StrictBool] = Field(default=False, description="whether the ExtKeyUsage field from a role is used, defaults to false meaning that certificate will be signed with ServerAuth.")
    allowed_issuers: Optional[List[StrictStr]] = Field(default=None, description="which issuers are allowed for use with ACME; by default, this will only be the primary (default) issuer")
    allowed_roles: Optional[List[StrictStr]] = Field(default=None, description="which roles are allowed for use with ACME; by default via '*', these will be all roles including sign-verbatim; when concrete role names are specified, any default_directory_policy role must be included to allow usage of the default acme directories under /pki/acme/directory and /pki/issuer/:issuer_id/acme/directory.")
    default_directory_policy: Optional[StrictStr] = Field(default='sign-verbatim', description="the policy to be used for non-role-qualified ACME requests; by default ACME issuance will be otherwise unrestricted, equivalent to the sign-verbatim endpoint; one may also specify a role to use as this policy, as \"role:<role_name>\", the specified role must be allowed by allowed_roles")
    dns_resolver: Optional[StrictStr] = Field(default='', description="DNS resolver to use for domain resolution on this mount. Defaults to using the default system resolver. Must be in the format <host>:<port>, with both parts mandatory.")
    eab_policy: Optional[StrictStr] = Field(default='always-required', description="Specify the policy to use for external account binding behaviour, 'not-required', 'new-account-required' or 'always-required'")
    enabled: Optional[StrictBool] = Field(default=False, description="whether ACME is enabled, defaults to false meaning that clusters will by default not get ACME support")
    __properties: ClassVar[List[str]] = ["allow_role_ext_key_usage", "allowed_issuers", "allowed_roles", "default_directory_policy", "dns_resolver", "eab_policy", "enabled"]

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
        """Create an instance of PkiConfigureAcmeRequest from a JSON string"""
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
        """Create an instance of PkiConfigureAcmeRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "allow_role_ext_key_usage": obj.get("allow_role_ext_key_usage") if obj.get("allow_role_ext_key_usage") is not None else False,
            "allowed_issuers": obj.get("allowed_issuers"),
            "allowed_roles": obj.get("allowed_roles"),
            "default_directory_policy": obj.get("default_directory_policy") if obj.get("default_directory_policy") is not None else 'sign-verbatim',
            "dns_resolver": obj.get("dns_resolver") if obj.get("dns_resolver") is not None else '',
            "eab_policy": obj.get("eab_policy") if obj.get("eab_policy") is not None else 'always-required',
            "enabled": obj.get("enabled") if obj.get("enabled") is not None else False
        })
        return _obj

