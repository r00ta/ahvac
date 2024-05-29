# AppRoleReadTokenBoundCidrsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_bound_cidrs** | **List[str]** | Comma separated string or list of CIDR blocks. If set, specifies the blocks of IP addresses which can use the returned token. Should be a subset of the token CIDR blocks listed on the role, if any. | [optional] 

## Example

```python
from ahvac.models.app_role_read_token_bound_cidrs_response import AppRoleReadTokenBoundCidrsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AppRoleReadTokenBoundCidrsResponse from a JSON string
app_role_read_token_bound_cidrs_response_instance = AppRoleReadTokenBoundCidrsResponse.from_json(json)
# print the JSON string representation of the object
print(AppRoleReadTokenBoundCidrsResponse.to_json())

# convert the object into a dict
app_role_read_token_bound_cidrs_response_dict = app_role_read_token_bound_cidrs_response_instance.to_dict()
# create an instance of AppRoleReadTokenBoundCidrsResponse from a dict
app_role_read_token_bound_cidrs_response_from_dict = AppRoleReadTokenBoundCidrsResponse.from_dict(app_role_read_token_bound_cidrs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


