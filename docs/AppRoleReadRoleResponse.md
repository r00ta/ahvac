# AppRoleReadRoleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bind_secret_id** | **bool** | Impose secret ID to be presented when logging in using this role. | [optional] 
**local_secret_ids** | **bool** | If true, the secret identifiers generated using this role will be cluster local. This can only be set during role creation and once set, it can&#39;t be reset later | [optional] 
**period** | **str** | Use \&quot;token_period\&quot; instead. If this and \&quot;token_period\&quot; are both specified, only \&quot;token_period\&quot; will be used. | [optional] 
**policies** | **List[str]** | Use \&quot;token_policies\&quot; instead. If this and \&quot;token_policies\&quot; are both specified, only \&quot;token_policies\&quot; will be used. | [optional] 
**secret_id_bound_cidrs** | **List[str]** | Comma separated string or list of CIDR blocks. If set, specifies the blocks of IP addresses which can perform the login operation. | [optional] 
**secret_id_num_uses** | **int** | Number of times a secret ID can access the role, after which the secret ID will expire. | [optional] 
**secret_id_ttl** | **str** | Duration in seconds after which the issued secret ID expires. | [optional] 
**token_bound_cidrs** | **List[str]** | Comma separated string or JSON list of CIDR blocks. If set, specifies the blocks of IP addresses which are allowed to use the generated token. | [optional] 
**token_explicit_max_ttl** | **str** | If set, tokens created via this role carry an explicit maximum TTL. During renewal, the current maximum TTL values of the role and the mount are not checked for changes, and any updates to these values will have no effect on the token being renewed. | [optional] 
**token_max_ttl** | **str** | The maximum lifetime of the generated token | [optional] 
**token_no_default_policy** | **bool** | If true, the &#39;default&#39; policy will not automatically be added to generated tokens | [optional] 
**token_num_uses** | **int** | The maximum number of times a token may be used, a value of zero means unlimited | [optional] 
**token_period** | **str** | If set, tokens created via this role will have no max lifetime; instead, their renewal period will be fixed to this value. | [optional] 
**token_policies** | **List[str]** | Comma-separated list of policies | [optional] 
**token_ttl** | **str** | The initial ttl of the token to generate | [optional] 
**token_type** | **str** | The type of token to generate, service or batch | [optional] [default to 'default-service']

## Example

```python
from ahvac.models.app_role_read_role_response import AppRoleReadRoleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AppRoleReadRoleResponse from a JSON string
app_role_read_role_response_instance = AppRoleReadRoleResponse.from_json(json)
# print the JSON string representation of the object
print(AppRoleReadRoleResponse.to_json())

# convert the object into a dict
app_role_read_role_response_dict = app_role_read_role_response_instance.to_dict()
# create an instance of AppRoleReadRoleResponse from a dict
app_role_read_role_response_from_dict = AppRoleReadRoleResponse.from_dict(app_role_read_role_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


