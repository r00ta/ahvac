# OidcWriteRoleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | Optional client_id | [optional] 
**key** | **str** | The OIDC key to use for generating tokens. The specified key must already exist. | 
**template** | **str** | The template string to use for generating tokens. This may be in string-ified JSON or base64 format. | [optional] 
**ttl** | **str** | TTL of the tokens generated against the role. | [optional] [default to '24h']

## Example

```python
from ahvac.models.oidc_write_role_request import OidcWriteRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OidcWriteRoleRequest from a JSON string
oidc_write_role_request_instance = OidcWriteRoleRequest.from_json(json)
# print the JSON string representation of the object
print(OidcWriteRoleRequest.to_json())

# convert the object into a dict
oidc_write_role_request_dict = oidc_write_role_request_instance.to_dict()
# create an instance of OidcWriteRoleRequest from a dict
oidc_write_role_request_from_dict = OidcWriteRoleRequest.from_dict(oidc_write_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


