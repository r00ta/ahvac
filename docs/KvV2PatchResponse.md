# KvV2PatchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_time** | **datetime** |  | [optional] 
**custom_metadata** | **object** |  | [optional] 
**deletion_time** | **str** |  | [optional] 
**destroyed** | **bool** |  | [optional] 
**version** | **int** |  | [optional] 

## Example

```python
from ahvac.models.kv_v2_patch_response import KvV2PatchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of KvV2PatchResponse from a JSON string
kv_v2_patch_response_instance = KvV2PatchResponse.from_json(json)
# print the JSON string representation of the object
print(KvV2PatchResponse.to_json())

# convert the object into a dict
kv_v2_patch_response_dict = kv_v2_patch_response_instance.to_dict()
# create an instance of KvV2PatchResponse from a dict
kv_v2_patch_response_from_dict = KvV2PatchResponse.from_dict(kv_v2_patch_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


