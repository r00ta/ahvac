# AppRoleWriteSecretIdNumUsesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret_id_num_uses** | **int** | Number of times a SecretID can access the role, after which the SecretID will expire. | [optional] 

## Example

```python
from ahvac.models.app_role_write_secret_id_num_uses_request import AppRoleWriteSecretIdNumUsesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppRoleWriteSecretIdNumUsesRequest from a JSON string
app_role_write_secret_id_num_uses_request_instance = AppRoleWriteSecretIdNumUsesRequest.from_json(json)
# print the JSON string representation of the object
print(AppRoleWriteSecretIdNumUsesRequest.to_json())

# convert the object into a dict
app_role_write_secret_id_num_uses_request_dict = app_role_write_secret_id_num_uses_request_instance.to_dict()
# create an instance of AppRoleWriteSecretIdNumUsesRequest from a dict
app_role_write_secret_id_num_uses_request_from_dict = AppRoleWriteSecretIdNumUsesRequest.from_dict(app_role_write_secret_id_num_uses_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


