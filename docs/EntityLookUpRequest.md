# EntityLookUpRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias_id** | **str** | ID of the alias. | [optional] 
**alias_mount_accessor** | **str** | Accessor of the mount to which the alias belongs to. This should be supplied in conjunction with &#39;alias_name&#39;. | [optional] 
**alias_name** | **str** | Name of the alias. This should be supplied in conjunction with &#39;alias_mount_accessor&#39;. | [optional] 
**id** | **str** | ID of the entity. | [optional] 
**name** | **str** | Name of the entity. | [optional] 

## Example

```python
from ahvac.models.entity_look_up_request import EntityLookUpRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EntityLookUpRequest from a JSON string
entity_look_up_request_instance = EntityLookUpRequest.from_json(json)
# print the JSON string representation of the object
print(EntityLookUpRequest.to_json())

# convert the object into a dict
entity_look_up_request_dict = entity_look_up_request_instance.to_dict()
# create an instance of EntityLookUpRequest from a dict
entity_look_up_request_from_dict = EntityLookUpRequest.from_dict(entity_look_up_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


