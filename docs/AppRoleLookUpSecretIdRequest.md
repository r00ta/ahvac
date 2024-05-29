# AppRoleLookUpSecretIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret_id** | **str** | SecretID attached to the role. | [optional] 

## Example

```python
from ahvac.models.app_role_look_up_secret_id_request import AppRoleLookUpSecretIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppRoleLookUpSecretIdRequest from a JSON string
app_role_look_up_secret_id_request_instance = AppRoleLookUpSecretIdRequest.from_json(json)
# print the JSON string representation of the object
print(AppRoleLookUpSecretIdRequest.to_json())

# convert the object into a dict
app_role_look_up_secret_id_request_dict = app_role_look_up_secret_id_request_instance.to_dict()
# create an instance of AppRoleLookUpSecretIdRequest from a dict
app_role_look_up_secret_id_request_from_dict = AppRoleLookUpSecretIdRequest.from_dict(app_role_look_up_secret_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


