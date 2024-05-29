# OidcWriteProviderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_client_ids** | **List[str]** | The client IDs that are permitted to use the provider | [optional] 
**issuer** | **str** | Specifies what will be used for the iss claim of ID tokens. | [optional] 
**scopes_supported** | **List[str]** | The scopes supported for requesting on the provider | [optional] 

## Example

```python
from ahvac.models.oidc_write_provider_request import OidcWriteProviderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OidcWriteProviderRequest from a JSON string
oidc_write_provider_request_instance = OidcWriteProviderRequest.from_json(json)
# print the JSON string representation of the object
print(OidcWriteProviderRequest.to_json())

# convert the object into a dict
oidc_write_provider_request_dict = oidc_write_provider_request_instance.to_dict()
# create an instance of OidcWriteProviderRequest from a dict
oidc_write_provider_request_from_dict = OidcWriteProviderRequest.from_dict(oidc_write_provider_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


