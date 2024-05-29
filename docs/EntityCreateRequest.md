# EntityCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disabled** | **bool** | If set true, tokens tied to this identity will not be able to be used (but will not be revoked). | [optional] 
**id** | **str** | ID of the entity. If set, updates the corresponding existing entity. | [optional] 
**metadata** | **object** | Metadata to be associated with the entity. In CLI, this parameter can be repeated multiple times, and it all gets merged together. For example: vault &lt;command&gt; &lt;path&gt; metadata&#x3D;key1&#x3D;value1 metadata&#x3D;key2&#x3D;value2 | [optional] 
**name** | **str** | Name of the entity | [optional] 
**policies** | **List[str]** | Policies to be tied to the entity. | [optional] 

## Example

```python
from ahvac.models.entity_create_request import EntityCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EntityCreateRequest from a JSON string
entity_create_request_instance = EntityCreateRequest.from_json(json)
# print the JSON string representation of the object
print(EntityCreateRequest.to_json())

# convert the object into a dict
entity_create_request_dict = entity_create_request_instance.to_dict()
# create an instance of EntityCreateRequest from a dict
entity_create_request_from_dict = EntityCreateRequest.from_dict(entity_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


