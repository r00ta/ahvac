# UserpassUpdatePoliciesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policies** | **List[str]** | Use \&quot;token_policies\&quot; instead. If this and \&quot;token_policies\&quot; are both specified, only \&quot;token_policies\&quot; will be used. | [optional] 
**token_policies** | **List[str]** | Comma-separated list of policies | [optional] 

## Example

```python
from ahvac.models.userpass_update_policies_request import UserpassUpdatePoliciesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserpassUpdatePoliciesRequest from a JSON string
userpass_update_policies_request_instance = UserpassUpdatePoliciesRequest.from_json(json)
# print the JSON string representation of the object
print(UserpassUpdatePoliciesRequest.to_json())

# convert the object into a dict
userpass_update_policies_request_dict = userpass_update_policies_request_instance.to_dict()
# create an instance of UserpassUpdatePoliciesRequest from a dict
userpass_update_policies_request_from_dict = UserpassUpdatePoliciesRequest.from_dict(userpass_update_policies_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


