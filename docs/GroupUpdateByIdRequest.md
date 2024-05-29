# GroupUpdateByIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_entity_ids** | **List[str]** | Entity IDs to be assigned as group members. | [optional] 
**member_group_ids** | **List[str]** | Group IDs to be assigned as group members. | [optional] 
**metadata** | **object** | Metadata to be associated with the group. In CLI, this parameter can be repeated multiple times, and it all gets merged together. For example: vault &lt;command&gt; &lt;path&gt; metadata&#x3D;key1&#x3D;value1 metadata&#x3D;key2&#x3D;value2 | [optional] 
**name** | **str** | Name of the group. | [optional] 
**policies** | **List[str]** | Policies to be tied to the group. | [optional] 
**type** | **str** | Type of the group, &#39;internal&#39; or &#39;external&#39;. Defaults to &#39;internal&#39; | [optional] 

## Example

```python
from ahvac.models.group_update_by_id_request import GroupUpdateByIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GroupUpdateByIdRequest from a JSON string
group_update_by_id_request_instance = GroupUpdateByIdRequest.from_json(json)
# print the JSON string representation of the object
print(GroupUpdateByIdRequest.to_json())

# convert the object into a dict
group_update_by_id_request_dict = group_update_by_id_request_instance.to_dict()
# create an instance of GroupUpdateByIdRequest from a dict
group_update_by_id_request_from_dict = GroupUpdateByIdRequest.from_dict(group_update_by_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


