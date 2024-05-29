# PkiIssuerReadCrlResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crl** | **str** |  | [optional] 

## Example

```python
from ahvac.models.pki_issuer_read_crl_response import PkiIssuerReadCrlResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PkiIssuerReadCrlResponse from a JSON string
pki_issuer_read_crl_response_instance = PkiIssuerReadCrlResponse.from_json(json)
# print the JSON string representation of the object
print(PkiIssuerReadCrlResponse.to_json())

# convert the object into a dict
pki_issuer_read_crl_response_dict = pki_issuer_read_crl_response_instance.to_dict()
# create an instance of PkiIssuerReadCrlResponse from a dict
pki_issuer_read_crl_response_from_dict = PkiIssuerReadCrlResponse.from_dict(pki_issuer_read_crl_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


