# PkiIssuerResignCrlsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crl** | **str** | CRL | [optional] 

## Example

```python
from ahvac.models.pki_issuer_resign_crls_response import PkiIssuerResignCrlsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PkiIssuerResignCrlsResponse from a JSON string
pki_issuer_resign_crls_response_instance = PkiIssuerResignCrlsResponse.from_json(json)
# print the JSON string representation of the object
print(PkiIssuerResignCrlsResponse.to_json())

# convert the object into a dict
pki_issuer_resign_crls_response_dict = pki_issuer_resign_crls_response_instance.to_dict()
# create an instance of PkiIssuerResignCrlsResponse from a dict
pki_issuer_resign_crls_response_from_dict = PkiIssuerResignCrlsResponse.from_dict(pki_issuer_resign_crls_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


