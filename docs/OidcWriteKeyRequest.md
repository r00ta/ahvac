# OidcWriteKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | **str** | Signing algorithm to use. This will default to RS256. | [optional] [default to 'RS256']
**allowed_client_ids** | **List[str]** | Comma separated string or array of role client ids allowed to use this key for signing. If empty no roles are allowed. If \&quot;*\&quot; all roles are allowed. | [optional] 
**rotation_period** | **str** | How often to generate a new keypair. | [optional] [default to '24h']
**verification_ttl** | **str** | Controls how long the public portion of a key will be available for verification after being rotated. | [optional] [default to '24h']

## Example

```python
from ahvac.models.oidc_write_key_request import OidcWriteKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OidcWriteKeyRequest from a JSON string
oidc_write_key_request_instance = OidcWriteKeyRequest.from_json(json)
# print the JSON string representation of the object
print(OidcWriteKeyRequest.to_json())

# convert the object into a dict
oidc_write_key_request_dict = oidc_write_key_request_instance.to_dict()
# create an instance of OidcWriteKeyRequest from a dict
oidc_write_key_request_from_dict = OidcWriteKeyRequest.from_dict(oidc_write_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


