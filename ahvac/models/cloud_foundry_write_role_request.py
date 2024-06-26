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

class CloudFoundryWriteRoleRequest(BaseModel):
    """
    CloudFoundryWriteRoleRequest
    """ # noqa: E501
    bound_application_ids: Optional[List[StrictStr]] = Field(default=None, description="Require that the client certificate presented has at least one of these app IDs.")
    bound_cidrs: Optional[List[StrictStr]] = Field(default=None, description="Use \"token_bound_cidrs\" instead. If this and \"token_bound_cidrs\" are both specified, only \"token_bound_cidrs\" will be used.")
    bound_instance_ids: Optional[List[StrictStr]] = Field(default=None, description="Require that the client certificate presented has at least one of these instance IDs.")
    bound_organization_ids: Optional[List[StrictStr]] = Field(default=None, description="Require that the client certificate presented has at least one of these org IDs.")
    bound_space_ids: Optional[List[StrictStr]] = Field(default=None, description="Require that the client certificate presented has at least one of these space IDs.")
    disable_ip_matching: Optional[StrictBool] = Field(default=False, description="If set to true, disables the default behavior that logging in must be performed from an acceptable IP address described by the certificate presented.")
    max_ttl: Optional[StrictStr] = Field(default=None, description="Use \"token_max_ttl\" instead. If this and \"token_max_ttl\" are both specified, only \"token_max_ttl\" will be used.")
    period: Optional[StrictStr] = Field(default=None, description="Use \"token_period\" instead. If this and \"token_period\" are both specified, only \"token_period\" will be used.")
    policies: Optional[List[StrictStr]] = Field(default=None, description="Use \"token_policies\" instead. If this and \"token_policies\" are both specified, only \"token_policies\" will be used.")
    token_bound_cidrs: Optional[List[StrictStr]] = Field(default=None, description="Comma separated string or JSON list of CIDR blocks. If set, specifies the blocks of IP addresses which are allowed to use the generated token.")
    token_explicit_max_ttl: Optional[StrictStr] = Field(default=None, description="If set, tokens created via this role carry an explicit maximum TTL. During renewal, the current maximum TTL values of the role and the mount are not checked for changes, and any updates to these values will have no effect on the token being renewed.")
    token_max_ttl: Optional[StrictStr] = Field(default=None, description="The maximum lifetime of the generated token")
    token_no_default_policy: Optional[StrictBool] = Field(default=None, description="If true, the 'default' policy will not automatically be added to generated tokens")
    token_num_uses: Optional[StrictInt] = Field(default=None, description="The maximum number of times a token may be used, a value of zero means unlimited")
    token_period: Optional[StrictStr] = Field(default=None, description="If set, tokens created via this role will have no max lifetime; instead, their renewal period will be fixed to this value. This takes an integer number of seconds, or a string duration (e.g. \"24h\").")
    token_policies: Optional[List[StrictStr]] = Field(default=None, description="Comma-separated list of policies")
    token_ttl: Optional[StrictStr] = Field(default=None, description="The initial ttl of the token to generate")
    token_type: Optional[StrictStr] = Field(default='default-service', description="The type of token to generate, service or batch")
    ttl: Optional[StrictStr] = Field(default=None, description="Use \"token_ttl\" instead. If this and \"token_ttl\" are both specified, only \"token_ttl\" will be used.")
    __properties: ClassVar[List[str]] = ["bound_application_ids", "bound_cidrs", "bound_instance_ids", "bound_organization_ids", "bound_space_ids", "disable_ip_matching", "max_ttl", "period", "policies", "token_bound_cidrs", "token_explicit_max_ttl", "token_max_ttl", "token_no_default_policy", "token_num_uses", "token_period", "token_policies", "token_ttl", "token_type", "ttl"]

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
        """Create an instance of CloudFoundryWriteRoleRequest from a JSON string"""
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
        """Create an instance of CloudFoundryWriteRoleRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "bound_application_ids": obj.get("bound_application_ids"),
            "bound_cidrs": obj.get("bound_cidrs"),
            "bound_instance_ids": obj.get("bound_instance_ids"),
            "bound_organization_ids": obj.get("bound_organization_ids"),
            "bound_space_ids": obj.get("bound_space_ids"),
            "disable_ip_matching": obj.get("disable_ip_matching") if obj.get("disable_ip_matching") is not None else False,
            "max_ttl": obj.get("max_ttl"),
            "period": obj.get("period"),
            "policies": obj.get("policies"),
            "token_bound_cidrs": obj.get("token_bound_cidrs"),
            "token_explicit_max_ttl": obj.get("token_explicit_max_ttl"),
            "token_max_ttl": obj.get("token_max_ttl"),
            "token_no_default_policy": obj.get("token_no_default_policy"),
            "token_num_uses": obj.get("token_num_uses"),
            "token_period": obj.get("token_period"),
            "token_policies": obj.get("token_policies"),
            "token_ttl": obj.get("token_ttl"),
            "token_type": obj.get("token_type") if obj.get("token_type") is not None else 'default-service',
            "ttl": obj.get("ttl")
        })
        return _obj


