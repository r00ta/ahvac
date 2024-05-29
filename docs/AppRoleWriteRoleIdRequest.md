# AppRoleWriteRoleIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_id** | **str** | Identifier of the role. Defaults to a UUID. | [optional] 

## Example

```python
from ahvac.models.app_role_write_role_id_request import AppRoleWriteRoleIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppRoleWriteRoleIdRequest from a JSON string
app_role_write_role_id_request_instance = AppRoleWriteRoleIdRequest.from_json(json)
# print the JSON string representation of the object
print(AppRoleWriteRoleIdRequest.to_json())

# convert the object into a dict
app_role_write_role_id_request_dict = app_role_write_role_id_request_instance.to_dict()
# create an instance of AppRoleWriteRoleIdRequest from a dict
app_role_write_role_id_request_from_dict = AppRoleWriteRoleIdRequest.from_dict(app_role_write_role_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


