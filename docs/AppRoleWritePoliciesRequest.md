# AppRoleWritePoliciesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policies** | **List[str]** | Use \&quot;token_policies\&quot; instead. If this and \&quot;token_policies\&quot; are both specified, only \&quot;token_policies\&quot; will be used. | [optional] 
**token_policies** | **List[str]** | Comma-separated list of policies | [optional] 

## Example

```python
from ahvac.models.app_role_write_policies_request import AppRoleWritePoliciesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppRoleWritePoliciesRequest from a JSON string
app_role_write_policies_request_instance = AppRoleWritePoliciesRequest.from_json(json)
# print the JSON string representation of the object
print(AppRoleWritePoliciesRequest.to_json())

# convert the object into a dict
app_role_write_policies_request_dict = app_role_write_policies_request_instance.to_dict()
# create an instance of AppRoleWritePoliciesRequest from a dict
app_role_write_policies_request_from_dict = AppRoleWritePoliciesRequest.from_dict(app_role_write_policies_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


