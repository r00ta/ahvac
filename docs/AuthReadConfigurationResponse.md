# AuthReadConfigurationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessor** | **str** |  | [optional] 
**config** | **object** |  | [optional] 
**deprecation_status** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**external_entropy_access** | **bool** |  | [optional] 
**local** | **bool** |  | [optional] 
**options** | **object** |  | [optional] 
**plugin_version** | **str** |  | [optional] 
**running_plugin_version** | **str** |  | [optional] 
**running_sha256** | **str** |  | [optional] 
**seal_wrap** | **bool** |  | [optional] 
**type** | **str** |  | [optional] 
**uuid** | **str** |  | [optional] 

## Example

```python
from ahvac.models.auth_read_configuration_response import AuthReadConfigurationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuthReadConfigurationResponse from a JSON string
auth_read_configuration_response_instance = AuthReadConfigurationResponse.from_json(json)
# print the JSON string representation of the object
print(AuthReadConfigurationResponse.to_json())

# convert the object into a dict
auth_read_configuration_response_dict = auth_read_configuration_response_instance.to_dict()
# create an instance of AuthReadConfigurationResponse from a dict
auth_read_configuration_response_from_dict = AuthReadConfigurationResponse.from_dict(auth_read_configuration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


