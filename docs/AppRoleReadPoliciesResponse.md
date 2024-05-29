# AppRoleReadPoliciesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policies** | **List[str]** | Use \&quot;token_policies\&quot; instead. If this and \&quot;token_policies\&quot; are both specified, only \&quot;token_policies\&quot; will be used. | [optional] 
**token_policies** | **List[str]** | Comma-separated list of policies | [optional] 

## Example

```python
from ahvac.models.app_role_read_policies_response import AppRoleReadPoliciesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AppRoleReadPoliciesResponse from a JSON string
app_role_read_policies_response_instance = AppRoleReadPoliciesResponse.from_json(json)
# print the JSON string representation of the object
print(AppRoleReadPoliciesResponse.to_json())

# convert the object into a dict
app_role_read_policies_response_dict = app_role_read_policies_response_instance.to_dict()
# create an instance of AppRoleReadPoliciesResponse from a dict
app_role_read_policies_response_from_dict = AppRoleReadPoliciesResponse.from_dict(app_role_read_policies_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


