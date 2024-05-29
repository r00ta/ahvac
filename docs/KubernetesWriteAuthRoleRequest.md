# KubernetesWriteAuthRoleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias_name_source** | **str** | Source to use when deriving the Alias name. valid choices: \&quot;serviceaccount_uid\&quot; : &lt;token.uid&gt; e.g. 474b11b5-0f20-4f9d-8ca5-65715ab325e0 (most secure choice) \&quot;serviceaccount_name\&quot; : &lt;namespace&gt;/&lt;serviceaccount&gt; e.g. vault/vault-agent default: \&quot;serviceaccount_uid\&quot; | [optional] [default to 'serviceaccount_uid']
**audience** | **str** | Optional Audience claim to verify in the jwt. | [optional] 
**bound_cidrs** | **List[str]** | Use \&quot;token_bound_cidrs\&quot; instead. If this and \&quot;token_bound_cidrs\&quot; are both specified, only \&quot;token_bound_cidrs\&quot; will be used. | [optional] 
**bound_service_account_names** | **List[str]** | List of service account names able to access this role. If set to \&quot;*\&quot; all names are allowed. | [optional] 
**bound_service_account_namespaces** | **List[str]** | List of namespaces allowed to access this role. If set to \&quot;*\&quot; all namespaces are allowed. | [optional] 
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
from ahvac.models.kubernetes_write_auth_role_request import KubernetesWriteAuthRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesWriteAuthRoleRequest from a JSON string
kubernetes_write_auth_role_request_instance = KubernetesWriteAuthRoleRequest.from_json(json)
# print the JSON string representation of the object
print(KubernetesWriteAuthRoleRequest.to_json())

# convert the object into a dict
kubernetes_write_auth_role_request_dict = kubernetes_write_auth_role_request_instance.to_dict()
# create an instance of KubernetesWriteAuthRoleRequest from a dict
kubernetes_write_auth_role_request_from_dict = KubernetesWriteAuthRoleRequest.from_dict(kubernetes_write_auth_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


