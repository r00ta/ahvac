# AppRoleReadSecretIdNumUsesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret_id_num_uses** | **int** | Number of times a secret ID can access the role, after which the SecretID will expire. Defaults to 0 meaning that the secret ID is of unlimited use. | [optional] 

## Example

```python
from ahvac.models.app_role_read_secret_id_num_uses_response import AppRoleReadSecretIdNumUsesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AppRoleReadSecretIdNumUsesResponse from a JSON string
app_role_read_secret_id_num_uses_response_instance = AppRoleReadSecretIdNumUsesResponse.from_json(json)
# print the JSON string representation of the object
print(AppRoleReadSecretIdNumUsesResponse.to_json())

# convert the object into a dict
app_role_read_secret_id_num_uses_response_dict = app_role_read_secret_id_num_uses_response_instance.to_dict()
# create an instance of AppRoleReadSecretIdNumUsesResponse from a dict
app_role_read_secret_id_num_uses_response_from_dict = AppRoleReadSecretIdNumUsesResponse.from_dict(app_role_read_secret_id_num_uses_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


