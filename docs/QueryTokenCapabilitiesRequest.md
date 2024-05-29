# QueryTokenCapabilitiesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **List[str]** | Use &#39;paths&#39; instead. | [optional] 
**paths** | **List[str]** | Paths on which capabilities are being queried. | [optional] 
**token** | **str** | Token for which capabilities are being queried. | [optional] 

## Example

```python
from ahvac.models.query_token_capabilities_request import QueryTokenCapabilitiesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QueryTokenCapabilitiesRequest from a JSON string
query_token_capabilities_request_instance = QueryTokenCapabilitiesRequest.from_json(json)
# print the JSON string representation of the object
print(QueryTokenCapabilitiesRequest.to_json())

# convert the object into a dict
query_token_capabilities_request_dict = query_token_capabilities_request_instance.to_dict()
# create an instance of QueryTokenCapabilitiesRequest from a dict
query_token_capabilities_request_from_dict = QueryTokenCapabilitiesRequest.from_dict(query_token_capabilities_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


