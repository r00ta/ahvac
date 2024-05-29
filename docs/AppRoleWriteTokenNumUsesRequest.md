# AppRoleWriteTokenNumUsesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_num_uses** | **int** | The maximum number of times a token may be used, a value of zero means unlimited | [optional] 

## Example

```python
from ahvac.models.app_role_write_token_num_uses_request import AppRoleWriteTokenNumUsesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppRoleWriteTokenNumUsesRequest from a JSON string
app_role_write_token_num_uses_request_instance = AppRoleWriteTokenNumUsesRequest.from_json(json)
# print the JSON string representation of the object
print(AppRoleWriteTokenNumUsesRequest.to_json())

# convert the object into a dict
app_role_write_token_num_uses_request_dict = app_role_write_token_num_uses_request_instance.to_dict()
# create an instance of AppRoleWriteTokenNumUsesRequest from a dict
app_role_write_token_num_uses_request_from_dict = AppRoleWriteTokenNumUsesRequest.from_dict(app_role_write_token_num_uses_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


