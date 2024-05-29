# EntityMergeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conflicting_alias_ids_to_keep** | **List[str]** | Alias IDs to keep in case of conflicting aliases. Ignored if no conflicting aliases found | [optional] 
**force** | **bool** | Setting this will follow the &#39;mine&#39; strategy for merging MFA secrets. If there are secrets of the same type both in entities that are merged from and in entity into which all others are getting merged, secrets in the destination will be unaltered. If not set, this API will throw an error containing all the conflicts. | [optional] 
**from_entity_ids** | **List[str]** | Entity IDs which need to get merged | [optional] 
**to_entity_id** | **str** | Entity ID into which all the other entities need to get merged | [optional] 

## Example

```python
from ahvac.models.entity_merge_request import EntityMergeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EntityMergeRequest from a JSON string
entity_merge_request_instance = EntityMergeRequest.from_json(json)
# print the JSON string representation of the object
print(EntityMergeRequest.to_json())

# convert the object into a dict
entity_merge_request_dict = entity_merge_request_instance.to_dict()
# create an instance of EntityMergeRequest from a dict
entity_merge_request_from_dict = EntityMergeRequest.from_dict(entity_merge_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


