# KvV2WriteMetadataRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cas_required** | **bool** | If true the key will require the cas parameter to be set on all write requests. If false, the backend’s configuration will be used. | [optional] 
**custom_metadata** | **object** | User-provided key-value pairs that are used to describe arbitrary and version-agnostic information about a secret. | [optional] 
**delete_version_after** | **str** | The length of time before a version is deleted. If not set, the backend&#39;s configured delete_version_after is used. Cannot be greater than the backend&#39;s delete_version_after. A zero duration clears the current setting. A negative duration will cause an error. | [optional] 
**max_versions** | **int** | The number of versions to keep. If not set, the backend’s configured max version is used. | [optional] 

## Example

```python
from ahvac.models.kv_v2_write_metadata_request import KvV2WriteMetadataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of KvV2WriteMetadataRequest from a JSON string
kv_v2_write_metadata_request_instance = KvV2WriteMetadataRequest.from_json(json)
# print the JSON string representation of the object
print(KvV2WriteMetadataRequest.to_json())

# convert the object into a dict
kv_v2_write_metadata_request_dict = kv_v2_write_metadata_request_instance.to_dict()
# create an instance of KvV2WriteMetadataRequest from a dict
kv_v2_write_metadata_request_from_dict = KvV2WriteMetadataRequest.from_dict(kv_v2_write_metadata_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


