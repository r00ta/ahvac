# PkiRootSignSelfIssuedRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate** | **str** | PEM-format self-issued certificate to be signed. | [optional] 
**issuer_ref** | **str** | Reference to a existing issuer; either \&quot;default\&quot; for the configured default issuer, an identifier or the name assigned to the issuer. | [optional] [default to 'default']
**require_matching_certificate_algorithms** | **bool** | If true, require the public key algorithm of the signer to match that of the self issued certificate. | [optional] [default to False]

## Example

```python
from ahvac.models.pki_root_sign_self_issued_request import PkiRootSignSelfIssuedRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PkiRootSignSelfIssuedRequest from a JSON string
pki_root_sign_self_issued_request_instance = PkiRootSignSelfIssuedRequest.from_json(json)
# print the JSON string representation of the object
print(PkiRootSignSelfIssuedRequest.to_json())

# convert the object into a dict
pki_root_sign_self_issued_request_dict = pki_root_sign_self_issued_request_instance.to_dict()
# create an instance of PkiRootSignSelfIssuedRequest from a dict
pki_root_sign_self_issued_request_from_dict = PkiRootSignSelfIssuedRequest.from_dict(pki_root_sign_self_issued_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


