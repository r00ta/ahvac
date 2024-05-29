# TransitRewrapRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_input** | **List[object]** | Specifies a list of items to be re-encrypted in a single batch. When this parameter is set, if the parameters &#39;ciphertext&#39;, &#39;context&#39; and &#39;nonce&#39; are also set, they will be ignored. Any batch output will preserve the order of the batch input. | [optional] 
**ciphertext** | **str** | Ciphertext value to rewrap | [optional] 
**context** | **str** | Base64 encoded context for key derivation. Required for derived keys. | [optional] 
**key_version** | **int** | The version of the key to use for encryption. Must be 0 (for latest) or a value greater than or equal to the min_encryption_version configured on the key. | [optional] 
**nonce** | **str** | Nonce for when convergent encryption is used | [optional] 

## Example

```python
from ahvac.models.transit_rewrap_request import TransitRewrapRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransitRewrapRequest from a JSON string
transit_rewrap_request_instance = TransitRewrapRequest.from_json(json)
# print the JSON string representation of the object
print(TransitRewrapRequest.to_json())

# convert the object into a dict
transit_rewrap_request_dict = transit_rewrap_request_instance.to_dict()
# create an instance of TransitRewrapRequest from a dict
transit_rewrap_request_from_dict = TransitRewrapRequest.from_dict(transit_rewrap_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


