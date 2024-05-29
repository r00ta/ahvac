# KvV2ReadConfigurationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cas_required** | **bool** | If true, the backend will require the cas parameter to be set for each write | [optional] 
**delete_version_after** | **str** | The length of time before a version is deleted. | [optional] 
**max_versions** | **int** | The number of versions to keep for each key. | [optional] 

## Example

```python
from ahvac.models.kv_v2_read_configuration_response import KvV2ReadConfigurationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of KvV2ReadConfigurationResponse from a JSON string
kv_v2_read_configuration_response_instance = KvV2ReadConfigurationResponse.from_json(json)
# print the JSON string representation of the object
print(KvV2ReadConfigurationResponse.to_json())

# convert the object into a dict
kv_v2_read_configuration_response_dict = kv_v2_read_configuration_response_instance.to_dict()
# create an instance of KvV2ReadConfigurationResponse from a dict
kv_v2_read_configuration_response_from_dict = KvV2ReadConfigurationResponse.from_dict(kv_v2_read_configuration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


