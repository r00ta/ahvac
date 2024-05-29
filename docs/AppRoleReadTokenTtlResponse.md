# AppRoleReadTokenTtlResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_ttl** | **str** | The initial ttl of the token to generate | [optional] 

## Example

```python
from ahvac.models.app_role_read_token_ttl_response import AppRoleReadTokenTtlResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AppRoleReadTokenTtlResponse from a JSON string
app_role_read_token_ttl_response_instance = AppRoleReadTokenTtlResponse.from_json(json)
# print the JSON string representation of the object
print(AppRoleReadTokenTtlResponse.to_json())

# convert the object into a dict
app_role_read_token_ttl_response_dict = app_role_read_token_ttl_response_instance.to_dict()
# create an instance of AppRoleReadTokenTtlResponse from a dict
app_role_read_token_ttl_response_from_dict = AppRoleReadTokenTtlResponse.from_dict(app_role_read_token_ttl_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


