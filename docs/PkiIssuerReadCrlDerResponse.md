# PkiIssuerReadCrlDerResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crl** | **str** |  | [optional] 

## Example

```python
from ahvac.models.pki_issuer_read_crl_der_response import PkiIssuerReadCrlDerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PkiIssuerReadCrlDerResponse from a JSON string
pki_issuer_read_crl_der_response_instance = PkiIssuerReadCrlDerResponse.from_json(json)
# print the JSON string representation of the object
print(PkiIssuerReadCrlDerResponse.to_json())

# convert the object into a dict
pki_issuer_read_crl_der_response_dict = pki_issuer_read_crl_der_response_instance.to_dict()
# create an instance of PkiIssuerReadCrlDerResponse from a dict
pki_issuer_read_crl_der_response_from_dict = PkiIssuerReadCrlDerResponse.from_dict(pki_issuer_read_crl_der_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


