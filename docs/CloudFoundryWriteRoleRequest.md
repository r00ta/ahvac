# CloudFoundryWriteRoleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bound_application_ids** | **List[str]** | Require that the client certificate presented has at least one of these app IDs. | [optional] 
**bound_cidrs** | **List[str]** | Use \&quot;token_bound_cidrs\&quot; instead. If this and \&quot;token_bound_cidrs\&quot; are both specified, only \&quot;token_bound_cidrs\&quot; will be used. | [optional] 
**bound_instance_ids** | **List[str]** | Require that the client certificate presented has at least one of these instance IDs. | [optional] 
**bound_organization_ids** | **List[str]** | Require that the client certificate presented has at least one of these org IDs. | [optional] 
**bound_space_ids** | **List[str]** | Require that the client certificate presented has at least one of these space IDs. | [optional] 
**disable_ip_matching** | **bool** | If set to true, disables the default behavior that logging in must be performed from an acceptable IP address described by the certificate presented. | [optional] [default to False]
**max_ttl** | **str** | Use \&quot;token_max_ttl\&quot; instead. If this and \&quot;token_max_ttl\&quot; are both specified, only \&quot;token_max_ttl\&quot; will be used. | [optional] 
**period** | **str** | Use \&quot;token_period\&quot; instead. If this and \&quot;token_period\&quot; are both specified, only \&quot;token_period\&quot; will be used. | [optional] 
**policies** | **List[str]** | Use \&quot;token_policies\&quot; instead. If this and \&quot;token_policies\&quot; are both specified, only \&quot;token_policies\&quot; will be used. | [optional] 
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
from ahvac.models.cloud_foundry_write_role_request import CloudFoundryWriteRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CloudFoundryWriteRoleRequest from a JSON string
cloud_foundry_write_role_request_instance = CloudFoundryWriteRoleRequest.from_json(json)
# print the JSON string representation of the object
print(CloudFoundryWriteRoleRequest.to_json())

# convert the object into a dict
cloud_foundry_write_role_request_dict = cloud_foundry_write_role_request_instance.to_dict()
# create an instance of CloudFoundryWriteRoleRequest from a dict
cloud_foundry_write_role_request_from_dict = CloudFoundryWriteRoleRequest.from_dict(cloud_foundry_write_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


