# HaStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nodes** | **List[object]** |  | [optional] 

## Example

```python
from ahvac.models.ha_status_response import HaStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HaStatusResponse from a JSON string
ha_status_response_instance = HaStatusResponse.from_json(json)
# print the JSON string representation of the object
print(HaStatusResponse.to_json())

# convert the object into a dict
ha_status_response_dict = ha_status_response_instance.to_dict()
# create an instance of HaStatusResponse from a dict
ha_status_response_from_dict = HaStatusResponse.from_dict(ha_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


