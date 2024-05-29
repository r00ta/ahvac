# AppRoleWriteSecretIdBoundCidrsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret_id_bound_cidrs** | **List[str]** | Comma separated string or list of CIDR blocks. If set, specifies the blocks of IP addresses which can perform the login operation. | [optional] 

## Example

```python
from ahvac.models.app_role_write_secret_id_bound_cidrs_request import AppRoleWriteSecretIdBoundCidrsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppRoleWriteSecretIdBoundCidrsRequest from a JSON string
app_role_write_secret_id_bound_cidrs_request_instance = AppRoleWriteSecretIdBoundCidrsRequest.from_json(json)
# print the JSON string representation of the object
print(AppRoleWriteSecretIdBoundCidrsRequest.to_json())

# convert the object into a dict
app_role_write_secret_id_bound_cidrs_request_dict = app_role_write_secret_id_bound_cidrs_request_instance.to_dict()
# create an instance of AppRoleWriteSecretIdBoundCidrsRequest from a dict
app_role_write_secret_id_bound_cidrs_request_from_dict = AppRoleWriteSecretIdBoundCidrsRequest.from_dict(app_role_write_secret_id_bound_cidrs_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


