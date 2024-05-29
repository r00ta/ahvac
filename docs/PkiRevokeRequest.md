# PkiRevokeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate** | **str** | Certificate to revoke in PEM format; must be signed by an issuer in this mount. | [optional] 
**serial_number** | **str** | Certificate serial number, in colon- or hyphen-separated octal | [optional] 

## Example

```python
from ahvac.models.pki_revoke_request import PkiRevokeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PkiRevokeRequest from a JSON string
pki_revoke_request_instance = PkiRevokeRequest.from_json(json)
# print the JSON string representation of the object
print(PkiRevokeRequest.to_json())

# convert the object into a dict
pki_revoke_request_dict = pki_revoke_request_instance.to_dict()
# create an instance of PkiRevokeRequest from a dict
pki_revoke_request_from_dict = PkiRevokeRequest.from_dict(pki_revoke_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


