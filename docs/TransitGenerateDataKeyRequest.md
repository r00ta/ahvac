# TransitGenerateDataKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bits** | **int** | Number of bits for the key; currently 128, 256, and 512 bits are supported. Defaults to 256. | [optional] [default to 256]
**context** | **str** | Context for key derivation. Required for derived keys. | [optional] 
**key_version** | **int** | The version of the Vault key to use for encryption of the data key. Must be 0 (for latest) or a value greater than or equal to the min_encryption_version configured on the key. | [optional] 
**nonce** | **str** | Nonce for when convergent encryption v1 is used (only in Vault 0.6.1) | [optional] 

## Example

```python
from ahvac.models.transit_generate_data_key_request import TransitGenerateDataKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransitGenerateDataKeyRequest from a JSON string
transit_generate_data_key_request_instance = TransitGenerateDataKeyRequest.from_json(json)
# print the JSON string representation of the object
print(TransitGenerateDataKeyRequest.to_json())

# convert the object into a dict
transit_generate_data_key_request_dict = transit_generate_data_key_request_instance.to_dict()
# create an instance of TransitGenerateDataKeyRequest from a dict
transit_generate_data_key_request_from_dict = TransitGenerateDataKeyRequest.from_dict(transit_generate_data_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


