# TransitRotateKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**managed_key_id** | **str** | The UUID of the managed key to use for the new version of this transit key | [optional] 
**managed_key_name** | **str** | The name of the managed key to use for the new version of this transit key | [optional] 

## Example

```python
from ahvac.models.transit_rotate_key_request import TransitRotateKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransitRotateKeyRequest from a JSON string
transit_rotate_key_request_instance = TransitRotateKeyRequest.from_json(json)
# print the JSON string representation of the object
print(TransitRotateKeyRequest.to_json())

# convert the object into a dict
transit_rotate_key_request_dict = transit_rotate_key_request_instance.to_dict()
# create an instance of TransitRotateKeyRequest from a dict
transit_rotate_key_request_from_dict = TransitRotateKeyRequest.from_dict(transit_rotate_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


