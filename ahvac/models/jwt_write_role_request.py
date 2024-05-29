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

class JwtWriteRoleRequest(BaseModel):
    """
    JwtWriteRoleRequest
    """ # noqa: E501
    allowed_redirect_uris: Optional[List[StrictStr]] = Field(default=None, description="Comma-separated list of allowed values for redirect_uri")
    bound_audiences: Optional[List[StrictStr]] = Field(default=None, description="Comma-separated list of 'aud' claims that are valid for login; any match is sufficient")
    bound_cidrs: Optional[List[StrictStr]] = Field(default=None, description="Use \"token_bound_cidrs\" instead. If this and \"token_bound_cidrs\" are both specified, only \"token_bound_cidrs\" will be used.")
    bound_claims: Optional[Dict[str, Any]] = Field(default=None, description="Map of claims/values which must match for login")
    bound_claims_type: Optional[StrictStr] = Field(default='string', description="How to interpret values in the map of claims/values (which must match for login): allowed values are 'string' or 'glob'")
    bound_subject: Optional[StrictStr] = Field(default=None, description="The 'sub' claim that is valid for login. Optional.")
    claim_mappings: Optional[Dict[str, Any]] = Field(default=None, description="Mappings of claims (key) that will be copied to a metadata field (value)")
    clock_skew_leeway: Optional[StrictStr] = Field(default='60000000000', description="Duration in seconds of leeway when validating all claims to account for clock skew. Defaults to 60 (1 minute) if set to 0 and can be disabled if set to -1.")
    expiration_leeway: Optional[StrictStr] = Field(default='150', description="Duration in seconds of leeway when validating expiration of a token to account for clock skew. Defaults to 150 (2.5 minutes) if set to 0 and can be disabled if set to -1.")
    groups_claim: Optional[StrictStr] = Field(default=None, description="The claim to use for the Identity group alias names")
    max_age: Optional[StrictStr] = Field(default=None, description="Specifies the allowable elapsed time in seconds since the last time the user was actively authenticated.")
    max_ttl: Optional[StrictStr] = Field(default=None, description="Use \"token_max_ttl\" instead. If this and \"token_max_ttl\" are both specified, only \"token_max_ttl\" will be used.")
    not_before_leeway: Optional[StrictStr] = Field(default='150', description="Duration in seconds of leeway when validating not before values of a token to account for clock skew. Defaults to 150 (2.5 minutes) if set to 0 and can be disabled if set to -1.")
    num_uses: Optional[StrictInt] = Field(default=None, description="Use \"token_num_uses\" instead. If this and \"token_num_uses\" are both specified, only \"token_num_uses\" will be used.")
    oidc_scopes: Optional[List[StrictStr]] = Field(default=None, description="Comma-separated list of OIDC scopes")
    period: Optional[StrictStr] = Field(default=None, description="Use \"token_period\" instead. If this and \"token_period\" are both specified, only \"token_period\" will be used.")
    policies: Optional[List[StrictStr]] = Field(default=None, description="Use \"token_policies\" instead. If this and \"token_policies\" are both specified, only \"token_policies\" will be used.")
    role_type: Optional[StrictStr] = Field(default=None, description="Type of the role, either 'jwt' or 'oidc'.")
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
    user_claim: Optional[StrictStr] = Field(default=None, description="The claim to use for the Identity entity alias name")
    user_claim_json_pointer: Optional[StrictBool] = Field(default=None, description="If true, the user_claim value will use JSON pointer syntax for referencing claims.")
    verbose_oidc_logging: Optional[StrictBool] = Field(default=None, description="Log received OIDC tokens and claims when debug-level logging is active. Not recommended in production since sensitive information may be present in OIDC responses.")
    __properties: ClassVar[List[str]] = ["allowed_redirect_uris", "bound_audiences", "bound_cidrs", "bound_claims", "bound_claims_type", "bound_subject", "claim_mappings", "clock_skew_leeway", "expiration_leeway", "groups_claim", "max_age", "max_ttl", "not_before_leeway", "num_uses", "oidc_scopes", "period", "policies", "role_type", "token_bound_cidrs", "token_explicit_max_ttl", "token_max_ttl", "token_no_default_policy", "token_num_uses", "token_period", "token_policies", "token_ttl", "token_type", "ttl", "user_claim", "user_claim_json_pointer", "verbose_oidc_logging"]

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
        """Create an instance of JwtWriteRoleRequest from a JSON string"""
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
        """Create an instance of JwtWriteRoleRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "allowed_redirect_uris": obj.get("allowed_redirect_uris"),
            "bound_audiences": obj.get("bound_audiences"),
            "bound_cidrs": obj.get("bound_cidrs"),
            "bound_claims": obj.get("bound_claims"),
            "bound_claims_type": obj.get("bound_claims_type") if obj.get("bound_claims_type") is not None else 'string',
            "bound_subject": obj.get("bound_subject"),
            "claim_mappings": obj.get("claim_mappings"),
            "clock_skew_leeway": obj.get("clock_skew_leeway") if obj.get("clock_skew_leeway") is not None else '60000000000',
            "expiration_leeway": obj.get("expiration_leeway") if obj.get("expiration_leeway") is not None else '150',
            "groups_claim": obj.get("groups_claim"),
            "max_age": obj.get("max_age"),
            "max_ttl": obj.get("max_ttl"),
            "not_before_leeway": obj.get("not_before_leeway") if obj.get("not_before_leeway") is not None else '150',
            "num_uses": obj.get("num_uses"),
            "oidc_scopes": obj.get("oidc_scopes"),
            "period": obj.get("period"),
            "policies": obj.get("policies"),
            "role_type": obj.get("role_type"),
            "token_bound_cidrs": obj.get("token_bound_cidrs"),
            "token_explicit_max_ttl": obj.get("token_explicit_max_ttl"),
            "token_max_ttl": obj.get("token_max_ttl"),
            "token_no_default_policy": obj.get("token_no_default_policy"),
            "token_num_uses": obj.get("token_num_uses"),
            "token_period": obj.get("token_period"),
            "token_policies": obj.get("token_policies"),
            "token_ttl": obj.get("token_ttl"),
            "token_type": obj.get("token_type") if obj.get("token_type") is not None else 'default-service',
            "ttl": obj.get("ttl"),
            "user_claim": obj.get("user_claim"),
            "user_claim_json_pointer": obj.get("user_claim_json_pointer"),
            "verbose_oidc_logging": obj.get("verbose_oidc_logging")
        })
        return _obj

