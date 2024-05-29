# JwtConfigureRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bound_issuer** | **str** | The value against which to match the &#39;iss&#39; claim in a JWT. Optional. | [optional] 
**default_role** | **str** | The default role to use if none is provided during login. If not set, a role is required during login. | [optional] 
**jwks_ca_pem** | **str** | The CA certificate or chain of certificates, in PEM format, to use to validate connections to the JWKS URL. If not set, system certificates are used. | [optional] 
**jwks_url** | **str** | JWKS URL to use to authenticate signatures. Cannot be used with \&quot;oidc_discovery_url\&quot; or \&quot;jwt_validation_pubkeys\&quot;. | [optional] 
**jwt_supported_algs** | **List[str]** | A list of supported signing algorithms. Defaults to RS256. | [optional] 
**jwt_validation_pubkeys** | **List[str]** | A list of PEM-encoded public keys to use to authenticate signatures locally. Cannot be used with \&quot;jwks_url\&quot; or \&quot;oidc_discovery_url\&quot;. | [optional] 
**namespace_in_state** | **bool** | Pass namespace in the OIDC state parameter instead of as a separate query parameter. With this setting, the allowed redirect URL(s) in Vault and on the provider side should not contain a namespace query parameter. This means only one redirect URL entry needs to be maintained on the provider side for all vault namespaces that will be authenticating against it. Defaults to true for new configs. | [optional] 
**oidc_client_id** | **str** | The OAuth Client ID configured with your OIDC provider. | [optional] 
**oidc_client_secret** | **str** | The OAuth Client Secret configured with your OIDC provider. | [optional] 
**oidc_discovery_ca_pem** | **str** | The CA certificate or chain of certificates, in PEM format, to use to validate connections to the OIDC Discovery URL. If not set, system certificates are used. | [optional] 
**oidc_discovery_url** | **str** | OIDC Discovery URL, without any .well-known component (base path). Cannot be used with \&quot;jwks_url\&quot; or \&quot;jwt_validation_pubkeys\&quot;. | [optional] 
**oidc_response_mode** | **str** | The response mode to be used in the OAuth2 request. Allowed values are &#39;query&#39; and &#39;form_post&#39;. | [optional] 
**oidc_response_types** | **List[str]** | The response types to request. Allowed values are &#39;code&#39; and &#39;id_token&#39;. Defaults to &#39;code&#39;. | [optional] 
**provider_config** | **object** | Provider-specific configuration. Optional. | [optional] 

## Example

```python
from ahvac.models.jwt_configure_request import JwtConfigureRequest

# TODO update the JSON string below
json = "{}"
# create an instance of JwtConfigureRequest from a JSON string
jwt_configure_request_instance = JwtConfigureRequest.from_json(json)
# print the JSON string representation of the object
print(JwtConfigureRequest.to_json())

# convert the object into a dict
jwt_configure_request_dict = jwt_configure_request_instance.to_dict()
# create an instance of JwtConfigureRequest from a dict
jwt_configure_request_from_dict = JwtConfigureRequest.from_dict(jwt_configure_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


