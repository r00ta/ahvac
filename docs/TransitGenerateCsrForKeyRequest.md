# TransitGenerateCsrForKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**csr** | **str** | PEM encoded CSR template. The information attributes will be used as a basis for the CSR with the key in transit. If not set, an empty CSR is returned. | [optional] 
**version** | **int** | Optional version of key, &#39;latest&#39; if not set | [optional] 

## Example

```python
from ahvac.models.transit_generate_csr_for_key_request import TransitGenerateCsrForKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransitGenerateCsrForKeyRequest from a JSON string
transit_generate_csr_for_key_request_instance = TransitGenerateCsrForKeyRequest.from_json(json)
# print the JSON string representation of the object
print(TransitGenerateCsrForKeyRequest.to_json())

# convert the object into a dict
transit_generate_csr_for_key_request_dict = transit_generate_csr_for_key_request_instance.to_dict()
# create an instance of TransitGenerateCsrForKeyRequest from a dict
transit_generate_csr_for_key_request_from_dict = TransitGenerateCsrForKeyRequest.from_dict(transit_generate_csr_for_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


