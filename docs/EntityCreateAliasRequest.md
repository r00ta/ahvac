# EntityCreateAliasRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**canonical_id** | **str** | Entity ID to which this alias belongs | [optional] 
**custom_metadata** | **object** | User provided key-value pairs | [optional] 
**entity_id** | **str** | Entity ID to which this alias belongs. This field is deprecated, use canonical_id. | [optional] 
**id** | **str** | ID of the entity alias. If set, updates the corresponding entity alias. | [optional] 
**mount_accessor** | **str** | Mount accessor to which this alias belongs to; unused for a modify | [optional] 
**name** | **str** | Name of the alias; unused for a modify | [optional] 

## Example

```python
from ahvac.models.entity_create_alias_request import EntityCreateAliasRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EntityCreateAliasRequest from a JSON string
entity_create_alias_request_instance = EntityCreateAliasRequest.from_json(json)
# print the JSON string representation of the object
print(EntityCreateAliasRequest.to_json())

# convert the object into a dict
entity_create_alias_request_dict = entity_create_alias_request_instance.to_dict()
# create an instance of EntityCreateAliasRequest from a dict
entity_create_alias_request_from_dict = EntityCreateAliasRequest.from_dict(entity_create_alias_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


