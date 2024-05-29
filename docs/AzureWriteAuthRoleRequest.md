# AzureWriteAuthRoleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bound_group_ids** | **List[str]** | Comma-separated list of group ids that login is restricted to. | [optional] 
**bound_locations** | **List[str]** | Comma-separated list of locations that login is restricted to. | [optional] 
**bound_resource_groups** | **List[str]** | Comma-separated list of resource groups that login is restricted to. | [optional] 
**bound_scale_sets** | **List[str]** | Comma-separated list of scale sets that login is restricted to. | [optional] 
**bound_service_principal_ids** | **List[str]** | Comma-separated list of service principal ids that login is restricted to. | [optional] 
**bound_subscription_ids** | **List[str]** | Comma-separated list of subscription ids that login is restricted to. | [optional] 
**max_ttl** | **str** | Use \&quot;token_max_ttl\&quot; instead. If this and \&quot;token_max_ttl\&quot; are both specified, only \&quot;token_max_ttl\&quot; will be used. | [optional] 
**num_uses** | **int** | Use \&quot;token_num_uses\&quot; instead. If this and \&quot;token_num_uses\&quot; are both specified, only \&quot;token_num_uses\&quot; will be used. | [optional] 
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
from ahvac.models.azure_write_auth_role_request import AzureWriteAuthRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AzureWriteAuthRoleRequest from a JSON string
azure_write_auth_role_request_instance = AzureWriteAuthRoleRequest.from_json(json)
# print the JSON string representation of the object
print(AzureWriteAuthRoleRequest.to_json())

# convert the object into a dict
azure_write_auth_role_request_dict = azure_write_auth_role_request_instance.to_dict()
# create an instance of AzureWriteAuthRoleRequest from a dict
azure_write_auth_role_request_from_dict = AzureWriteAuthRoleRequest.from_dict(azure_write_auth_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


