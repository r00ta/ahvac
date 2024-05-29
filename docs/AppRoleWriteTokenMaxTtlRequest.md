# AppRoleWriteTokenMaxTtlRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_max_ttl** | **str** | The maximum lifetime of the generated token | [optional] 

## Example

```python
from ahvac.models.app_role_write_token_max_ttl_request import AppRoleWriteTokenMaxTtlRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppRoleWriteTokenMaxTtlRequest from a JSON string
app_role_write_token_max_ttl_request_instance = AppRoleWriteTokenMaxTtlRequest.from_json(json)
# print the JSON string representation of the object
print(AppRoleWriteTokenMaxTtlRequest.to_json())

# convert the object into a dict
app_role_write_token_max_ttl_request_dict = app_role_write_token_max_ttl_request_instance.to_dict()
# create an instance of AppRoleWriteTokenMaxTtlRequest from a dict
app_role_write_token_max_ttl_request_from_dict = AppRoleWriteTokenMaxTtlRequest.from_dict(app_role_write_token_max_ttl_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


