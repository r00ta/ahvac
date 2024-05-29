# AppRoleReadBindSecretIdResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bind_secret_id** | **bool** | Impose secret_id to be presented when logging in using this role. Defaults to &#39;true&#39;. | [optional] 

## Example

```python
from ahvac.models.app_role_read_bind_secret_id_response import AppRoleReadBindSecretIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AppRoleReadBindSecretIdResponse from a JSON string
app_role_read_bind_secret_id_response_instance = AppRoleReadBindSecretIdResponse.from_json(json)
# print the JSON string representation of the object
print(AppRoleReadBindSecretIdResponse.to_json())

# convert the object into a dict
app_role_read_bind_secret_id_response_dict = app_role_read_bind_secret_id_response_instance.to_dict()
# create an instance of AppRoleReadBindSecretIdResponse from a dict
app_role_read_bind_secret_id_response_from_dict = AppRoleReadBindSecretIdResponse.from_dict(app_role_read_bind_secret_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


