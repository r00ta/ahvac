# AppRoleReadBoundCidrListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bound_cidr_list** | **List[str]** | Deprecated: Please use \&quot;secret_id_bound_cidrs\&quot; instead. Comma separated string or list of CIDR blocks. If set, specifies the blocks of IP addresses which can perform the login operation. | [optional] 

## Example

```python
from ahvac.models.app_role_read_bound_cidr_list_response import AppRoleReadBoundCidrListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AppRoleReadBoundCidrListResponse from a JSON string
app_role_read_bound_cidr_list_response_instance = AppRoleReadBoundCidrListResponse.from_json(json)
# print the JSON string representation of the object
print(AppRoleReadBoundCidrListResponse.to_json())

# convert the object into a dict
app_role_read_bound_cidr_list_response_dict = app_role_read_bound_cidr_list_response_instance.to_dict()
# create an instance of AppRoleReadBoundCidrListResponse from a dict
app_role_read_bound_cidr_list_response_from_dict = AppRoleReadBoundCidrListResponse.from_dict(app_role_read_bound_cidr_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


