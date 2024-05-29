# TransitConfigureKeysRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disable_upsert** | **bool** | Whether to allow automatic upserting (creation) of keys on the encrypt endpoint. | [optional] 

## Example

```python
from ahvac.models.transit_configure_keys_request import TransitConfigureKeysRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransitConfigureKeysRequest from a JSON string
transit_configure_keys_request_instance = TransitConfigureKeysRequest.from_json(json)
# print the JSON string representation of the object
print(TransitConfigureKeysRequest.to_json())

# convert the object into a dict
transit_configure_keys_request_dict = transit_configure_keys_request_instance.to_dict()
# create an instance of TransitConfigureKeysRequest from a dict
transit_configure_keys_request_from_dict = TransitConfigureKeysRequest.from_dict(transit_configure_keys_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


