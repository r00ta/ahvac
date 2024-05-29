# TransitGenerateHmacWithAlgorithmRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | **str** | Algorithm to use (POST body parameter). Valid values are: * sha2-224 * sha2-256 * sha2-384 * sha2-512 * sha3-224 * sha3-256 * sha3-384 * sha3-512 Defaults to \&quot;sha2-256\&quot;. | [optional] [default to 'sha2-256']
**batch_input** | **List[object]** | Specifies a list of items to be processed in a single batch. When this parameter is set, if the parameter &#39;input&#39; is also set, it will be ignored. Any batch output will preserve the order of the batch input. | [optional] 
**input** | **str** | The base64-encoded input data | [optional] 
**key_version** | **int** | The version of the key to use for generating the HMAC. Must be 0 (for latest) or a value greater than or equal to the min_encryption_version configured on the key. | [optional] 

## Example

```python
from ahvac.models.transit_generate_hmac_with_algorithm_request import TransitGenerateHmacWithAlgorithmRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransitGenerateHmacWithAlgorithmRequest from a JSON string
transit_generate_hmac_with_algorithm_request_instance = TransitGenerateHmacWithAlgorithmRequest.from_json(json)
# print the JSON string representation of the object
print(TransitGenerateHmacWithAlgorithmRequest.to_json())

# convert the object into a dict
transit_generate_hmac_with_algorithm_request_dict = transit_generate_hmac_with_algorithm_request_instance.to_dict()
# create an instance of TransitGenerateHmacWithAlgorithmRequest from a dict
transit_generate_hmac_with_algorithm_request_from_dict = TransitGenerateHmacWithAlgorithmRequest.from_dict(transit_generate_hmac_with_algorithm_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


