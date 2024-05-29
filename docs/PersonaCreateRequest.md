# PersonaCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **str** | Entity ID to which this persona belongs to | [optional] 
**id** | **str** | ID of the persona | [optional] 
**metadata** | **object** | Metadata to be associated with the persona. In CLI, this parameter can be repeated multiple times, and it all gets merged together. For example: vault &lt;command&gt; &lt;path&gt; metadata&#x3D;key1&#x3D;value1 metadata&#x3D;key2&#x3D;value2 | [optional] 
**mount_accessor** | **str** | Mount accessor to which this persona belongs to | [optional] 
**name** | **str** | Name of the persona | [optional] 

## Example

```python
from ahvac.models.persona_create_request import PersonaCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PersonaCreateRequest from a JSON string
persona_create_request_instance = PersonaCreateRequest.from_json(json)
# print the JSON string representation of the object
print(PersonaCreateRequest.to_json())

# convert the object into a dict
persona_create_request_dict = persona_create_request_instance.to_dict()
# create an instance of PersonaCreateRequest from a dict
persona_create_request_from_dict = PersonaCreateRequest.from_dict(persona_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


