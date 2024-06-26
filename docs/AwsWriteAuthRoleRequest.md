# AwsWriteAuthRoleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_instance_migration** | **bool** | If set, allows migration of the underlying instance where the client resides. This keys off of pendingTime in the metadata document, so essentially, this disables the client nonce check whenever the instance is migrated to a new host and pendingTime is newer than the previously-remembered time. Use with caution. This is only checked when auth_type is ec2. | [optional] [default to False]
**auth_type** | **str** | The auth_type permitted to authenticate to this role. Must be one of iam or ec2 and cannot be changed after role creation. | [optional] 
**bound_account_id** | **List[str]** | If set, defines a constraint on the EC2 instances that the account ID in its identity document to match one of the IDs specified by this parameter. This is only applicable when auth_type is ec2 or inferred_entity_type is ec2_instance. | [optional] 
**bound_ami_id** | **List[str]** | If set, defines a constraint on the EC2 instances that they should be using one of the AMI IDs specified by this parameter. This is only applicable when auth_type is ec2 or inferred_entity_type is ec2_instance. | [optional] 
**bound_ec2_instance_id** | **List[str]** | If set, defines a constraint on the EC2 instances to have one of the given instance IDs. Can be a list or comma-separated string of EC2 instance IDs. This is only applicable when auth_type is ec2 or inferred_entity_type is ec2_instance. | [optional] 
**bound_iam_instance_profile_arn** | **List[str]** | If set, defines a constraint on the EC2 instances to be associated with an IAM instance profile ARN which has a prefix that matches one of the values specified by this parameter. The value is prefix-matched (as though it were a glob ending in &#39;*&#39;). This is only applicable when auth_type is ec2 or inferred_entity_type is ec2_instance. | [optional] 
**bound_iam_principal_arn** | **List[str]** | ARN of the IAM principals to bind to this role. Only applicable when auth_type is iam. | [optional] 
**bound_iam_role_arn** | **List[str]** | If set, defines a constraint on the authenticating EC2 instance that it must match one of the IAM role ARNs specified by this parameter. The value is prefix-matched (as though it were a glob ending in &#39;*&#39;). The configured IAM user or EC2 instance role must be allowed to execute the &#39;iam:GetInstanceProfile&#39; action if this is specified. This is only applicable when auth_type is ec2 or inferred_entity_type is ec2_instance. | [optional] 
**bound_region** | **List[str]** | If set, defines a constraint on the EC2 instances that the region in its identity document match one of the regions specified by this parameter. This is only applicable when auth_type is ec2. | [optional] 
**bound_subnet_id** | **List[str]** | If set, defines a constraint on the EC2 instance to be associated with the subnet ID that matches one of the values specified by this parameter. This is only applicable when auth_type is ec2 or inferred_entity_type is ec2_instance. | [optional] 
**bound_vpc_id** | **List[str]** | If set, defines a constraint on the EC2 instance to be associated with a VPC ID that matches one of the value specified by this parameter. This is only applicable when auth_type is ec2 or inferred_entity_type is ec2_instance. | [optional] 
**disallow_reauthentication** | **bool** | If set, only allows a single token to be granted per instance ID. In order to perform a fresh login, the entry in the access list for the instance ID needs to be cleared using &#39;auth/aws-ec2/identity-accesslist/&lt;instance_id&gt;&#39; endpoint. This is only applicable when auth_type is ec2. | [optional] [default to False]
**inferred_aws_region** | **str** | When auth_type is iam and inferred_entity_type is set, the region to assume the inferred entity exists in. | [optional] 
**inferred_entity_type** | **str** | When auth_type is iam, the AWS entity type to infer from the authenticated principal. The only supported value is ec2_instance, which will extract the EC2 instance ID from the authenticated role and apply the following restrictions specific to EC2 instances: bound_ami_id, bound_account_id, bound_iam_role_arn, bound_iam_instance_profile_arn, bound_vpc_id, bound_subnet_id. The configured EC2 client must be able to find the inferred instance ID in the results, and the instance must be running. If unable to determine the EC2 instance ID or unable to find the EC2 instance ID among running instances, then authentication will fail. | [optional] 
**max_ttl** | **str** | Use \&quot;token_max_ttl\&quot; instead. If this and \&quot;token_max_ttl\&quot; are both specified, only \&quot;token_max_ttl\&quot; will be used. | [optional] 
**period** | **str** | Use \&quot;token_period\&quot; instead. If this and \&quot;token_period\&quot; are both specified, only \&quot;token_period\&quot; will be used. | [optional] 
**policies** | **List[str]** | Use \&quot;token_policies\&quot; instead. If this and \&quot;token_policies\&quot; are both specified, only \&quot;token_policies\&quot; will be used. | [optional] 
**resolve_aws_unique_ids** | **bool** | If set, resolve all AWS IAM ARNs into AWS&#39;s internal unique IDs. When an IAM entity (e.g., user, role, or instance profile) is deleted, then all references to it within the role will be invalidated, which prevents a new IAM entity from being created with the same name and matching the role&#39;s IAM binds. Once set, this cannot be unset. | [optional] [default to True]
**role_tag** | **str** | If set, enables the role tags for this role. The value set for this field should be the &#39;key&#39; of the tag on the EC2 instance. The &#39;value&#39; of the tag should be generated using &#39;role/&lt;role&gt;/tag&#39; endpoint. Defaults to an empty string, meaning that role tags are disabled. This is only allowed if auth_type is ec2. | [optional] [default to '']
**token_bound_cidrs** | **List[str]** | Comma separated string or JSON list of CIDR blocks. If set, specifies the blocks of IP addresses which are allowed to use the generated token. | [optional] 
**token_explicit_max_ttl** | **str** | If set, tokens created via this role carry an explicit maximum TTL. During renewal, the current maximum TTL values of the role and the mount are not checked for changes, and any updates to these values will have no effect on the token being renewed. | [optional] 
**token_max_ttl** | **str** | The maximum lifetime of the generated token | [optional] 
**token_no_default_policy** | **bool** | If true, the &#39;default&#39; policy will not automatically be added to generated tokens | [optional] 
**token_num_uses** | **int** | The maximum number of times a token may be used, a value of zero means unlimited | [optional] 
**token_period** | **str** | If set, tokens created via this role will have no max lifetime; instead, their renewal period will be fixed to this value. This takes an integer number of seconds, or a string duration (e.g. \&quot;24h\&quot;). | [optional] 
**token_policies** | **List[str]** | Comma-separated list of policies | [optional] 
**token_ttl** | **str** | The initial ttl of the token to generate | [optional] 
**token_type** | **str** | The type of token to generate, service or batch | [optional] [default to 'default-service']
**ttl** | **str** | Use \&quot;token_ttl\&quot; instead. If this and \&quot;token_ttl\&quot; are both specified, only \&quot;token_ttl\&quot; will be used. | [optional] 

## Example

```python
from ahvac.models.aws_write_auth_role_request import AwsWriteAuthRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AwsWriteAuthRoleRequest from a JSON string
aws_write_auth_role_request_instance = AwsWriteAuthRoleRequest.from_json(json)
# print the JSON string representation of the object
print(AwsWriteAuthRoleRequest.to_json())

# convert the object into a dict
aws_write_auth_role_request_dict = aws_write_auth_role_request_instance.to_dict()
# create an instance of AwsWriteAuthRoleRequest from a dict
aws_write_auth_role_request_from_dict = AwsWriteAuthRoleRequest.from_dict(aws_write_auth_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


