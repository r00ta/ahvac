# PluginsRuntimesCatalogRegisterPluginRuntimeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cgroup_parent** | **str** | Optional parent cgroup for the container | [optional] 
**cpu_nanos** | **int** | The limit of runtime CPU in nanos | [optional] 
**memory_bytes** | **int** | The limit of runtime memory in bytes | [optional] 
**oci_runtime** | **str** | The OCI-compatible runtime (default \&quot;runsc\&quot;) | [optional] 

## Example

```python
from ahvac.models.plugins_runtimes_catalog_register_plugin_runtime_request import PluginsRuntimesCatalogRegisterPluginRuntimeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PluginsRuntimesCatalogRegisterPluginRuntimeRequest from a JSON string
plugins_runtimes_catalog_register_plugin_runtime_request_instance = PluginsRuntimesCatalogRegisterPluginRuntimeRequest.from_json(json)
# print the JSON string representation of the object
print(PluginsRuntimesCatalogRegisterPluginRuntimeRequest.to_json())

# convert the object into a dict
plugins_runtimes_catalog_register_plugin_runtime_request_dict = plugins_runtimes_catalog_register_plugin_runtime_request_instance.to_dict()
# create an instance of PluginsRuntimesCatalogRegisterPluginRuntimeRequest from a dict
plugins_runtimes_catalog_register_plugin_runtime_request_from_dict = PluginsRuntimesCatalogRegisterPluginRuntimeRequest.from_dict(plugins_runtimes_catalog_register_plugin_runtime_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


