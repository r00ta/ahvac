# KvV2DeleteVersionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**versions** | **List[int]** | The versions to be archived. The versioned data will not be deleted, but it will no longer be returned in normal get requests. | [optional] 

## Example

```python
from ahvac.models.kv_v2_delete_versions_request import KvV2DeleteVersionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of KvV2DeleteVersionsRequest from a JSON string
kv_v2_delete_versions_request_instance = KvV2DeleteVersionsRequest.from_json(json)
# print the JSON string representation of the object
print(KvV2DeleteVersionsRequest.to_json())

# convert the object into a dict
kv_v2_delete_versions_request_dict = kv_v2_delete_versions_request_instance.to_dict()
# create an instance of KvV2DeleteVersionsRequest from a dict
kv_v2_delete_versions_request_from_dict = KvV2DeleteVersionsRequest.from_dict(kv_v2_delete_versions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


