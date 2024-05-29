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

class AppRoleWriteRoleRequest(BaseModel):
    """
    AppRoleWriteRoleRequest
    """ # noqa: E501
    bind_secret_id: Optional[StrictBool] = Field(default=True, description="Impose secret_id to be presented when logging in using this role. Defaults to 'true'.")
    bound_cidr_list: Optional[List[StrictStr]] = Field(default=None, description="Use \"secret_id_bound_cidrs\" instead.")
    local_secret_ids: Optional[StrictBool] = Field(default=None, description="If set, the secret IDs generated using this role will be cluster local. This can only be set during role creation and once set, it can't be reset later.")
    period: Optional[StrictStr] = Field(default=None, description="Use \"token_period\" instead. If this and \"token_period\" are both specified, only \"token_period\" will be used.")
    policies: Optional[List[StrictStr]] = Field(default=None, description="Use \"token_policies\" instead. If this and \"token_policies\" are both specified, only \"token_policies\" will be used.")
    role_id: Optional[StrictStr] = Field(default=None, description="Identifier of the role. Defaults to a UUID.")
    secret_id_bound_cidrs: Optional[List[StrictStr]] = Field(default=None, description="Comma separated string or list of CIDR blocks. If set, specifies the blocks of IP addresses which can perform the login operation.")
    secret_id_num_uses: Optional[StrictInt] = Field(default=None, description="Number of times a SecretID can access the role, after which the SecretID will expire. Defaults to 0 meaning that the the secret_id is of unlimited use.")
    secret_id_ttl: Optional[StrictStr] = Field(default=None, description="Duration in seconds after which the issued SecretID should expire. Defaults to 0, meaning no expiration.")
    token_bound_cidrs: Optional[List[StrictStr]] = Field(default=None, description="Comma separated string or JSON list of CIDR blocks. If set, specifies the blocks of IP addresses which are allowed to use the generated token.")
    token_explicit_max_ttl: Optional[StrictStr] = Field(default=None, description="If set, tokens created via this role carry an explicit maximum TTL. During renewal, the current maximum TTL values of the role and the mount are not checked for changes, and any updates to these values will have no effect on the token being renewed.")
    token_max_ttl: Optional[StrictStr] = Field(default=None, description="The maximum lifetime of the generated token")
    token_no_default_policy: Optional[StrictBool] = Field(default=None, description="If true, the 'default' policy will not automatically be added to generated tokens")
    token_num_uses: Optional[StrictInt] = Field(default=None, description="The maximum number of times a token may be used, a value of zero means unlimited")
    token_period: Optional[StrictStr] = Field(default=None, description="If set, tokens created via this role will have no max lifetime; instead, their renewal period will be fixed to this value. This takes an integer number of seconds, or a string duration (e.g. \"24h\").")
    token_policies: Optional[List[StrictStr]] = Field(default=None, description="Comma-separated list of policies")
    token_ttl: Optional[StrictStr] = Field(default=None, description="The initial ttl of the token to generate")
    token_type: Optional[StrictStr] = Field(default='default-service', description="The type of token to generate, service or batch")
    __properties: ClassVar[List[str]] = ["bind_secret_id", "bound_cidr_list", "local_secret_ids", "period", "policies", "role_id", "secret_id_bound_cidrs", "secret_id_num_uses", "secret_id_ttl", "token_bound_cidrs", "token_explicit_max_ttl", "token_max_ttl", "token_no_default_policy", "token_num_uses", "token_period", "token_policies", "token_ttl", "token_type"]

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
        """Create an instance of AppRoleWriteRoleRequest from a JSON string"""
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
        """Create an instance of AppRoleWriteRoleRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "bind_secret_id": obj.get("bind_secret_id") if obj.get("bind_secret_id") is not None else True,
            "bound_cidr_list": obj.get("bound_cidr_list"),
            "local_secret_ids": obj.get("local_secret_ids"),
            "period": obj.get("period"),
            "policies": obj.get("policies"),
            "role_id": obj.get("role_id"),
            "secret_id_bound_cidrs": obj.get("secret_id_bound_cidrs"),
            "secret_id_num_uses": obj.get("secret_id_num_uses"),
            "secret_id_ttl": obj.get("secret_id_ttl"),
            "token_bound_cidrs": obj.get("token_bound_cidrs"),
            "token_explicit_max_ttl": obj.get("token_explicit_max_ttl"),
            "token_max_ttl": obj.get("token_max_ttl"),
            "token_no_default_policy": obj.get("token_no_default_policy"),
            "token_num_uses": obj.get("token_num_uses"),
            "token_period": obj.get("token_period"),
            "token_policies": obj.get("token_policies"),
            "token_ttl": obj.get("token_ttl"),
            "token_type": obj.get("token_type") if obj.get("token_type") is not None else 'default-service'
        })
        return _obj

