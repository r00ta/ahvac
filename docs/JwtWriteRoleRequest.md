# JwtWriteRoleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_redirect_uris** | **List[str]** | Comma-separated list of allowed values for redirect_uri | [optional] 
**bound_audiences** | **List[str]** | Comma-separated list of &#39;aud&#39; claims that are valid for login; any match is sufficient | [optional] 
**bound_cidrs** | **List[str]** | Use \&quot;token_bound_cidrs\&quot; instead. If this and \&quot;token_bound_cidrs\&quot; are both specified, only \&quot;token_bound_cidrs\&quot; will be used. | [optional] 
**bound_claims** | **object** | Map of claims/values which must match for login | [optional] 
**bound_claims_type** | **str** | How to interpret values in the map of claims/values (which must match for login): allowed values are &#39;string&#39; or &#39;glob&#39; | [optional] [default to 'string']
**bound_subject** | **str** | The &#39;sub&#39; claim that is valid for login. Optional. | [optional] 
**claim_mappings** | **object** | Mappings of claims (key) that will be copied to a metadata field (value) | [optional] 
**clock_skew_leeway** | **str** | Duration in seconds of leeway when validating all claims to account for clock skew. Defaults to 60 (1 minute) if set to 0 and can be disabled if set to -1. | [optional] [default to '60000000000']
**expiration_leeway** | **str** | Duration in seconds of leeway when validating expiration of a token to account for clock skew. Defaults to 150 (2.5 minutes) if set to 0 and can be disabled if set to -1. | [optional] [default to '150']
**groups_claim** | **str** | The claim to use for the Identity group alias names | [optional] 
**max_age** | **str** | Specifies the allowable elapsed time in seconds since the last time the user was actively authenticated. | [optional] 
**max_ttl** | **str** | Use \&quot;token_max_ttl\&quot; instead. If this and \&quot;token_max_ttl\&quot; are both specified, only \&quot;token_max_ttl\&quot; will be used. | [optional] 
**not_before_leeway** | **str** | Duration in seconds of leeway when validating not before values of a token to account for clock skew. Defaults to 150 (2.5 minutes) if set to 0 and can be disabled if set to -1. | [optional] [default to '150']
**num_uses** | **int** | Use \&quot;token_num_uses\&quot; instead. If this and \&quot;token_num_uses\&quot; are both specified, only \&quot;token_num_uses\&quot; will be used. | [optional] 
**oidc_scopes** | **List[str]** | Comma-separated list of OIDC scopes | [optional] 
**period** | **str** | Use \&quot;token_period\&quot; instead. If this and \&quot;token_period\&quot; are both specified, only \&quot;token_period\&quot; will be used. | [optional] 
**policies** | **List[str]** | Use \&quot;token_policies\&quot; instead. If this and \&quot;token_policies\&quot; are both specified, only \&quot;token_policies\&quot; will be used. | [optional] 
**role_type** | **str** | Type of the role, either &#39;jwt&#39; or &#39;oidc&#39;. | [optional] 
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
**user_claim** | **str** | The claim to use for the Identity entity alias name | [optional] 
**user_claim_json_pointer** | **bool** | If true, the user_claim value will use JSON pointer syntax for referencing claims. | [optional] 
**verbose_oidc_logging** | **bool** | Log received OIDC tokens and claims when debug-level logging is active. Not recommended in production since sensitive information may be present in OIDC responses. | [optional] 

## Example

```python
from ahvac.models.jwt_write_role_request import JwtWriteRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of JwtWriteRoleRequest from a JSON string
jwt_write_role_request_instance = JwtWriteRoleRequest.from_json(json)
# print the JSON string representation of the object
print(JwtWriteRoleRequest.to_json())

# convert the object into a dict
jwt_write_role_request_dict = jwt_write_role_request_instance.to_dict()
# create an instance of JwtWriteRoleRequest from a dict
jwt_write_role_request_from_dict = JwtWriteRoleRequest.from_dict(jwt_write_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


