# AppRoleLookUpSecretIdByAccessorRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret_id_accessor** | **str** | Accessor of the SecretID | [optional] 

## Example

```python
from ahvac.models.app_role_look_up_secret_id_by_accessor_request import AppRoleLookUpSecretIdByAccessorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppRoleLookUpSecretIdByAccessorRequest from a JSON string
app_role_look_up_secret_id_by_accessor_request_instance = AppRoleLookUpSecretIdByAccessorRequest.from_json(json)
# print the JSON string representation of the object
print(AppRoleLookUpSecretIdByAccessorRequest.to_json())

# convert the object into a dict
app_role_look_up_secret_id_by_accessor_request_dict = app_role_look_up_secret_id_by_accessor_request_instance.to_dict()
# create an instance of AppRoleLookUpSecretIdByAccessorRequest from a dict
app_role_look_up_secret_id_by_accessor_request_from_dict = AppRoleLookUpSecretIdByAccessorRequest.from_dict(app_role_look_up_secret_id_by_accessor_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


