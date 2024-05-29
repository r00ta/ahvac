# MountsReadConfigurationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessor** | **str** |  | [optional] 
**config** | **object** | Configuration for this mount, such as default_lease_ttl and max_lease_ttl. | [optional] 
**deprecation_status** | **str** |  | [optional] 
**description** | **str** | User-friendly description for this mount. | [optional] 
**external_entropy_access** | **bool** |  | [optional] 
**local** | **bool** | Mark the mount as a local mount, which is not replicated and is unaffected by replication. | [optional] [default to False]
**options** | **object** | The options to pass into the backend. Should be a json object with string keys and values. | [optional] 
**plugin_version** | **str** | The semantic version of the plugin to use, or image tag if oci_image is provided. | [optional] 
**running_plugin_version** | **str** |  | [optional] 
**running_sha256** | **str** |  | [optional] 
**seal_wrap** | **bool** | Whether to turn on seal wrapping for the mount. | [optional] [default to False]
**type** | **str** | The type of the backend. Example: \&quot;passthrough\&quot; | [optional] 
**uuid** | **str** |  | [optional] 

## Example

```python
from ahvac.models.mounts_read_configuration_response import MountsReadConfigurationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MountsReadConfigurationResponse from a JSON string
mounts_read_configuration_response_instance = MountsReadConfigurationResponse.from_json(json)
# print the JSON string representation of the object
print(MountsReadConfigurationResponse.to_json())

# convert the object into a dict
mounts_read_configuration_response_dict = mounts_read_configuration_response_instance.to_dict()
# create an instance of MountsReadConfigurationResponse from a dict
mounts_read_configuration_response_from_dict = MountsReadConfigurationResponse.from_dict(mounts_read_configuration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


