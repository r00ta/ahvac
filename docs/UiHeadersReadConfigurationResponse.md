# UiHeadersReadConfigurationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | returns the first header value when &#x60;multivalue&#x60; request parameter is false | [optional] 
**values** | **List[str]** | returns all header values when &#x60;multivalue&#x60; request parameter is true | [optional] 

## Example

```python
from ahvac.models.ui_headers_read_configuration_response import UiHeadersReadConfigurationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UiHeadersReadConfigurationResponse from a JSON string
ui_headers_read_configuration_response_instance = UiHeadersReadConfigurationResponse.from_json(json)
# print the JSON string representation of the object
print(UiHeadersReadConfigurationResponse.to_json())

# convert the object into a dict
ui_headers_read_configuration_response_dict = ui_headers_read_configuration_response_instance.to_dict()
# create an instance of UiHeadersReadConfigurationResponse from a dict
ui_headers_read_configuration_response_from_dict = UiHeadersReadConfigurationResponse.from_dict(ui_headers_read_configuration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


