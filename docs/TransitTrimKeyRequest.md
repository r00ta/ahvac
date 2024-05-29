# TransitTrimKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_available_version** | **int** | The minimum available version for the key ring. All versions before this version will be permanently deleted. This value can at most be equal to the lesser of &#39;min_decryption_version&#39; and &#39;min_encryption_version&#39;. This is not allowed to be set when either &#39;min_encryption_version&#39; or &#39;min_decryption_version&#39; is set to zero. | [optional] 

## Example

```python
from ahvac.models.transit_trim_key_request import TransitTrimKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransitTrimKeyRequest from a JSON string
transit_trim_key_request_instance = TransitTrimKeyRequest.from_json(json)
# print the JSON string representation of the object
print(TransitTrimKeyRequest.to_json())

# convert the object into a dict
transit_trim_key_request_dict = transit_trim_key_request_instance.to_dict()
# create an instance of TransitTrimKeyRequest from a dict
transit_trim_key_request_from_dict = TransitTrimKeyRequest.from_dict(transit_trim_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


