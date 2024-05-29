# GroupLookUpRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias_id** | **str** | ID of the alias. | [optional] 
**alias_mount_accessor** | **str** | Accessor of the mount to which the alias belongs to. This should be supplied in conjunction with &#39;alias_name&#39;. | [optional] 
**alias_name** | **str** | Name of the alias. This should be supplied in conjunction with &#39;alias_mount_accessor&#39;. | [optional] 
**id** | **str** | ID of the group. | [optional] 
**name** | **str** | Name of the group. | [optional] 

## Example

```python
from ahvac.models.group_look_up_request import GroupLookUpRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GroupLookUpRequest from a JSON string
group_look_up_request_instance = GroupLookUpRequest.from_json(json)
# print the JSON string representation of the object
print(GroupLookUpRequest.to_json())

# convert the object into a dict
group_look_up_request_dict = group_look_up_request_instance.to_dict()
# create an instance of GroupLookUpRequest from a dict
group_look_up_request_from_dict = GroupLookUpRequest.from_dict(group_look_up_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


