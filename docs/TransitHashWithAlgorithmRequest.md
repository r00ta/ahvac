# TransitHashWithAlgorithmRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | **str** | Algorithm to use (POST body parameter). Valid values are: * sha2-224 * sha2-256 * sha2-384 * sha2-512 * sha3-224 * sha3-256 * sha3-384 * sha3-512 Defaults to \&quot;sha2-256\&quot;. | [optional] [default to 'sha2-256']
**format** | **str** | Encoding format to use. Can be \&quot;hex\&quot; or \&quot;base64\&quot;. Defaults to \&quot;hex\&quot;. | [optional] [default to 'hex']
**input** | **str** | The base64-encoded input data | [optional] 

## Example

```python
from ahvac.models.transit_hash_with_algorithm_request import TransitHashWithAlgorithmRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransitHashWithAlgorithmRequest from a JSON string
transit_hash_with_algorithm_request_instance = TransitHashWithAlgorithmRequest.from_json(json)
# print the JSON string representation of the object
print(TransitHashWithAlgorithmRequest.to_json())

# convert the object into a dict
transit_hash_with_algorithm_request_dict = transit_hash_with_algorithm_request_instance.to_dict()
# create an instance of TransitHashWithAlgorithmRequest from a dict
transit_hash_with_algorithm_request_from_dict = TransitHashWithAlgorithmRequest.from_dict(transit_hash_with_algorithm_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


