# AppRoleWriteSecretIdResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret_id** | **str** | Secret ID attached to the role. | [optional] 
**secret_id_accessor** | **str** | Accessor of the secret ID | [optional] 
**secret_id_num_uses** | **int** | Number of times a secret ID can access the role, after which the secret ID will expire. | [optional] 
**secret_id_ttl** | **str** | Duration in seconds after which the issued secret ID expires. | [optional] 

## Example

```python
from ahvac.models.app_role_write_secret_id_response import AppRoleWriteSecretIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AppRoleWriteSecretIdResponse from a JSON string
app_role_write_secret_id_response_instance = AppRoleWriteSecretIdResponse.from_json(json)
# print the JSON string representation of the object
print(AppRoleWriteSecretIdResponse.to_json())

# convert the object into a dict
app_role_write_secret_id_response_dict = app_role_write_secret_id_response_instance.to_dict()
# create an instance of AppRoleWriteSecretIdResponse from a dict
app_role_write_secret_id_response_from_dict = AppRoleWriteSecretIdResponse.from_dict(app_role_write_secret_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


