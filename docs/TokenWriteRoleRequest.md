# TokenWriteRoleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_entity_aliases** | **List[str]** | String or JSON list of allowed entity aliases. If set, specifies the entity aliases which are allowed to be used during token generation. This field supports globbing. | [optional] 
**allowed_policies** | **List[str]** | If set, tokens can be created with any subset of the policies in this list, rather than the normal semantics of tokens being a subset of the calling token&#39;s policies. The parameter is a comma-delimited string of policy names. | [optional] 
**allowed_policies_glob** | **List[str]** | If set, tokens can be created with any subset of glob matched policies in this list, rather than the normal semantics of tokens being a subset of the calling token&#39;s policies. The parameter is a comma-delimited string of policy name globs. | [optional] 
**bound_cidrs** | **List[str]** | Use &#39;token_bound_cidrs&#39; instead. | [optional] 
**disallowed_policies** | **List[str]** | If set, successful token creation via this role will require that no policies in the given list are requested. The parameter is a comma-delimited string of policy names. | [optional] 
**disallowed_policies_glob** | **List[str]** | If set, successful token creation via this role will require that no requested policies glob match any of policies in this list. The parameter is a comma-delimited string of policy name globs. | [optional] 
**explicit_max_ttl** | **str** | Use &#39;token_explicit_max_ttl&#39; instead. | [optional] 
**orphan** | **bool** | If true, tokens created via this role will be orphan tokens (have no parent) | [optional] 
**path_suffix** | **str** | If set, tokens created via this role will contain the given suffix as a part of their path. This can be used to assist use of the &#39;revoke-prefix&#39; endpoint later on. The given suffix must match the regular expression.\\w[\\w-.]+\\w | [optional] 
**period** | **str** | Use &#39;token_period&#39; instead. | [optional] 
**renewable** | **bool** | Tokens created via this role will be renewable or not according to this value. Defaults to \&quot;true\&quot;. | [optional] [default to True]
**token_bound_cidrs** | **List[str]** | Comma separated string or JSON list of CIDR blocks. If set, specifies the blocks of IP addresses which are allowed to use the generated token. | [optional] 
**token_explicit_max_ttl** | **str** | If set, tokens created via this role carry an explicit maximum TTL. During renewal, the current maximum TTL values of the role and the mount are not checked for changes, and any updates to these values will have no effect on the token being renewed. | [optional] 
**token_no_default_policy** | **bool** | If true, the &#39;default&#39; policy will not automatically be added to generated tokens | [optional] 
**token_num_uses** | **int** | The maximum number of times a token may be used, a value of zero means unlimited | [optional] 
**token_period** | **str** | If set, tokens created via this role will have no max lifetime; instead, their renewal period will be fixed to this value. This takes an integer number of seconds, or a string duration (e.g. \&quot;24h\&quot;). | [optional] 
**token_type** | **str** | The type of token to generate, service or batch | [optional] [default to 'default-service']

## Example

```python
from ahvac.models.token_write_role_request import TokenWriteRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TokenWriteRoleRequest from a JSON string
token_write_role_request_instance = TokenWriteRoleRequest.from_json(json)
# print the JSON string representation of the object
print(TokenWriteRoleRequest.to_json())

# convert the object into a dict
token_write_role_request_dict = token_write_role_request_instance.to_dict()
# create an instance of TokenWriteRoleRequest from a dict
token_write_role_request_from_dict = TokenWriteRoleRequest.from_dict(token_write_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


