# PluginsCatalogListPluginsWithTypeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keys** | **List[str]** | List of plugin names in the catalog | [optional] 

## Example

```python
from ahvac.models.plugins_catalog_list_plugins_with_type_response import PluginsCatalogListPluginsWithTypeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PluginsCatalogListPluginsWithTypeResponse from a JSON string
plugins_catalog_list_plugins_with_type_response_instance = PluginsCatalogListPluginsWithTypeResponse.from_json(json)
# print the JSON string representation of the object
print(PluginsCatalogListPluginsWithTypeResponse.to_json())

# convert the object into a dict
plugins_catalog_list_plugins_with_type_response_dict = plugins_catalog_list_plugins_with_type_response_instance.to_dict()
# create an instance of PluginsCatalogListPluginsWithTypeResponse from a dict
plugins_catalog_list_plugins_with_type_response_from_dict = PluginsCatalogListPluginsWithTypeResponse.from_dict(plugins_catalog_list_plugins_with_type_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


