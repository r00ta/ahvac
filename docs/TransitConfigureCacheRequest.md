# TransitConfigureCacheRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | **int** | Size of cache, use 0 for an unlimited cache size, defaults to 0 | [optional] [default to 0]

## Example

```python
from ahvac.models.transit_configure_cache_request import TransitConfigureCacheRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransitConfigureCacheRequest from a JSON string
transit_configure_cache_request_instance = TransitConfigureCacheRequest.from_json(json)
# print the JSON string representation of the object
print(TransitConfigureCacheRequest.to_json())

# convert the object into a dict
transit_configure_cache_request_dict = transit_configure_cache_request_instance.to_dict()
# create an instance of TransitConfigureCacheRequest from a dict
transit_configure_cache_request_from_dict = TransitConfigureCacheRequest.from_dict(transit_configure_cache_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


