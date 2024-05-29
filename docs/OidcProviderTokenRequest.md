# OidcProviderTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | The ID of the requesting client. | [optional] 
**client_secret** | **str** | The secret of the requesting client. | [optional] 
**code** | **str** | The authorization code received from the provider&#39;s authorization endpoint. | 
**code_verifier** | **str** | The code verifier associated with the authorization code. | [optional] 
**grant_type** | **str** | The authorization grant type. The following grant types are supported: &#39;authorization_code&#39;. | 
**redirect_uri** | **str** | The callback location where the authentication response was sent. | 

## Example

```python
from ahvac.models.oidc_provider_token_request import OidcProviderTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OidcProviderTokenRequest from a JSON string
oidc_provider_token_request_instance = OidcProviderTokenRequest.from_json(json)
# print the JSON string representation of the object
print(OidcProviderTokenRequest.to_json())

# convert the object into a dict
oidc_provider_token_request_dict = oidc_provider_token_request_instance.to_dict()
# create an instance of OidcProviderTokenRequest from a dict
oidc_provider_token_request_from_dict = OidcProviderTokenRequest.from_dict(oidc_provider_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


