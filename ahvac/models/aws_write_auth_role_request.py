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

class AwsWriteAuthRoleRequest(BaseModel):
    """
    AwsWriteAuthRoleRequest
    """ # noqa: E501
    allow_instance_migration: Optional[StrictBool] = Field(default=False, description="If set, allows migration of the underlying instance where the client resides. This keys off of pendingTime in the metadata document, so essentially, this disables the client nonce check whenever the instance is migrated to a new host and pendingTime is newer than the previously-remembered time. Use with caution. This is only checked when auth_type is ec2.")
    auth_type: Optional[StrictStr] = Field(default=None, description="The auth_type permitted to authenticate to this role. Must be one of iam or ec2 and cannot be changed after role creation.")
    bound_account_id: Optional[List[StrictStr]] = Field(default=None, description="If set, defines a constraint on the EC2 instances that the account ID in its identity document to match one of the IDs specified by this parameter. This is only applicable when auth_type is ec2 or inferred_entity_type is ec2_instance.")
    bound_ami_id: Optional[List[StrictStr]] = Field(default=None, description="If set, defines a constraint on the EC2 instances that they should be using one of the AMI IDs specified by this parameter. This is only applicable when auth_type is ec2 or inferred_entity_type is ec2_instance.")
    bound_ec2_instance_id: Optional[List[StrictStr]] = Field(default=None, description="If set, defines a constraint on the EC2 instances to have one of the given instance IDs. Can be a list or comma-separated string of EC2 instance IDs. This is only applicable when auth_type is ec2 or inferred_entity_type is ec2_instance.")
    bound_iam_instance_profile_arn: Optional[List[StrictStr]] = Field(default=None, description="If set, defines a constraint on the EC2 instances to be associated with an IAM instance profile ARN which has a prefix that matches one of the values specified by this parameter. The value is prefix-matched (as though it were a glob ending in '*'). This is only applicable when auth_type is ec2 or inferred_entity_type is ec2_instance.")
    bound_iam_principal_arn: Optional[List[StrictStr]] = Field(default=None, description="ARN of the IAM principals to bind to this role. Only applicable when auth_type is iam.")
    bound_iam_role_arn: Optional[List[StrictStr]] = Field(default=None, description="If set, defines a constraint on the authenticating EC2 instance that it must match one of the IAM role ARNs specified by this parameter. The value is prefix-matched (as though it were a glob ending in '*'). The configured IAM user or EC2 instance role must be allowed to execute the 'iam:GetInstanceProfile' action if this is specified. This is only applicable when auth_type is ec2 or inferred_entity_type is ec2_instance.")
    bound_region: Optional[List[StrictStr]] = Field(default=None, description="If set, defines a constraint on the EC2 instances that the region in its identity document match one of the regions specified by this parameter. This is only applicable when auth_type is ec2.")
    bound_subnet_id: Optional[List[StrictStr]] = Field(default=None, description="If set, defines a constraint on the EC2 instance to be associated with the subnet ID that matches one of the values specified by this parameter. This is only applicable when auth_type is ec2 or inferred_entity_type is ec2_instance.")
    bound_vpc_id: Optional[List[StrictStr]] = Field(default=None, description="If set, defines a constraint on the EC2 instance to be associated with a VPC ID that matches one of the value specified by this parameter. This is only applicable when auth_type is ec2 or inferred_entity_type is ec2_instance.")
    disallow_reauthentication: Optional[StrictBool] = Field(default=False, description="If set, only allows a single token to be granted per instance ID. In order to perform a fresh login, the entry in the access list for the instance ID needs to be cleared using 'auth/aws-ec2/identity-accesslist/<instance_id>' endpoint. This is only applicable when auth_type is ec2.")
    inferred_aws_region: Optional[StrictStr] = Field(default=None, description="When auth_type is iam and inferred_entity_type is set, the region to assume the inferred entity exists in.")
    inferred_entity_type: Optional[StrictStr] = Field(default=None, description="When auth_type is iam, the AWS entity type to infer from the authenticated principal. The only supported value is ec2_instance, which will extract the EC2 instance ID from the authenticated role and apply the following restrictions specific to EC2 instances: bound_ami_id, bound_account_id, bound_iam_role_arn, bound_iam_instance_profile_arn, bound_vpc_id, bound_subnet_id. The configured EC2 client must be able to find the inferred instance ID in the results, and the instance must be running. If unable to determine the EC2 instance ID or unable to find the EC2 instance ID among running instances, then authentication will fail.")
    max_ttl: Optional[StrictStr] = Field(default=None, description="Use \"token_max_ttl\" instead. If this and \"token_max_ttl\" are both specified, only \"token_max_ttl\" will be used.")
    period: Optional[StrictStr] = Field(default=None, description="Use \"token_period\" instead. If this and \"token_period\" are both specified, only \"token_period\" will be used.")
    policies: Optional[List[StrictStr]] = Field(default=None, description="Use \"token_policies\" instead. If this and \"token_policies\" are both specified, only \"token_policies\" will be used.")
    resolve_aws_unique_ids: Optional[StrictBool] = Field(default=True, description="If set, resolve all AWS IAM ARNs into AWS's internal unique IDs. When an IAM entity (e.g., user, role, or instance profile) is deleted, then all references to it within the role will be invalidated, which prevents a new IAM entity from being created with the same name and matching the role's IAM binds. Once set, this cannot be unset.")
    role_tag: Optional[StrictStr] = Field(default='', description="If set, enables the role tags for this role. The value set for this field should be the 'key' of the tag on the EC2 instance. The 'value' of the tag should be generated using 'role/<role>/tag' endpoint. Defaults to an empty string, meaning that role tags are disabled. This is only allowed if auth_type is ec2.")
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
    __properties: ClassVar[List[str]] = ["allow_instance_migration", "auth_type", "bound_account_id", "bound_ami_id", "bound_ec2_instance_id", "bound_iam_instance_profile_arn", "bound_iam_principal_arn", "bound_iam_role_arn", "bound_region", "bound_subnet_id", "bound_vpc_id", "disallow_reauthentication", "inferred_aws_region", "inferred_entity_type", "max_ttl", "period", "policies", "resolve_aws_unique_ids", "role_tag", "token_bound_cidrs", "token_explicit_max_ttl", "token_max_ttl", "token_no_default_policy", "token_num_uses", "token_period", "token_policies", "token_ttl", "token_type", "ttl"]

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
        """Create an instance of AwsWriteAuthRoleRequest from a JSON string"""
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
        """Create an instance of AwsWriteAuthRoleRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "allow_instance_migration": obj.get("allow_instance_migration") if obj.get("allow_instance_migration") is not None else False,
            "auth_type": obj.get("auth_type"),
            "bound_account_id": obj.get("bound_account_id"),
            "bound_ami_id": obj.get("bound_ami_id"),
            "bound_ec2_instance_id": obj.get("bound_ec2_instance_id"),
            "bound_iam_instance_profile_arn": obj.get("bound_iam_instance_profile_arn"),
            "bound_iam_principal_arn": obj.get("bound_iam_principal_arn"),
            "bound_iam_role_arn": obj.get("bound_iam_role_arn"),
            "bound_region": obj.get("bound_region"),
            "bound_subnet_id": obj.get("bound_subnet_id"),
            "bound_vpc_id": obj.get("bound_vpc_id"),
            "disallow_reauthentication": obj.get("disallow_reauthentication") if obj.get("disallow_reauthentication") is not None else False,
            "inferred_aws_region": obj.get("inferred_aws_region"),
            "inferred_entity_type": obj.get("inferred_entity_type"),
            "max_ttl": obj.get("max_ttl"),
            "period": obj.get("period"),
            "policies": obj.get("policies"),
            "resolve_aws_unique_ids": obj.get("resolve_aws_unique_ids") if obj.get("resolve_aws_unique_ids") is not None else True,
            "role_tag": obj.get("role_tag") if obj.get("role_tag") is not None else '',
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


