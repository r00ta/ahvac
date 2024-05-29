# PkiIssuerSignSelfIssuedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate** | **str** | Certificate | [optional] 
**issuing_ca** | **str** | Issuing CA | [optional] 

## Example

```python
from ahvac.models.pki_issuer_sign_self_issued_response import PkiIssuerSignSelfIssuedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PkiIssuerSignSelfIssuedResponse from a JSON string
pki_issuer_sign_self_issued_response_instance = PkiIssuerSignSelfIssuedResponse.from_json(json)
# print the JSON string representation of the object
print(PkiIssuerSignSelfIssuedResponse.to_json())

# convert the object into a dict
pki_issuer_sign_self_issued_response_dict = pki_issuer_sign_self_issued_response_instance.to_dict()
# create an instance of PkiIssuerSignSelfIssuedResponse from a dict
pki_issuer_sign_self_issued_response_from_dict = PkiIssuerSignSelfIssuedResponse.from_dict(pki_issuer_sign_self_issued_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


