# UiHeadersConfigureRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**multivalue** | **bool** | Returns multiple values if true | [optional] 
**values** | **List[str]** | The values to set the header. | [optional] 

## Example

```python
from ahvac.models.ui_headers_configure_request import UiHeadersConfigureRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UiHeadersConfigureRequest from a JSON string
ui_headers_configure_request_instance = UiHeadersConfigureRequest.from_json(json)
# print the JSON string representation of the object
print(UiHeadersConfigureRequest.to_json())

# convert the object into a dict
ui_headers_configure_request_dict = ui_headers_configure_request_instance.to_dict()
# create an instance of UiHeadersConfigureRequest from a dict
ui_headers_configure_request_from_dict = UiHeadersConfigureRequest.from_dict(ui_headers_configure_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


