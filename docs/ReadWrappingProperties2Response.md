# ReadWrappingProperties2Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creation_path** | **str** |  | [optional] 
**creation_time** | **datetime** |  | [optional] 
**creation_ttl** | **str** |  | [optional] 

## Example

```python
from ahvac.models.read_wrapping_properties2_response import ReadWrappingProperties2Response

# TODO update the JSON string below
json = "{}"
# create an instance of ReadWrappingProperties2Response from a JSON string
read_wrapping_properties2_response_instance = ReadWrappingProperties2Response.from_json(json)
# print the JSON string representation of the object
print(ReadWrappingProperties2Response.to_json())

# convert the object into a dict
read_wrapping_properties2_response_dict = read_wrapping_properties2_response_instance.to_dict()
# create an instance of ReadWrappingProperties2Response from a dict
read_wrapping_properties2_response_from_dict = ReadWrappingProperties2Response.from_dict(read_wrapping_properties2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


