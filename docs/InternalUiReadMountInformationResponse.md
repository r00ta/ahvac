# InternalUiReadMountInformationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessor** | **str** |  | [optional] 
**config** | **object** |  | [optional] 
**description** | **str** |  | [optional] 
**external_entropy_access** | **bool** |  | [optional] 
**local** | **bool** |  | [optional] 
**options** | **object** |  | [optional] 
**path** | **str** |  | [optional] 
**plugin_version** | **str** |  | [optional] 
**running_plugin_version** | **str** |  | [optional] 
**running_sha256** | **str** |  | [optional] 
**seal_wrap** | **bool** |  | [optional] 
**type** | **str** |  | [optional] 
**uuid** | **str** |  | [optional] 

## Example

```python
from ahvac.models.internal_ui_read_mount_information_response import InternalUiReadMountInformationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InternalUiReadMountInformationResponse from a JSON string
internal_ui_read_mount_information_response_instance = InternalUiReadMountInformationResponse.from_json(json)
# print the JSON string representation of the object
print(InternalUiReadMountInformationResponse.to_json())

# convert the object into a dict
internal_ui_read_mount_information_response_dict = internal_ui_read_mount_information_response_instance.to_dict()
# create an instance of InternalUiReadMountInformationResponse from a dict
internal_ui_read_mount_information_response_from_dict = InternalUiReadMountInformationResponse.from_dict(internal_ui_read_mount_information_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


