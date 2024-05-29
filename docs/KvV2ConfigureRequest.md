# KvV2ConfigureRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cas_required** | **bool** | If true, the backend will require the cas parameter to be set for each write | [optional] 
**delete_version_after** | **str** | If set, the length of time before a version is deleted. A negative duration disables the use of delete_version_after on all keys. A zero duration clears the current setting. Accepts a Go duration format string. | [optional] 
**max_versions** | **int** | The number of versions to keep for each key. Defaults to 10 | [optional] 

## Example

```python
from ahvac.models.kv_v2_configure_request import KvV2ConfigureRequest

# TODO update the JSON string below
json = "{}"
# create an instance of KvV2ConfigureRequest from a JSON string
kv_v2_configure_request_instance = KvV2ConfigureRequest.from_json(json)
# print the JSON string representation of the object
print(KvV2ConfigureRequest.to_json())

# convert the object into a dict
kv_v2_configure_request_dict = kv_v2_configure_request_instance.to_dict()
# create an instance of KvV2ConfigureRequest from a dict
kv_v2_configure_request_from_dict = KvV2ConfigureRequest.from_dict(kv_v2_configure_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


