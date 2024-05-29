# PkiReadCaDerResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca_chain** | **str** | Issuing CA Chain | [optional] 
**certificate** | **str** | Certificate | [optional] 
**issuer_id** | **str** | ID of the issuer | [optional] 
**revocation_time** | **int** | Revocation time | [optional] 
**revocation_time_rfc3339** | **str** | Revocation time RFC 3339 formatted | [optional] 

## Example

```python
from ahvac.models.pki_read_ca_der_response import PkiReadCaDerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PkiReadCaDerResponse from a JSON string
pki_read_ca_der_response_instance = PkiReadCaDerResponse.from_json(json)
# print the JSON string representation of the object
print(PkiReadCaDerResponse.to_json())

# convert the object into a dict
pki_read_ca_der_response_dict = pki_read_ca_der_response_instance.to_dict()
# create an instance of PkiReadCaDerResponse from a dict
pki_read_ca_der_response_from_dict = PkiReadCaDerResponse.from_dict(pki_read_ca_der_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

