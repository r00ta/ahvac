# KvV2DestroyVersionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**versions** | **List[int]** | The versions to destroy. Their data will be permanently deleted. | [optional] 

## Example

```python
from ahvac.models.kv_v2_destroy_versions_request import KvV2DestroyVersionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of KvV2DestroyVersionsRequest from a JSON string
kv_v2_destroy_versions_request_instance = KvV2DestroyVersionsRequest.from_json(json)
# print the JSON string representation of the object
print(KvV2DestroyVersionsRequest.to_json())

# convert the object into a dict
kv_v2_destroy_versions_request_dict = kv_v2_destroy_versions_request_instance.to_dict()
# create an instance of KvV2DestroyVersionsRequest from a dict
kv_v2_destroy_versions_request_from_dict = KvV2DestroyVersionsRequest.from_dict(kv_v2_destroy_versions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


