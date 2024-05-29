# RawWriteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compressed** | **bool** |  | [optional] 
**compression_type** | **str** |  | [optional] 
**encoding** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from ahvac.models.raw_write_request import RawWriteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RawWriteRequest from a JSON string
raw_write_request_instance = RawWriteRequest.from_json(json)
# print the JSON string representation of the object
print(RawWriteRequest.to_json())

# convert the object into a dict
raw_write_request_dict = raw_write_request_instance.to_dict()
# create an instance of RawWriteRequest from a dict
raw_write_request_from_dict = RawWriteRequest.from_dict(raw_write_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


