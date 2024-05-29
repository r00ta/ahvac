# AppRoleLoginResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  | [optional] 

## Example

```python
from ahvac.models.app_role_login_response import AppRoleLoginResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AppRoleLoginResponse from a JSON string
app_role_login_response_instance = AppRoleLoginResponse.from_json(json)
# print the JSON string representation of the object
print(AppRoleLoginResponse.to_json())

# convert the object into a dict
app_role_login_response_dict = app_role_login_response_instance.to_dict()
# create an instance of AppRoleLoginResponse from a dict
app_role_login_response_from_dict = AppRoleLoginResponse.from_dict(app_role_login_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


