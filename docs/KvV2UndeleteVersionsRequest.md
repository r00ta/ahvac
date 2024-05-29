# KvV2UndeleteVersionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**versions** | **List[int]** | The versions to unarchive. The versions will be restored and their data will be returned on normal get requests. | [optional] 

## Example

```python
from ahvac.models.kv_v2_undelete_versions_request import KvV2UndeleteVersionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of KvV2UndeleteVersionsRequest from a JSON string
kv_v2_undelete_versions_request_instance = KvV2UndeleteVersionsRequest.from_json(json)
# print the JSON string representation of the object
print(KvV2UndeleteVersionsRequest.to_json())

# convert the object into a dict
kv_v2_undelete_versions_request_dict = kv_v2_undelete_versions_request_instance.to_dict()
# create an instance of KvV2UndeleteVersionsRequest from a dict
kv_v2_undelete_versions_request_from_dict = KvV2UndeleteVersionsRequest.from_dict(kv_v2_undelete_versions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


