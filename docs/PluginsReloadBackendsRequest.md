# PluginsReloadBackendsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mounts** | **List[str]** | The mount paths of the plugin backends to reload. | [optional] 
**plugin** | **str** | The name of the plugin to reload, as registered in the plugin catalog. | [optional] 
**scope** | **str** |  | [optional] 

## Example

```python
from ahvac.models.plugins_reload_backends_request import PluginsReloadBackendsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PluginsReloadBackendsRequest from a JSON string
plugins_reload_backends_request_instance = PluginsReloadBackendsRequest.from_json(json)
# print the JSON string representation of the object
print(PluginsReloadBackendsRequest.to_json())

# convert the object into a dict
plugins_reload_backends_request_dict = plugins_reload_backends_request_instance.to_dict()
# create an instance of PluginsReloadBackendsRequest from a dict
plugins_reload_backends_request_from_dict = PluginsReloadBackendsRequest.from_dict(plugins_reload_backends_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


