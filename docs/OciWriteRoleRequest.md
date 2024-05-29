# OciWriteRoleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ocid_list** | **List[str]** | A comma separated list of Group or Dynamic Group OCIDs that are allowed to take this role. | [optional] 
**token_bound_cidrs** | **List[str]** | Comma separated string or JSON list of CIDR blocks. If set, specifies the blocks of IP addresses which are allowed to use the generated token. | [optional] 
**token_explicit_max_ttl** | **str** | If set, tokens created via this role carry an explicit maximum TTL. During renewal, the current maximum TTL values of the role and the mount are not checked for changes, and any updates to these values will have no effect on the token being renewed. | [optional] 
**token_max_ttl** | **str** | The maximum lifetime of the generated token | [optional] 
**token_no_default_policy** | **bool** | If true, the &#39;default&#39; policy will not automatically be added to generated tokens | [optional] 
**token_num_uses** | **int** | The maximum number of times a token may be used, a value of zero means unlimited | [optional] 
**token_period** | **str** | If set, tokens created via this role will have no max lifetime; instead, their renewal period will be fixed to this value. This takes an integer number of seconds, or a string duration (e.g. \&quot;24h\&quot;). | [optional] 
**token_policies** | **List[str]** | Comma-separated list of policies | [optional] 
**token_ttl** | **str** | The initial ttl of the token to generate | [optional] 
**token_type** | **str** | The type of token to generate, service or batch | [optional] [default to 'default-service']

## Example

```python
from ahvac.models.oci_write_role_request import OciWriteRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OciWriteRoleRequest from a JSON string
oci_write_role_request_instance = OciWriteRoleRequest.from_json(json)
# print the JSON string representation of the object
print(OciWriteRoleRequest.to_json())

# convert the object into a dict
oci_write_role_request_dict = oci_write_role_request_instance.to_dict()
# create an instance of OciWriteRoleRequest from a dict
oci_write_role_request_from_dict = OciWriteRoleRequest.from_dict(oci_write_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


