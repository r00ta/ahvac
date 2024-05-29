# InternalUiListNamespacesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keys** | **List[str]** | field is only returned if there are one or more namespaces | [optional] 

## Example

```python
from ahvac.models.internal_ui_list_namespaces_response import InternalUiListNamespacesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InternalUiListNamespacesResponse from a JSON string
internal_ui_list_namespaces_response_instance = InternalUiListNamespacesResponse.from_json(json)
# print the JSON string representation of the object
print(InternalUiListNamespacesResponse.to_json())

# convert the object into a dict
internal_ui_list_namespaces_response_dict = internal_ui_list_namespaces_response_instance.to_dict()
# create an instance of InternalUiListNamespacesResponse from a dict
internal_ui_list_namespaces_response_from_dict = InternalUiListNamespacesResponse.from_dict(internal_ui_list_namespaces_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


