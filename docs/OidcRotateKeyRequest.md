# OidcRotateKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verification_ttl** | **str** | Controls how long the public portion of a key will be available for verification after being rotated. Setting verification_ttl here will override the verification_ttl set on the key. | [optional] 

## Example

```python
from ahvac.models.oidc_rotate_key_request import OidcRotateKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OidcRotateKeyRequest from a JSON string
oidc_rotate_key_request_instance = OidcRotateKeyRequest.from_json(json)
# print the JSON string representation of the object
print(OidcRotateKeyRequest.to_json())

# convert the object into a dict
oidc_rotate_key_request_dict = oidc_rotate_key_request_instance.to_dict()
# create an instance of OidcRotateKeyRequest from a dict
oidc_rotate_key_request_from_dict = OidcRotateKeyRequest.from_dict(oidc_rotate_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


