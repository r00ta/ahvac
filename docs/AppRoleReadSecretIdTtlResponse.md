# AppRoleReadSecretIdTtlResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret_id_ttl** | **str** | Duration in seconds after which the issued secret ID should expire. Defaults to 0, meaning no expiration. | [optional] 

## Example

```python
from ahvac.models.app_role_read_secret_id_ttl_response import AppRoleReadSecretIdTtlResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AppRoleReadSecretIdTtlResponse from a JSON string
app_role_read_secret_id_ttl_response_instance = AppRoleReadSecretIdTtlResponse.from_json(json)
# print the JSON string representation of the object
print(AppRoleReadSecretIdTtlResponse.to_json())

# convert the object into a dict
app_role_read_secret_id_ttl_response_dict = app_role_read_secret_id_ttl_response_instance.to_dict()
# create an instance of AppRoleReadSecretIdTtlResponse from a dict
app_role_read_secret_id_ttl_response_from_dict = AppRoleReadSecretIdTtlResponse.from_dict(app_role_read_secret_id_ttl_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


