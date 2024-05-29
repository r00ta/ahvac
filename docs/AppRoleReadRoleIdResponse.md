# AppRoleReadRoleIdResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_id** | **str** | Identifier of the role. Defaults to a UUID. | [optional] 

## Example

```python
from ahvac.models.app_role_read_role_id_response import AppRoleReadRoleIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AppRoleReadRoleIdResponse from a JSON string
app_role_read_role_id_response_instance = AppRoleReadRoleIdResponse.from_json(json)
# print the JSON string representation of the object
print(AppRoleReadRoleIdResponse.to_json())

# convert the object into a dict
app_role_read_role_id_response_dict = app_role_read_role_id_response_instance.to_dict()
# create an instance of AppRoleReadRoleIdResponse from a dict
app_role_read_role_id_response_from_dict = AppRoleReadRoleIdResponse.from_dict(app_role_read_role_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


