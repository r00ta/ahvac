# EntityUpdateByIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disabled** | **bool** | If set true, tokens tied to this identity will not be able to be used (but will not be revoked). | [optional] 
**metadata** | **object** | Metadata to be associated with the entity. In CLI, this parameter can be repeated multiple times, and it all gets merged together. For example: vault &lt;command&gt; &lt;path&gt; metadata&#x3D;key1&#x3D;value1 metadata&#x3D;key2&#x3D;value2 | [optional] 
**name** | **str** | Name of the entity | [optional] 
**policies** | **List[str]** | Policies to be tied to the entity. | [optional] 

## Example

```python
from ahvac.models.entity_update_by_id_request import EntityUpdateByIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EntityUpdateByIdRequest from a JSON string
entity_update_by_id_request_instance = EntityUpdateByIdRequest.from_json(json)
# print the JSON string representation of the object
print(EntityUpdateByIdRequest.to_json())

# convert the object into a dict
entity_update_by_id_request_dict = entity_update_by_id_request_instance.to_dict()
# create an instance of EntityUpdateByIdRequest from a dict
entity_update_by_id_request_from_dict = EntityUpdateByIdRequest.from_dict(entity_update_by_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


