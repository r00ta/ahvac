# GroupCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the group. If set, updates the corresponding existing group. | [optional] 
**member_entity_ids** | **List[str]** | Entity IDs to be assigned as group members. | [optional] 
**member_group_ids** | **List[str]** | Group IDs to be assigned as group members. | [optional] 
**metadata** | **object** | Metadata to be associated with the group. In CLI, this parameter can be repeated multiple times, and it all gets merged together. For example: vault &lt;command&gt; &lt;path&gt; metadata&#x3D;key1&#x3D;value1 metadata&#x3D;key2&#x3D;value2 | [optional] 
**name** | **str** | Name of the group. | [optional] 
**policies** | **List[str]** | Policies to be tied to the group. | [optional] 
**type** | **str** | Type of the group, &#39;internal&#39; or &#39;external&#39;. Defaults to &#39;internal&#39; | [optional] 

## Example

```python
from ahvac.models.group_create_request import GroupCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GroupCreateRequest from a JSON string
group_create_request_instance = GroupCreateRequest.from_json(json)
# print the JSON string representation of the object
print(GroupCreateRequest.to_json())

# convert the object into a dict
group_create_request_dict = group_create_request_instance.to_dict()
# create an instance of GroupCreateRequest from a dict
group_create_request_from_dict = GroupCreateRequest.from_dict(group_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


