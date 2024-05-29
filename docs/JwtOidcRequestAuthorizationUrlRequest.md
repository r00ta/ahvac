# JwtOidcRequestAuthorizationUrlRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_nonce** | **str** | Optional client-provided nonce that must match during callback, if present. | [optional] 
**redirect_uri** | **str** | The OAuth redirect_uri to use in the authorization URL. | [optional] 
**role** | **str** | The role to issue an OIDC authorization URL against. | [optional] 

## Example

```python
from ahvac.models.jwt_oidc_request_authorization_url_request import JwtOidcRequestAuthorizationUrlRequest

# TODO update the JSON string below
json = "{}"
# create an instance of JwtOidcRequestAuthorizationUrlRequest from a JSON string
jwt_oidc_request_authorization_url_request_instance = JwtOidcRequestAuthorizationUrlRequest.from_json(json)
# print the JSON string representation of the object
print(JwtOidcRequestAuthorizationUrlRequest.to_json())

# convert the object into a dict
jwt_oidc_request_authorization_url_request_dict = jwt_oidc_request_authorization_url_request_instance.to_dict()
# create an instance of JwtOidcRequestAuthorizationUrlRequest from a dict
jwt_oidc_request_authorization_url_request_from_dict = JwtOidcRequestAuthorizationUrlRequest.from_dict(jwt_oidc_request_authorization_url_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


