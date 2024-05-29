# TransitRestoreKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup** | **str** | Backed up key data to be restored. This should be the output from the &#39;backup/&#39; endpoint. | [optional] 
**force** | **bool** | If set and a key by the given name exists, force the restore operation and override the key. | [optional] [default to False]

## Example

```python
from ahvac.models.transit_restore_key_request import TransitRestoreKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransitRestoreKeyRequest from a JSON string
transit_restore_key_request_instance = TransitRestoreKeyRequest.from_json(json)
# print the JSON string representation of the object
print(TransitRestoreKeyRequest.to_json())

# convert the object into a dict
transit_restore_key_request_dict = transit_restore_key_request_instance.to_dict()
# create an instance of TransitRestoreKeyRequest from a dict
transit_restore_key_request_from_dict = TransitRestoreKeyRequest.from_dict(transit_restore_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


