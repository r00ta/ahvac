# AppRoleReadTokenNumUsesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_num_uses** | **int** | The maximum number of times a token may be used, a value of zero means unlimited | [optional] 

## Example

```python
from ahvac.models.app_role_read_token_num_uses_response import AppRoleReadTokenNumUsesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AppRoleReadTokenNumUsesResponse from a JSON string
app_role_read_token_num_uses_response_instance = AppRoleReadTokenNumUsesResponse.from_json(json)
# print the JSON string representation of the object
print(AppRoleReadTokenNumUsesResponse.to_json())

# convert the object into a dict
app_role_read_token_num_uses_response_dict = app_role_read_token_num_uses_response_instance.to_dict()
# create an instance of AppRoleReadTokenNumUsesResponse from a dict
app_role_read_token_num_uses_response_from_dict = AppRoleReadTokenNumUsesResponse.from_dict(app_role_read_token_num_uses_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


