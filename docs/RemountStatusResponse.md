# RemountStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**migration_id** | **str** |  | [optional] 
**migration_info** | **object** |  | [optional] 

## Example

```python
from ahvac.models.remount_status_response import RemountStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RemountStatusResponse from a JSON string
remount_status_response_instance = RemountStatusResponse.from_json(json)
# print the JSON string representation of the object
print(RemountStatusResponse.to_json())

# convert the object into a dict
remount_status_response_dict = remount_status_response_instance.to_dict()
# create an instance of RemountStatusResponse from a dict
remount_status_response_from_dict = RemountStatusResponse.from_dict(remount_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


