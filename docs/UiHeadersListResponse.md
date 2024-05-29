# UiHeadersListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keys** | **List[str]** | Lists of configured UI headers. Omitted if list is empty | [optional] 

## Example

```python
from ahvac.models.ui_headers_list_response import UiHeadersListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UiHeadersListResponse from a JSON string
ui_headers_list_response_instance = UiHeadersListResponse.from_json(json)
# print the JSON string representation of the object
print(UiHeadersListResponse.to_json())

# convert the object into a dict
ui_headers_list_response_dict = ui_headers_list_response_instance.to_dict()
# create an instance of UiHeadersListResponse from a dict
ui_headers_list_response_from_dict = UiHeadersListResponse.from_dict(ui_headers_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


