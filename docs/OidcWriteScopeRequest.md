# OidcWriteScopeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The description of the scope | [optional] 
**template** | **str** | The template string to use for the scope. This may be in string-ified JSON or base64 format. | [optional] 

## Example

```python
from ahvac.models.oidc_write_scope_request import OidcWriteScopeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OidcWriteScopeRequest from a JSON string
oidc_write_scope_request_instance = OidcWriteScopeRequest.from_json(json)
# print the JSON string representation of the object
print(OidcWriteScopeRequest.to_json())

# convert the object into a dict
oidc_write_scope_request_dict = oidc_write_scope_request_instance.to_dict()
# create an instance of OidcWriteScopeRequest from a dict
oidc_write_scope_request_from_dict = OidcWriteScopeRequest.from_dict(oidc_write_scope_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


