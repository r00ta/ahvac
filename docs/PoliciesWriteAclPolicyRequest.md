# PoliciesWriteAclPolicyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy** | **str** | The rules of the policy. | [optional] 

## Example

```python
from ahvac.models.policies_write_acl_policy_request import PoliciesWriteAclPolicyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PoliciesWriteAclPolicyRequest from a JSON string
policies_write_acl_policy_request_instance = PoliciesWriteAclPolicyRequest.from_json(json)
# print the JSON string representation of the object
print(PoliciesWriteAclPolicyRequest.to_json())

# convert the object into a dict
policies_write_acl_policy_request_dict = policies_write_acl_policy_request_instance.to_dict()
# create an instance of PoliciesWriteAclPolicyRequest from a dict
policies_write_acl_policy_request_from_dict = PoliciesWriteAclPolicyRequest.from_dict(policies_write_acl_policy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


