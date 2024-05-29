# EntityBatchDeleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_ids** | **List[str]** | Entity IDs to delete | [optional] 

## Example

```python
from ahvac.models.entity_batch_delete_request import EntityBatchDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EntityBatchDeleteRequest from a JSON string
entity_batch_delete_request_instance = EntityBatchDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(EntityBatchDeleteRequest.to_json())

# convert the object into a dict
entity_batch_delete_request_dict = entity_batch_delete_request_instance.to_dict()
# create an instance of EntityBatchDeleteRequest from a dict
entity_batch_delete_request_from_dict = EntityBatchDeleteRequest.from_dict(entity_batch_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


