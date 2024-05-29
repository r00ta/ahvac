# AppRoleWriteBoundCidrListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bound_cidr_list** | **List[str]** | Deprecated: Please use \&quot;secret_id_bound_cidrs\&quot; instead. Comma separated string or list of CIDR blocks. If set, specifies the blocks of IP addresses which can perform the login operation. | [optional] 

## Example

```python
from ahvac.models.app_role_write_bound_cidr_list_request import AppRoleWriteBoundCidrListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppRoleWriteBoundCidrListRequest from a JSON string
app_role_write_bound_cidr_list_request_instance = AppRoleWriteBoundCidrListRequest.from_json(json)
# print the JSON string representation of the object
print(AppRoleWriteBoundCidrListRequest.to_json())

# convert the object into a dict
app_role_write_bound_cidr_list_request_dict = app_role_write_bound_cidr_list_request_instance.to_dict()
# create an instance of AppRoleWriteBoundCidrListRequest from a dict
app_role_write_bound_cidr_list_request_from_dict = AppRoleWriteBoundCidrListRequest.from_dict(app_role_write_bound_cidr_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


