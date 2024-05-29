# KvV2WriteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** | The contents of the data map will be stored and returned on read. | [optional] 
**options** | **object** | Options for writing a KV entry. Set the \&quot;cas\&quot; value to use a Check-And-Set operation. If not set the write will be allowed. If set to 0 a write will only be allowed if the key doesn’t exist. If the index is non-zero the write will only be allowed if the key’s current version matches the version specified in the cas parameter. | [optional] 
**version** | **int** | If provided during a read, the value at the version number will be returned | [optional] 

## Example

```python
from ahvac.models.kv_v2_write_request import KvV2WriteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of KvV2WriteRequest from a JSON string
kv_v2_write_request_instance = KvV2WriteRequest.from_json(json)
# print the JSON string representation of the object
print(KvV2WriteRequest.to_json())

# convert the object into a dict
kv_v2_write_request_dict = kv_v2_write_request_instance.to_dict()
# create an instance of KvV2WriteRequest from a dict
kv_v2_write_request_from_dict = KvV2WriteRequest.from_dict(kv_v2_write_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


