# PkiRootSignIntermediateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca_chain** | **List[str]** | CA Chain | [optional] 
**certificate** | **str** | Certificate | [optional] 
**expiration** | **int** | Expiration Time | [optional] 
**issuing_ca** | **str** | Issuing CA | [optional] 
**serial_number** | **str** | Serial Number | [optional] 

## Example

```python
from ahvac.models.pki_root_sign_intermediate_response import PkiRootSignIntermediateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PkiRootSignIntermediateResponse from a JSON string
pki_root_sign_intermediate_response_instance = PkiRootSignIntermediateResponse.from_json(json)
# print the JSON string representation of the object
print(PkiRootSignIntermediateResponse.to_json())

# convert the object into a dict
pki_root_sign_intermediate_response_dict = pki_root_sign_intermediate_response_instance.to_dict()
# create an instance of PkiRootSignIntermediateResponse from a dict
pki_root_sign_intermediate_response_from_dict = PkiRootSignIntermediateResponse.from_dict(pki_root_sign_intermediate_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


