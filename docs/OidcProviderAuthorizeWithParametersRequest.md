# OidcProviderAuthorizeWithParametersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | The ID of the requesting client. | 
**code_challenge** | **str** | The code challenge derived from the code verifier. | [optional] 
**code_challenge_method** | **str** | The method that was used to derive the code challenge. The following methods are supported: &#39;S256&#39;, &#39;plain&#39;. Defaults to &#39;plain&#39;. | [optional] [default to 'plain']
**max_age** | **int** | The allowable elapsed time in seconds since the last time the end-user was actively authenticated. | [optional] 
**nonce** | **str** | The value that will be returned in the ID token nonce claim after a token exchange. | [optional] 
**redirect_uri** | **str** | The redirection URI to which the response will be sent. | 
**response_type** | **str** | The OIDC authentication flow to be used. The following response types are supported: &#39;code&#39; | 
**scope** | **str** | A space-delimited, case-sensitive list of scopes to be requested. The &#39;openid&#39; scope is required. | 
**state** | **str** | The value used to maintain state between the authentication request and client. | [optional] 

## Example

```python
from ahvac.models.oidc_provider_authorize_with_parameters_request import OidcProviderAuthorizeWithParametersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OidcProviderAuthorizeWithParametersRequest from a JSON string
oidc_provider_authorize_with_parameters_request_instance = OidcProviderAuthorizeWithParametersRequest.from_json(json)
# print the JSON string representation of the object
print(OidcProviderAuthorizeWithParametersRequest.to_json())

# convert the object into a dict
oidc_provider_authorize_with_parameters_request_dict = oidc_provider_authorize_with_parameters_request_instance.to_dict()
# create an instance of OidcProviderAuthorizeWithParametersRequest from a dict
oidc_provider_authorize_with_parameters_request_from_dict = OidcProviderAuthorizeWithParametersRequest.from_dict(oidc_provider_authorize_with_parameters_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


