# OidcConfigureRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issuer** | **str** | Issuer URL to be used in the iss claim of the token. If not set, Vault&#39;s app_addr will be used. | [optional] 

## Example

```python
from ahvac.models.oidc_configure_request import OidcConfigureRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OidcConfigureRequest from a JSON string
oidc_configure_request_instance = OidcConfigureRequest.from_json(json)
# print the JSON string representation of the object
print(OidcConfigureRequest.to_json())

# convert the object into a dict
oidc_configure_request_dict = oidc_configure_request_instance.to_dict()
# create an instance of OidcConfigureRequest from a dict
oidc_configure_request_from_dict = OidcConfigureRequest.from_dict(oidc_configure_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


