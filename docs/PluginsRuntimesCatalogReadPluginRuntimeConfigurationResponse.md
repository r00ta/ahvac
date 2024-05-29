# PluginsRuntimesCatalogReadPluginRuntimeConfigurationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cgroup_parent** | **str** | Optional parent cgroup for the container | [optional] 
**cpu_nanos** | **int** | The limit of runtime CPU in nanos | [optional] 
**memory_bytes** | **int** | The limit of runtime memory in bytes | [optional] 
**name** | **str** | The name of the plugin runtime | [optional] 
**oci_runtime** | **str** | The OCI-compatible runtime (default \&quot;runsc\&quot;) | [optional] 
**type** | **str** | The type of the plugin runtime | [optional] 

## Example

```python
from ahvac.models.plugins_runtimes_catalog_read_plugin_runtime_configuration_response import PluginsRuntimesCatalogReadPluginRuntimeConfigurationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PluginsRuntimesCatalogReadPluginRuntimeConfigurationResponse from a JSON string
plugins_runtimes_catalog_read_plugin_runtime_configuration_response_instance = PluginsRuntimesCatalogReadPluginRuntimeConfigurationResponse.from_json(json)
# print the JSON string representation of the object
print(PluginsRuntimesCatalogReadPluginRuntimeConfigurationResponse.to_json())

# convert the object into a dict
plugins_runtimes_catalog_read_plugin_runtime_configuration_response_dict = plugins_runtimes_catalog_read_plugin_runtime_configuration_response_instance.to_dict()
# create an instance of PluginsRuntimesCatalogReadPluginRuntimeConfigurationResponse from a dict
plugins_runtimes_catalog_read_plugin_runtime_configuration_response_from_dict = PluginsRuntimesCatalogReadPluginRuntimeConfigurationResponse.from_dict(plugins_runtimes_catalog_read_plugin_runtime_configuration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


