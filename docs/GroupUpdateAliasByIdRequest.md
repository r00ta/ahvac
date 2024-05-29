# GroupUpdateAliasByIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**canonical_id** | **str** | ID of the group to which this is an alias. | [optional] 
**mount_accessor** | **str** | Mount accessor to which this alias belongs to. | [optional] 
**name** | **str** | Alias of the group. | [optional] 

## Example

```python
from ahvac.models.group_update_alias_by_id_request import GroupUpdateAliasByIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GroupUpdateAliasByIdRequest from a JSON string
group_update_alias_by_id_request_instance = GroupUpdateAliasByIdRequest.from_json(json)
# print the JSON string representation of the object
print(GroupUpdateAliasByIdRequest.to_json())

# convert the object into a dict
group_update_alias_by_id_request_dict = group_update_alias_by_id_request_instance.to_dict()
# create an instance of GroupUpdateAliasByIdRequest from a dict
group_update_alias_by_id_request_from_dict = GroupUpdateAliasByIdRequest.from_dict(group_update_alias_by_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


