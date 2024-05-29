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

class GoogleCloudWriteRoleRequest(BaseModel):
    """
    GoogleCloudWriteRoleRequest
    """ # noqa: E501
    add_group_aliases: Optional[StrictBool] = Field(default=False, description="If true, will add group aliases to auth tokens generated under this role. This will add the full list of ancestors (projects, folders, organizations) for the given entity's project. Requires IAM permission `resourcemanager.projects.get` on this project.")
    allow_gce_inference: Optional[StrictBool] = Field(default=True, description="'iam' roles only. If false, Vault will not not allow GCE instances to login in against this role")
    bound_instance_group: Optional[StrictStr] = Field(default=None, description="Deprecated: use \"bound_instance_groups\" instead.")
    bound_instance_groups: Optional[List[StrictStr]] = Field(default=None, description="Comma-separated list of permitted instance groups to which the GCE instance must belong. This option only applies to \"gce\" roles.")
    bound_labels: Optional[List[StrictStr]] = Field(default=None, description="Comma-separated list of GCP labels formatted as\"key:value\" strings that must be present on the GCE instance in order to authenticate. This option only applies to \"gce\" roles.")
    bound_projects: Optional[List[StrictStr]] = Field(default=None, description="GCP Projects that authenticating entities must belong to.")
    bound_region: Optional[StrictStr] = Field(default=None, description="Deprecated: use \"bound_regions\" instead.")
    bound_regions: Optional[List[StrictStr]] = Field(default=None, description="Comma-separated list of permitted regions to which the GCE instance must belong. If a group is provided, it is assumed to be a regional group. If \"zone\" is provided, this option is ignored. This can be a self-link or region name. This option only applies to \"gce\" roles.")
    bound_service_accounts: Optional[List[StrictStr]] = Field(default=None, description="Can be set for both 'iam' and 'gce' roles (required for 'iam'). A comma-seperated list of authorized service accounts. If the single value \"*\" is given, this is assumed to be all service accounts under the role's project. If this is set on a GCE role, the inferred service account from the instance metadata token will be used.")
    bound_zone: Optional[StrictStr] = Field(default=None, description="Deprecated: use \"bound_zones\" instead.")
    bound_zones: Optional[List[StrictStr]] = Field(default=None, description="Comma-separated list of permitted zones to which the GCE instance must belong. If a group is provided, it is assumed to be a zonal group. This can be a self-link or zone name. This option only applies to \"gce\" roles.")
    max_jwt_exp: Optional[StrictStr] = Field(default='900', description="Currently enabled for 'iam' only. Duration in seconds from time of validation that a JWT must expire within.")
    max_ttl: Optional[StrictStr] = Field(default=None, description="Use \"token_max_ttl\" instead. If this and \"token_max_ttl\" are both specified, only \"token_max_ttl\" will be used.")
    period: Optional[StrictStr] = Field(default=None, description="Use \"token_period\" instead. If this and \"token_period\" are both specified, only \"token_period\" will be used.")
    policies: Optional[List[StrictStr]] = Field(default=None, description="Use \"token_policies\" instead. If this and \"token_policies\" are both specified, only \"token_policies\" will be used.")
    project_id: Optional[StrictStr] = Field(default=None, description="Deprecated: use \"bound_projects\" instead")
    service_accounts: Optional[List[StrictStr]] = Field(default=None, description="Deprecated: use \"bound_service_accounts\" instead.")
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
    type: Optional[StrictStr] = Field(default=None, description="Type of the role. Currently supported: iam, gce")
    __properties: ClassVar[List[str]] = ["add_group_aliases", "allow_gce_inference", "bound_instance_group", "bound_instance_groups", "bound_labels", "bound_projects", "bound_region", "bound_regions", "bound_service_accounts", "bound_zone", "bound_zones", "max_jwt_exp", "max_ttl", "period", "policies", "project_id", "service_accounts", "token_bound_cidrs", "token_explicit_max_ttl", "token_max_ttl", "token_no_default_policy", "token_num_uses", "token_period", "token_policies", "token_ttl", "token_type", "ttl", "type"]

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
        """Create an instance of GoogleCloudWriteRoleRequest from a JSON string"""
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
        """Create an instance of GoogleCloudWriteRoleRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "add_group_aliases": obj.get("add_group_aliases") if obj.get("add_group_aliases") is not None else False,
            "allow_gce_inference": obj.get("allow_gce_inference") if obj.get("allow_gce_inference") is not None else True,
            "bound_instance_group": obj.get("bound_instance_group"),
            "bound_instance_groups": obj.get("bound_instance_groups"),
            "bound_labels": obj.get("bound_labels"),
            "bound_projects": obj.get("bound_projects"),
            "bound_region": obj.get("bound_region"),
            "bound_regions": obj.get("bound_regions"),
            "bound_service_accounts": obj.get("bound_service_accounts"),
            "bound_zone": obj.get("bound_zone"),
            "bound_zones": obj.get("bound_zones"),
            "max_jwt_exp": obj.get("max_jwt_exp") if obj.get("max_jwt_exp") is not None else '900',
            "max_ttl": obj.get("max_ttl"),
            "period": obj.get("period"),
            "policies": obj.get("policies"),
            "project_id": obj.get("project_id"),
            "service_accounts": obj.get("service_accounts"),
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
            "type": obj.get("type")
        })
        return _obj

