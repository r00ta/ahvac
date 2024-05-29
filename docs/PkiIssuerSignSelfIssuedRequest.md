# PkiIssuerSignSelfIssuedRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate** | **str** | PEM-format self-issued certificate to be signed. | [optional] 
**require_matching_certificate_algorithms** | **bool** | If true, require the public key algorithm of the signer to match that of the self issued certificate. | [optional] [default to False]

## Example

```python
from ahvac.models.pki_issuer_sign_self_issued_request import PkiIssuerSignSelfIssuedRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PkiIssuerSignSelfIssuedRequest from a JSON string
pki_issuer_sign_self_issued_request_instance = PkiIssuerSignSelfIssuedRequest.from_json(json)
# print the JSON string representation of the object
print(PkiIssuerSignSelfIssuedRequest.to_json())

# convert the object into a dict
pki_issuer_sign_self_issued_request_dict = pki_issuer_sign_self_issued_request_instance.to_dict()
# create an instance of PkiIssuerSignSelfIssuedRequest from a dict
pki_issuer_sign_self_issued_request_from_dict = PkiIssuerSignSelfIssuedRequest.from_dict(pki_issuer_sign_self_issued_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


