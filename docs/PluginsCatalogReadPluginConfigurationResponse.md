# PluginsCatalogReadPluginConfigurationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**args** | **List[str]** | The args passed to plugin command. | [optional] 
**builtin** | **bool** |  | [optional] 
**command** | **str** | The command used to start the plugin. The executable defined in this command must exist in vault&#39;s plugin directory. | [optional] 
**deprecation_status** | **str** |  | [optional] 
**name** | **str** | The name of the plugin | [optional] 
**oci_image** | **str** | The name of the OCI image to be run, without the tag or SHA256. Must already be present on the machine. | [optional] 
**sha256** | **str** | The SHA256 sum of the executable or container to be run. This should be HEX encoded. | [optional] 
**version** | **str** | The semantic version of the plugin to use, or image tag if oci_image is provided. | [optional] 

## Example

```python
from ahvac.models.plugins_catalog_read_plugin_configuration_response import PluginsCatalogReadPluginConfigurationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PluginsCatalogReadPluginConfigurationResponse from a JSON string
plugins_catalog_read_plugin_configuration_response_instance = PluginsCatalogReadPluginConfigurationResponse.from_json(json)
# print the JSON string representation of the object
print(PluginsCatalogReadPluginConfigurationResponse.to_json())

# convert the object into a dict
plugins_catalog_read_plugin_configuration_response_dict = plugins_catalog_read_plugin_configuration_response_instance.to_dict()
# create an instance of PluginsCatalogReadPluginConfigurationResponse from a dict
plugins_catalog_read_plugin_configuration_response_from_dict = PluginsCatalogReadPluginConfigurationResponse.from_dict(plugins_catalog_read_plugin_configuration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


