# PoliciesReadAclPolicy2Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**policy** | **str** |  | [optional] 
**rules** | **str** |  | [optional] 

## Example

```python
from ahvac.models.policies_read_acl_policy2_response import PoliciesReadAclPolicy2Response

# TODO update the JSON string below
json = "{}"
# create an instance of PoliciesReadAclPolicy2Response from a JSON string
policies_read_acl_policy2_response_instance = PoliciesReadAclPolicy2Response.from_json(json)
# print the JSON string representation of the object
print(PoliciesReadAclPolicy2Response.to_json())

# convert the object into a dict
policies_read_acl_policy2_response_dict = policies_read_acl_policy2_response_instance.to_dict()
# create an instance of PoliciesReadAclPolicy2Response from a dict
policies_read_acl_policy2_response_from_dict = PoliciesReadAclPolicy2Response.from_dict(policies_read_acl_policy2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


