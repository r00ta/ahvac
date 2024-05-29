# CollectHostInformationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu** | **List[object]** |  | [optional] 
**cpu_times** | **List[object]** |  | [optional] 
**disk** | **List[object]** |  | [optional] 
**host** | **object** |  | [optional] 
**memory** | **object** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 

## Example

```python
from ahvac.models.collect_host_information_response import CollectHostInformationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CollectHostInformationResponse from a JSON string
collect_host_information_response_instance = CollectHostInformationResponse.from_json(json)
# print the JSON string representation of the object
print(CollectHostInformationResponse.to_json())

# convert the object into a dict
collect_host_information_response_dict = collect_host_information_response_instance.to_dict()
# create an instance of CollectHostInformationResponse from a dict
collect_host_information_response_from_dict = CollectHostInformationResponse.from_dict(collect_host_information_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


