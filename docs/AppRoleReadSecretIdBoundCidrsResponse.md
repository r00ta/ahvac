# AppRoleReadSecretIdBoundCidrsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret_id_bound_cidrs** | **List[str]** | Comma separated string or list of CIDR blocks. If set, specifies the blocks of IP addresses which can perform the login operation. | [optional] 

## Example

```python
from ahvac.models.app_role_read_secret_id_bound_cidrs_response import AppRoleReadSecretIdBoundCidrsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AppRoleReadSecretIdBoundCidrsResponse from a JSON string
app_role_read_secret_id_bound_cidrs_response_instance = AppRoleReadSecretIdBoundCidrsResponse.from_json(json)
# print the JSON string representation of the object
print(AppRoleReadSecretIdBoundCidrsResponse.to_json())

# convert the object into a dict
app_role_read_secret_id_bound_cidrs_response_dict = app_role_read_secret_id_bound_cidrs_response_instance.to_dict()
# create an instance of AppRoleReadSecretIdBoundCidrsResponse from a dict
app_role_read_secret_id_bound_cidrs_response_from_dict = AppRoleReadSecretIdBoundCidrsResponse.from_dict(app_role_read_secret_id_bound_cidrs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


