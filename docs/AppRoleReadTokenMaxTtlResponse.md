# AppRoleReadTokenMaxTtlResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_max_ttl** | **str** | The maximum lifetime of the generated token | [optional] 

## Example

```python
from ahvac.models.app_role_read_token_max_ttl_response import AppRoleReadTokenMaxTtlResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AppRoleReadTokenMaxTtlResponse from a JSON string
app_role_read_token_max_ttl_response_instance = AppRoleReadTokenMaxTtlResponse.from_json(json)
# print the JSON string representation of the object
print(AppRoleReadTokenMaxTtlResponse.to_json())

# convert the object into a dict
app_role_read_token_max_ttl_response_dict = app_role_read_token_max_ttl_response_instance.to_dict()
# create an instance of AppRoleReadTokenMaxTtlResponse from a dict
app_role_read_token_max_ttl_response_from_dict = AppRoleReadTokenMaxTtlResponse.from_dict(app_role_read_token_max_ttl_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


