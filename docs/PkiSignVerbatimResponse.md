# PkiSignVerbatimResponse


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
from ahvac.models.pki_sign_verbatim_response import PkiSignVerbatimResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PkiSignVerbatimResponse from a JSON string
pki_sign_verbatim_response_instance = PkiSignVerbatimResponse.from_json(json)
# print the JSON string representation of the object
print(PkiSignVerbatimResponse.to_json())

# convert the object into a dict
pki_sign_verbatim_response_dict = pki_sign_verbatim_response_instance.to_dict()
# create an instance of PkiSignVerbatimResponse from a dict
pki_sign_verbatim_response_from_dict = PkiSignVerbatimResponse.from_dict(pki_sign_verbatim_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


