# AppRoleLoginRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_id** | **str** | Unique identifier of the Role. Required to be supplied when the &#39;bind_secret_id&#39; constraint is set. | [optional] 
**secret_id** | **str** | SecretID belong to the App role | [optional] [default to '']

## Example

```python
from ahvac.models.app_role_login_request import AppRoleLoginRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppRoleLoginRequest from a JSON string
app_role_login_request_instance = AppRoleLoginRequest.from_json(json)
# print the JSON string representation of the object
print(AppRoleLoginRequest.to_json())

# convert the object into a dict
app_role_login_request_dict = app_role_login_request_instance.to_dict()
# create an instance of AppRoleLoginRequest from a dict
app_role_login_request_from_dict = AppRoleLoginRequest.from_dict(app_role_login_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


