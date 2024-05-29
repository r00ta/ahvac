# PkiRevokeWithKeyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**revocation_time** | **int** | Revocation Time | [optional] 
**revocation_time_rfc3339** | **datetime** | Revocation Time | [optional] 
**state** | **str** | Revocation State | [optional] 

## Example

```python
from ahvac.models.pki_revoke_with_key_response import PkiRevokeWithKeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PkiRevokeWithKeyResponse from a JSON string
pki_revoke_with_key_response_instance = PkiRevokeWithKeyResponse.from_json(json)
# print the JSON string representation of the object
print(PkiRevokeWithKeyResponse.to_json())

# convert the object into a dict
pki_revoke_with_key_response_dict = pki_revoke_with_key_response_instance.to_dict()
# create an instance of PkiRevokeWithKeyResponse from a dict
pki_revoke_with_key_response_from_dict = PkiRevokeWithKeyResponse.from_dict(pki_revoke_with_key_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


