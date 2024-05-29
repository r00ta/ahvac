# GroupCreateAliasRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**canonical_id** | **str** | ID of the group to which this is an alias. | [optional] 
**id** | **str** | ID of the group alias. | [optional] 
**mount_accessor** | **str** | Mount accessor to which this alias belongs to. | [optional] 
**name** | **str** | Alias of the group. | [optional] 

## Example

```python
from ahvac.models.group_create_alias_request import GroupCreateAliasRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GroupCreateAliasRequest from a JSON string
group_create_alias_request_instance = GroupCreateAliasRequest.from_json(json)
# print the JSON string representation of the object
print(GroupCreateAliasRequest.to_json())

# convert the object into a dict
group_create_alias_request_dict = group_create_alias_request_instance.to_dict()
# create an instance of GroupCreateAliasRequest from a dict
group_create_alias_request_from_dict = GroupCreateAliasRequest.from_dict(group_create_alias_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


