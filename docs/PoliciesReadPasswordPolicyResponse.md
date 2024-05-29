# PoliciesReadPasswordPolicyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy** | **str** |  | [optional] 

## Example

```python
from ahvac.models.policies_read_password_policy_response import PoliciesReadPasswordPolicyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PoliciesReadPasswordPolicyResponse from a JSON string
policies_read_password_policy_response_instance = PoliciesReadPasswordPolicyResponse.from_json(json)
# print the JSON string representation of the object
print(PoliciesReadPasswordPolicyResponse.to_json())

# convert the object into a dict
policies_read_password_policy_response_dict = policies_read_password_policy_response_instance.to_dict()
# create an instance of PoliciesReadPasswordPolicyResponse from a dict
policies_read_password_policy_response_from_dict = PoliciesReadPasswordPolicyResponse.from_dict(policies_read_password_policy_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


