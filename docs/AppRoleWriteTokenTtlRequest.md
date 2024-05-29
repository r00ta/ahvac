# AppRoleWriteTokenTtlRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_ttl** | **str** | The initial ttl of the token to generate | [optional] 

## Example

```python
from ahvac.models.app_role_write_token_ttl_request import AppRoleWriteTokenTtlRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppRoleWriteTokenTtlRequest from a JSON string
app_role_write_token_ttl_request_instance = AppRoleWriteTokenTtlRequest.from_json(json)
# print the JSON string representation of the object
print(AppRoleWriteTokenTtlRequest.to_json())

# convert the object into a dict
app_role_write_token_ttl_request_dict = app_role_write_token_ttl_request_instance.to_dict()
# create an instance of AppRoleWriteTokenTtlRequest from a dict
app_role_write_token_ttl_request_from_dict = AppRoleWriteTokenTtlRequest.from_dict(app_role_write_token_ttl_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


