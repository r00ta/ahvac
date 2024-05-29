# PkiGenerateIntermediateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**csr** | **str** | Certificate signing request. | [optional] 
**key_id** | **str** | Id of the key. | [optional] 
**private_key** | **str** | Generated private key. | [optional] 
**private_key_type** | **str** | Specifies the format used for marshaling the private key. | [optional] 

## Example

```python
from ahvac.models.pki_generate_intermediate_response import PkiGenerateIntermediateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PkiGenerateIntermediateResponse from a JSON string
pki_generate_intermediate_response_instance = PkiGenerateIntermediateResponse.from_json(json)
# print the JSON string representation of the object
print(PkiGenerateIntermediateResponse.to_json())

# convert the object into a dict
pki_generate_intermediate_response_dict = pki_generate_intermediate_response_instance.to_dict()
# create an instance of PkiGenerateIntermediateResponse from a dict
pki_generate_intermediate_response_from_dict = PkiGenerateIntermediateResponse.from_dict(pki_generate_intermediate_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


