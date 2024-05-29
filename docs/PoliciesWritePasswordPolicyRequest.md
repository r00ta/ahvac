# PoliciesWritePasswordPolicyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy** | **str** | The password policy | [optional] 

## Example

```python
from ahvac.models.policies_write_password_policy_request import PoliciesWritePasswordPolicyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PoliciesWritePasswordPolicyRequest from a JSON string
policies_write_password_policy_request_instance = PoliciesWritePasswordPolicyRequest.from_json(json)
# print the JSON string representation of the object
print(PoliciesWritePasswordPolicyRequest.to_json())

# convert the object into a dict
policies_write_password_policy_request_dict = policies_write_password_policy_request_instance.to_dict()
# create an instance of PoliciesWritePasswordPolicyRequest from a dict
policies_write_password_policy_request_from_dict = PoliciesWritePasswordPolicyRequest.from_dict(policies_write_password_policy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


