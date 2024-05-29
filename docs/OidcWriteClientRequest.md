# OidcWriteClientRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token_ttl** | **str** | The time-to-live for access tokens obtained by the client. | [optional] [default to '24h']
**assignments** | **List[str]** | Comma separated string or array of assignment resources. | [optional] 
**client_type** | **str** | The client type based on its ability to maintain confidentiality of credentials. The following client types are supported: &#39;confidential&#39;, &#39;public&#39;. Defaults to &#39;confidential&#39;. | [optional] [default to 'confidential']
**id_token_ttl** | **str** | The time-to-live for ID tokens obtained by the client. | [optional] [default to '24h']
**key** | **str** | A reference to a named key resource. Cannot be modified after creation. Defaults to the &#39;default&#39; key. | [optional] [default to 'default']
**redirect_uris** | **List[str]** | Comma separated string or array of redirect URIs used by the client. One of these values must exactly match the redirect_uri parameter value used in each authentication request. | [optional] 

## Example

```python
from ahvac.models.oidc_write_client_request import OidcWriteClientRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OidcWriteClientRequest from a JSON string
oidc_write_client_request_instance = OidcWriteClientRequest.from_json(json)
# print the JSON string representation of the object
print(OidcWriteClientRequest.to_json())

# convert the object into a dict
oidc_write_client_request_dict = oidc_write_client_request_instance.to_dict()
# create an instance of OidcWriteClientRequest from a dict
oidc_write_client_request_from_dict = OidcWriteClientRequest.from_dict(oidc_write_client_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


