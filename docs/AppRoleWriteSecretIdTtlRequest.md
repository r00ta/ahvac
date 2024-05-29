# AppRoleWriteSecretIdTtlRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret_id_ttl** | **str** | Duration in seconds after which the issued SecretID should expire. Defaults to 0, meaning no expiration. | [optional] 

## Example

```python
from ahvac.models.app_role_write_secret_id_ttl_request import AppRoleWriteSecretIdTtlRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppRoleWriteSecretIdTtlRequest from a JSON string
app_role_write_secret_id_ttl_request_instance = AppRoleWriteSecretIdTtlRequest.from_json(json)
# print the JSON string representation of the object
print(AppRoleWriteSecretIdTtlRequest.to_json())

# convert the object into a dict
app_role_write_secret_id_ttl_request_dict = app_role_write_secret_id_ttl_request_instance.to_dict()
# create an instance of AppRoleWriteSecretIdTtlRequest from a dict
app_role_write_secret_id_ttl_request_from_dict = AppRoleWriteSecretIdTtlRequest.from_dict(app_role_write_secret_id_ttl_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


