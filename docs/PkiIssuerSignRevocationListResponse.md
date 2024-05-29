# PkiIssuerSignRevocationListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crl** | **str** | CRL | [optional] 

## Example

```python
from ahvac.models.pki_issuer_sign_revocation_list_response import PkiIssuerSignRevocationListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PkiIssuerSignRevocationListResponse from a JSON string
pki_issuer_sign_revocation_list_response_instance = PkiIssuerSignRevocationListResponse.from_json(json)
# print the JSON string representation of the object
print(PkiIssuerSignRevocationListResponse.to_json())

# convert the object into a dict
pki_issuer_sign_revocation_list_response_dict = pki_issuer_sign_revocation_list_response_instance.to_dict()
# create an instance of PkiIssuerSignRevocationListResponse from a dict
pki_issuer_sign_revocation_list_response_from_dict = PkiIssuerSignRevocationListResponse.from_dict(pki_issuer_sign_revocation_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


