# PoliciesReadAclPolicyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**policy** | **str** |  | [optional] 
**rules** | **str** |  | [optional] 

## Example

```python
from ahvac.models.policies_read_acl_policy_response import PoliciesReadAclPolicyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PoliciesReadAclPolicyResponse from a JSON string
policies_read_acl_policy_response_instance = PoliciesReadAclPolicyResponse.from_json(json)
# print the JSON string representation of the object
print(PoliciesReadAclPolicyResponse.to_json())

# convert the object into a dict
policies_read_acl_policy_response_dict = policies_read_acl_policy_response_instance.to_dict()
# create an instance of PoliciesReadAclPolicyResponse from a dict
policies_read_acl_policy_response_from_dict = PoliciesReadAclPolicyResponse.from_dict(policies_read_acl_policy_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


