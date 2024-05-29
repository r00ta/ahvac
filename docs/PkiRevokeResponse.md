# PkiRevokeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**revocation_time** | **int** | Revocation Time | [optional] 
**revocation_time_rfc3339** | **datetime** | Revocation Time | [optional] 
**state** | **str** | Revocation State | [optional] 

## Example

```python
from ahvac.models.pki_revoke_response import PkiRevokeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PkiRevokeResponse from a JSON string
pki_revoke_response_instance = PkiRevokeResponse.from_json(json)
# print the JSON string representation of the object
print(PkiRevokeResponse.to_json())

# convert the object into a dict
pki_revoke_response_dict = pki_revoke_response_instance.to_dict()
# create an instance of PkiRevokeResponse from a dict
pki_revoke_response_from_dict = PkiRevokeResponse.from_dict(pki_revoke_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


