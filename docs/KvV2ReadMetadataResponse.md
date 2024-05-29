# KvV2ReadMetadataResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cas_required** | **bool** |  | [optional] 
**created_time** | **datetime** |  | [optional] 
**current_version** | **int** |  | [optional] 
**custom_metadata** | **object** | User-provided key-value pairs that are used to describe arbitrary and version-agnostic information about a secret. | [optional] 
**delete_version_after** | **str** | The length of time before a version is deleted. | [optional] 
**max_versions** | **int** | The number of versions to keep | [optional] 
**oldest_version** | **int** |  | [optional] 
**updated_time** | **datetime** |  | [optional] 
**versions** | **object** |  | [optional] 

## Example

```python
from ahvac.models.kv_v2_read_metadata_response import KvV2ReadMetadataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of KvV2ReadMetadataResponse from a JSON string
kv_v2_read_metadata_response_instance = KvV2ReadMetadataResponse.from_json(json)
# print the JSON string representation of the object
print(KvV2ReadMetadataResponse.to_json())

# convert the object into a dict
kv_v2_read_metadata_response_dict = kv_v2_read_metadata_response_instance.to_dict()
# create an instance of KvV2ReadMetadataResponse from a dict
kv_v2_read_metadata_response_from_dict = KvV2ReadMetadataResponse.from_dict(kv_v2_read_metadata_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


