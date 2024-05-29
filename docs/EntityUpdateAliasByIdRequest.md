# EntityUpdateAliasByIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**canonical_id** | **str** | Entity ID to which this alias should be tied to | [optional] 
**custom_metadata** | **object** | User provided key-value pairs | [optional] 
**entity_id** | **str** | Entity ID to which this alias belongs to. This field is deprecated, use canonical_id. | [optional] 
**mount_accessor** | **str** | (Unused) | [optional] 
**name** | **str** | (Unused) | [optional] 

## Example

```python
from ahvac.models.entity_update_alias_by_id_request import EntityUpdateAliasByIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EntityUpdateAliasByIdRequest from a JSON string
entity_update_alias_by_id_request_instance = EntityUpdateAliasByIdRequest.from_json(json)
# print the JSON string representation of the object
print(EntityUpdateAliasByIdRequest.to_json())

# convert the object into a dict
entity_update_alias_by_id_request_dict = entity_update_alias_by_id_request_instance.to_dict()
# create an instance of EntityUpdateAliasByIdRequest from a dict
entity_update_alias_by_id_request_from_dict = EntityUpdateAliasByIdRequest.from_dict(entity_update_alias_by_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


