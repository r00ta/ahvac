# ReadWrappingPropertiesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creation_path** | **str** |  | [optional] 
**creation_time** | **datetime** |  | [optional] 
**creation_ttl** | **str** |  | [optional] 

## Example

```python
from ahvac.models.read_wrapping_properties_response import ReadWrappingPropertiesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadWrappingPropertiesResponse from a JSON string
read_wrapping_properties_response_instance = ReadWrappingPropertiesResponse.from_json(json)
# print the JSON string representation of the object
print(ReadWrappingPropertiesResponse.to_json())

# convert the object into a dict
read_wrapping_properties_response_dict = read_wrapping_properties_response_instance.to_dict()
# create an instance of ReadWrappingPropertiesResponse from a dict
read_wrapping_properties_response_from_dict = ReadWrappingPropertiesResponse.from_dict(read_wrapping_properties_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


