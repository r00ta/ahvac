# AppRoleDestroySecretIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret_id** | **str** | SecretID attached to the role. | [optional] 

## Example

```python
from ahvac.models.app_role_destroy_secret_id_request import AppRoleDestroySecretIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppRoleDestroySecretIdRequest from a JSON string
app_role_destroy_secret_id_request_instance = AppRoleDestroySecretIdRequest.from_json(json)
# print the JSON string representation of the object
print(AppRoleDestroySecretIdRequest.to_json())

# convert the object into a dict
app_role_destroy_secret_id_request_dict = app_role_destroy_secret_id_request_instance.to_dict()
# create an instance of AppRoleDestroySecretIdRequest from a dict
app_role_destroy_secret_id_request_from_dict = AppRoleDestroySecretIdRequest.from_dict(app_role_destroy_secret_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


