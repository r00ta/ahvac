# AppRoleReadLocalSecretIdsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local_secret_ids** | **bool** | If true, the secret identifiers generated using this role will be cluster local. This can only be set during role creation and once set, it can&#39;t be reset later | [optional] 

## Example

```python
from ahvac.models.app_role_read_local_secret_ids_response import AppRoleReadLocalSecretIdsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AppRoleReadLocalSecretIdsResponse from a JSON string
app_role_read_local_secret_ids_response_instance = AppRoleReadLocalSecretIdsResponse.from_json(json)
# print the JSON string representation of the object
print(AppRoleReadLocalSecretIdsResponse.to_json())

# convert the object into a dict
app_role_read_local_secret_ids_response_dict = app_role_read_local_secret_ids_response_instance.to_dict()
# create an instance of AppRoleReadLocalSecretIdsResponse from a dict
app_role_read_local_secret_ids_response_from_dict = AppRoleReadLocalSecretIdsResponse.from_dict(app_role_read_local_secret_ids_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


