# AppRoleWriteTokenBoundCidrsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_bound_cidrs** | **List[str]** | Comma separated string or JSON list of CIDR blocks. If set, specifies the blocks of IP addresses which are allowed to use the generated token. | [optional] 

## Example

```python
from ahvac.models.app_role_write_token_bound_cidrs_request import AppRoleWriteTokenBoundCidrsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppRoleWriteTokenBoundCidrsRequest from a JSON string
app_role_write_token_bound_cidrs_request_instance = AppRoleWriteTokenBoundCidrsRequest.from_json(json)
# print the JSON string representation of the object
print(AppRoleWriteTokenBoundCidrsRequest.to_json())

# convert the object into a dict
app_role_write_token_bound_cidrs_request_dict = app_role_write_token_bound_cidrs_request_instance.to_dict()
# create an instance of AppRoleWriteTokenBoundCidrsRequest from a dict
app_role_write_token_bound_cidrs_request_from_dict = AppRoleWriteTokenBoundCidrsRequest.from_dict(app_role_write_token_bound_cidrs_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


