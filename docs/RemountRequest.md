# RemountRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** | The previous mount point. | [optional] 
**to** | **str** | The new mount point. | [optional] 

## Example

```python
from ahvac.models.remount_request import RemountRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RemountRequest from a JSON string
remount_request_instance = RemountRequest.from_json(json)
# print the JSON string representation of the object
print(RemountRequest.to_json())

# convert the object into a dict
remount_request_dict = remount_request_instance.to_dict()
# create an instance of RemountRequest from a dict
remount_request_from_dict = RemountRequest.from_dict(remount_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


