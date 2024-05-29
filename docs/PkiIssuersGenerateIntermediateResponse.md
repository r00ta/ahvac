# PkiIssuersGenerateIntermediateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**csr** | **str** | Certificate signing request. | [optional] 
**key_id** | **str** | Id of the key. | [optional] 
**private_key** | **str** | Generated private key. | [optional] 
**private_key_type** | **str** | Specifies the format used for marshaling the private key. | [optional] 

## Example

```python
from ahvac.models.pki_issuers_generate_intermediate_response import PkiIssuersGenerateIntermediateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PkiIssuersGenerateIntermediateResponse from a JSON string
pki_issuers_generate_intermediate_response_instance = PkiIssuersGenerateIntermediateResponse.from_json(json)
# print the JSON string representation of the object
print(PkiIssuersGenerateIntermediateResponse.to_json())

# convert the object into a dict
pki_issuers_generate_intermediate_response_dict = pki_issuers_generate_intermediate_response_instance.to_dict()
# create an instance of PkiIssuersGenerateIntermediateResponse from a dict
pki_issuers_generate_intermediate_response_from_dict = PkiIssuersGenerateIntermediateResponse.from_dict(pki_issuers_generate_intermediate_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


