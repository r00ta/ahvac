# PkiIssuerSignVerbatimResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca_chain** | **List[str]** | Certificate Chain | [optional] 
**certificate** | **str** | Certificate | [optional] 
**expiration** | **int** | Time of expiration | [optional] 
**issuing_ca** | **str** | Issuing Certificate Authority | [optional] 
**serial_number** | **str** | Serial Number | [optional] 

## Example

```python
from ahvac.models.pki_issuer_sign_verbatim_response import PkiIssuerSignVerbatimResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PkiIssuerSignVerbatimResponse from a JSON string
pki_issuer_sign_verbatim_response_instance = PkiIssuerSignVerbatimResponse.from_json(json)
# print the JSON string representation of the object
print(PkiIssuerSignVerbatimResponse.to_json())

# convert the object into a dict
pki_issuer_sign_verbatim_response_dict = pki_issuer_sign_verbatim_response_instance.to_dict()
# create an instance of PkiIssuerSignVerbatimResponse from a dict
pki_issuer_sign_verbatim_response_from_dict = PkiIssuerSignVerbatimResponse.from_dict(pki_issuer_sign_verbatim_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


