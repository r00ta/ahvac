# PkiSetSignedIntermediateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate** | **str** | PEM-format certificate. This must be a CA certificate with a public key matching the previously-generated key from the generation endpoint. Additional parent CAs may be optionally appended to the bundle. | [optional] 

## Example

```python
from ahvac.models.pki_set_signed_intermediate_request import PkiSetSignedIntermediateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PkiSetSignedIntermediateRequest from a JSON string
pki_set_signed_intermediate_request_instance = PkiSetSignedIntermediateRequest.from_json(json)
# print the JSON string representation of the object
print(PkiSetSignedIntermediateRequest.to_json())

# convert the object into a dict
pki_set_signed_intermediate_request_dict = pki_set_signed_intermediate_request_instance.to_dict()
# create an instance of PkiSetSignedIntermediateRequest from a dict
pki_set_signed_intermediate_request_from_dict = PkiSetSignedIntermediateRequest.from_dict(pki_set_signed_intermediate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


