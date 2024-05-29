# AppRoleWriteBindSecretIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bind_secret_id** | **bool** | Impose secret_id to be presented when logging in using this role. | [optional] [default to True]

## Example

```python
from ahvac.models.app_role_write_bind_secret_id_request import AppRoleWriteBindSecretIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppRoleWriteBindSecretIdRequest from a JSON string
app_role_write_bind_secret_id_request_instance = AppRoleWriteBindSecretIdRequest.from_json(json)
# print the JSON string representation of the object
print(AppRoleWriteBindSecretIdRequest.to_json())

# convert the object into a dict
app_role_write_bind_secret_id_request_dict = app_role_write_bind_secret_id_request_instance.to_dict()
# create an instance of AppRoleWriteBindSecretIdRequest from a dict
app_role_write_bind_secret_id_request_from_dict = AppRoleWriteBindSecretIdRequest.from_dict(app_role_write_bind_secret_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


