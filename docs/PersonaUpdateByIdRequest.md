# PersonaUpdateByIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **str** | Entity ID to which this persona should be tied to | [optional] 
**metadata** | **object** | Metadata to be associated with the persona. In CLI, this parameter can be repeated multiple times, and it all gets merged together. For example: vault &lt;command&gt; &lt;path&gt; metadata&#x3D;key1&#x3D;value1 metadata&#x3D;key2&#x3D;value2 | [optional] 
**mount_accessor** | **str** | Mount accessor to which this persona belongs to | [optional] 
**name** | **str** | Name of the persona | [optional] 

## Example

```python
from ahvac.models.persona_update_by_id_request import PersonaUpdateByIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PersonaUpdateByIdRequest from a JSON string
persona_update_by_id_request_instance = PersonaUpdateByIdRequest.from_json(json)
# print the JSON string representation of the object
print(PersonaUpdateByIdRequest.to_json())

# convert the object into a dict
persona_update_by_id_request_dict = persona_update_by_id_request_instance.to_dict()
# create an instance of PersonaUpdateByIdRequest from a dict
persona_update_by_id_request_from_dict = PersonaUpdateByIdRequest.from_dict(persona_update_by_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


